import pygame
import sys
import time
import random
from pygame.locals import *

redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)


def gameOver(playSurface, score):
    gameOverFont = pygame.font.SysFont("arial.ttf", 54)
    gameOverSurf = gameOverFont.render("Game Over!", True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (300, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    scoreFont = pygame.font.SysFont("arial.ttf", 54)
    scoreSurf = scoreFont.render("Score:" + str(score), True, greyColour)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (300, 50)
    playSurface.blit(scoreSurf, scoreRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    playSurface = pygame.display.set_mode((600, 460))
    pygame.display.set_caption("Snake Game")
    snakePosition = [100, 100]
    snakeSegments = [[100, 100]]
    raspberryPosition = [300, 300]
    raspberrySpawned = 1
    direction = "right"
    changeDirection = direction
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord("d"):
                    changeDirection = "right"
                if event.key == K_LEFT or event.key == ord("a"):
                    changeDirection = "left"
                if event.key == K_UP or event.key == ord("w"):
                    changeDirection = "up"
                if event.key == K_DOWN or event.key == ord("s"):
                    changeDirection = "down"
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        if changeDirection == "right" and not direction == "left":
            direction = changeDirection
        if changeDirection == "left" and not direction == "right":
            direction = changeDirection
        if changeDirection == "up" and not direction == "down":
            direction = changeDirection
        if changeDirection == "down" and not direction == "up":
            direction = changeDirection

        if direction == "right":
            snakePosition[0] += 20
        if direction == "left":
            snakePosition[0] -= 20
        if direction == "up":
            snakePosition[1] -= 20
        if direction == "down":
            snakePosition[1] += 20

        snakeSegments.insert(0, list(snakePosition))

        if (
            snakePosition[0] == raspberryPosition[0]
            and snakePosition[1] == raspberryPosition[1]
        ):
            raspberrySpawned = 0
        else:
            snakeSegments.pop()

        if raspberrySpawned == 0:
            x = random.randrange(1, 30)
            y = random.randrange(1, 23)
            raspberryPosition = [int(x * 20), int(y * 20)]
            raspberrySpawned = 1
            score += 1

        playSurface.fill(blackColour)
        for position in snakeSegments:
            pygame.draw.rect(
                playSurface, whiteColour, Rect(position[0], position[1], 20, 20)
            )
            pygame.draw.rect(
                playSurface,
                redColour,
                Rect(raspberryPosition[0], raspberryPosition[1], 20, 20),
            )

        pygame.display.flip()

        if snakePosition[0] > 600 or snakePosition[0] < 0:
            gameOver(playSurface, score)
            if snakePosition[1] > 460 or snakePosition[1] < 0:
                gameOver(playSurface, score)
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface, score)

        fpsClock.tick(5)


if __name__ == "__main__":
    main()
