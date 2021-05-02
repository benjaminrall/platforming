from platform import Platform

from pygame.constants import K_SPACE
from player import Player
import pygame
import os
from personallib.camera import Camera

# Constants
WIN_WIDTH = 800
WIN_HEIGHT = 800
FRAMERATE = 120
ICON_IMG = pygame.image.load(os.path.join("imgs", "icon.png"))

# Pygame Setup
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Platforming Test")
pygame.display.set_icon(ICON_IMG)
clock = pygame.time.Clock()

# Objects
cam = Camera(win, 0, 0, 1)
cam.set_bounds((0, 0), (0, 300), (False, False, False, True))
player = Player(0, 0, 10)
platforms = []
platforms.append(Platform(-50, 10, 100, 12))

# Variables
running = True
movement = (0, 0)
cameraSmoothing = 0.95
keysPressed = {
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_SPACE: False
}
keyMovement = {
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
}

# Subroutines
def getMovement():
    m = (0, 0)
    for key in keysPressed:
        if keysPressed[key] and key in keyMovement:
            x = keyMovement[key]
            m = (m[0] + x[0], m[1] + x[1])
    return m

# Main Loop
if __name__ == '__main__':
    while running:

        dt = clock.tick(FRAMERATE) * 0.001

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in keysPressed:
                    keysPressed[event.key] = True
                    movement = getMovement()
            elif event.type == pygame.KEYUP:
                if event.key in keysPressed:
                    keysPressed[event.key] = False
                    movement = getMovement()
                    
        win.fill((255, 255, 255))
        player.draw(cam)
        for platform in platforms:
            platform.draw(cam)

        player.move((dt * movement[0], dt * movement[1]))
        cam.follow(player.get_pos(), (0, -30), smoothing=cameraSmoothing)

        player.jump(keysPressed[pygame.K_SPACE], dt)
        
        pygame.display.update()