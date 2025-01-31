import pygame

import settings
from player import Player
from terrain import Terrain


class Game:
    def __init__(self):
        pygame.init()

        # if pygame.joystick.get_count() > 0:
        #     pygame.joystick.init()
        #     print(f"Joysticks detected: {pygame.joystick.get_count()}")
        # else:
        #     pygame.joystick.quit()


        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        pygame.display.set_caption('Golf2D')
        self.clock = pygame.time.Clock()

        self.players = Player(settings.SCREEN_WIDTH // 2,settings.SCREEN_HEIGHT // 2) ##TODO Replace with Player class
        self.terrain = Terrain()

        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(settings.FPS)

        pygame.quit()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.players.ball.handle_aiming(event.type)

    def update(self):
        keys = pygame.key.get_pressed()
        self.players.ball.move(keys)
        self.players.ball.update(self.terrain)



    def draw(self):
        self.screen.fill(settings.BLACK)
        self.players.ball.draw(self.screen)
        self.terrain.draw(self.screen)

        pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()








