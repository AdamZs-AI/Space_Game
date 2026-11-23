################################
# Ethan Adam et Maxence Karlik #
################################

# --- Import --- #
import os
import random

import pygame

# --- Setup --- #
size_mult = 0.8
screen_width = 600 * size_mult
screen_length = 1000 * size_mult
fps = 144
asteroids_width = 40
asteroid_speed = 400
asteroid_base_cooldown = 1

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_length))
clock = pygame.time.Clock()
dt = 0.0
running = True
player_position = [screen_width / 2, 6 * screen_length / 7]
player_speed = 200
asteroids = []
asteroid_cooldown = 1


# --- Game Loop --- #
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # --- Mechanics --- #
    if keys[pygame.K_LEFT]:
        player_position[0] -= player_speed * dt
    if keys[pygame.K_RIGHT]:
        player_position[0] += player_speed * dt
    if keys[pygame.K_e]:
        running = False

    if asteroid_cooldown <= 0:
        first_asteroid_position = random.uniform(
            asteroids_width / 2, screen_width - asteroids_width
        )
        last_asteroid_position = random.uniform(
            first_asteroid_position + asteroids_width, screen_width - asteroids_width
        )
        asteroids.append([first_asteroid_position, 0.0])
        asteroids.append([last_asteroid_position, 0.0])

        asteroid_cooldown = asteroid_base_cooldown
    else:
        asteroid_cooldown -= dt

    for asteroid in asteroids:
        asteroid[1] += asteroid_speed * dt

    # --- Rendering --- #
    screen.fill("black")

    x, y = player_position
    pygame.draw.polygon(
        screen,
        (255, 255, 255),
        [
            (x, y - 15 * size_mult),
            (x - 15 * size_mult, y + 20 * size_mult),
            (x, y + 15 * size_mult),
            (x + 15 * size_mult, y + 20 * size_mult),
        ],
    )

    for asteroid in asteroids:
        pygame.draw.circle(screen, (255, 255, 255), asteroid, asteroids_width / 2)

    pygame.display.flip()

    dt = clock.tick(fps) / 1000

pygame.quit()
