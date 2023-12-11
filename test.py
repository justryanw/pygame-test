import sys
import pygame as pg
from pygame.locals import *
from pygame._sdl2.video import Window, Renderer, Texture

FONT_SIZE = 40

class Game:
    clock = pg.time.Clock()
    
    def __init__(self):
        pg.init()
        self.window = Window("SPRITE STACK TEST", (1920,1080))
        self.renderer = Renderer(self.window)
        self.renderer.draw_color = [100,100,100,100]

        self.font = pg.font.SysFont(None, FONT_SIZE)

        self.mainloop()

    def update(self, dt):
        for e in pg.event.get():
            if e.type == QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def draw(self):
        self.renderer.clear()

        fps = f'{Game.clock.get_fps() :.0f} FPS'
        tex = Texture.from_surface(self.renderer, self.font.render(fps, False, "green"))
        self.renderer.blit(tex, tex.get_rect())

        self.renderer.present()

    def mainloop(self):
        while True:
            dt = Game.clock.tick() / 1000
            self.update(dt)
            self.draw()

        

if __name__ == "__main__":
    game = Game()