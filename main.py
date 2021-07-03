from platform import Platform
import json
from player import Player
import pygame
import os
from personallib.camera import Camera

# Constants
WIN_WIDTH = 1000
WIN_HEIGHT = 800
FRAMERATE = 120
ICON_IMG = pygame.image.load(os.path.join("imgs", "icon.png"))

# Pygame Setup
pygame.font.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Platforming Test")
pygame.display.set_icon(ICON_IMG)
clock = pygame.time.Clock()

# Objects
cam = Camera(win, 0, 0, 1)
cam.set_bounds((0, 0), (0, 300), (False, False, False, True))
player = Player(0, 0, 10)
platforms = []
try:
    with open("platforms.json", "r") as f:
        platforms = json.load(f)
except:
    pass
platforms = [ Platform(p[0], p[1], p[2], p[3]) for p in platforms ]

# Variables
running = True
movement = (0, 0)
cameraSmoothing = 0.95
keysPressed = {
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_SPACE: False,
    pygame.K_LCTRL: False
}
keyMovement = {
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
}
font = pygame.font.SysFont(None, 48)
fontImage = font.render("you win!", True, (0, 0, 0))
debug = False

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
                with open("platforms.json", "w") as f:
                    json.dump([ p.get_rect() for p in platforms ], f)
                running = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in keysPressed:
                    keysPressed[event.key] = True
                    movement = getMovement()
                elif event.key == pygame.K_c and debug:
                    player.startPos = player.get_pos()
                elif event.key == pygame.K_F3:
                    debug = not debug
            elif event.type == pygame.KEYUP:
                if event.key in keysPressed:
                    keysPressed[event.key] = False
                    movement = getMovement()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and keysPressed[pygame.K_LCTRL] and debug:
                    m = cam.get_world_coord(pygame.mouse.get_pos())
                    platforms.append(Platform(m[0] - 50, m[1] - 6, 100, 12))
                elif event.button == 1:
                    m = cam.get_world_coord(pygame.mouse.get_pos())
                    print(m)
                    
        win.fill((255, 255, 255))
        player.draw(cam)

        player.move((dt * movement[0], dt * movement[1]))
        cam.follow(player.get_pos(), (0, -30), smoothing=cameraSmoothing)
        player.jump(keysPressed[pygame.K_SPACE], dt)

        for platform in platforms:
            platform.draw(cam)
            collision = platform.overlap(player)
            for c in collision:
                if c:
                    player.collided(platform, collision)

        if player.get_pos()[1] > 400:
            player.die()
        
        cam.blit(fontImage, (3080, -1200))

        pygame.display.update()