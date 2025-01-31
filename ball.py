import pygame
import settings
import math


class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.radius = settings.BALL_RADIUS
        self.color = (255, 255, 255)

        self.is_aiming = False
        self.aim_location = None

        self.velocity_x = 0.0
        self.velocity_y = 0.0


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos_x), int(self.pos_y)), self.radius)

    def move(self, move_keys):
        if move_keys[pygame.K_LEFT]:
            self.pos_x -= settings.MOVE_SPEED
        if move_keys[pygame.K_RIGHT]:
            self.pos_x += settings.MOVE_SPEED
        if move_keys[pygame.K_UP]:
            self.pos_y -= settings.MOVE_SPEED
        if move_keys[pygame.K_DOWN]:
            self.pos_y += settings.MOVE_SPEED


    def handle_aiming(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.is_aiming = True
            print('aiming')
        if event_type == pygame.MOUSEBUTTONUP:
            self.is_aiming = False
            self.aim_location = pygame.mouse.get_pos()
            print('stopped aiming')
            print(f'({self.pos_x}, {self.pos_y}) - before hit')

            self.hit(self.aim_location)


    def hit(self, aim_location):
        dx = self.pos_x - aim_location[0]
        dy = self.pos_y - aim_location[1]
        power = math.sqrt(dx ** 2 + dy ** 2) * 0.2  # Convert drag to power
        angle = math.atan2(dy, dx)  # Calculate shot angle
        print(f'angle - {angle}')

        self.velocity_x = -power * math.cos(angle)  # Set velocity based on power and angle

        self.velocity_y = -power * math.sin(angle)
        print(f'vx - {self.velocity_y}, vy - {self.velocity_x}')



    def update(self, terrain):
        if abs(self.velocity_x) > 0.05 or abs(self.velocity_y) > 0.05:  # Ensure it moves while velocity is significant
            self.pos_x += self.velocity_x
            self.pos_y += self.velocity_y

            self.velocity_x *= settings.FRICTION
            self.velocity_y *= settings.FRICTION

            if self.pos_y + self.radius >= terrain.y_pos:
                self.pos_y = terrain.y_pos - self.radius  # Stop the ball on the ground
                self.velocity_y = 0  # Stop vertical movement

                # Apply slight bounce effect if speed is high
                if abs(self.velocity_x) > 0.5:
                    self.velocity_x *= 0.8  # Reduce horizontal speed after bounce

            # stop if movement to looow
            if abs(self.velocity_x) < 0.05:  # Set to 0 when movement is minimal
                self.velocity_x = 0
            if abs(self.velocity_y) < 0.05:
                self.velocity_y = 0

            print(f'({self.pos_x}, {self.pos_y}) - after hit')

