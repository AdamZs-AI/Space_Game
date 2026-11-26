################################
# Ethan Adam et Maxence Karlik #
################################

# ----------------------------------#
# ------------- Import -------------#
# ----------------------------------#
import os
import random

import pygame

# ---------------------------------#
# ------------- Setup -------------#
# ---------------------------------#
size_mult = 0.8
screen_width = 600 * size_mult
screen_length = 1000 * size_mult
fps = 144
asteroids_width = 40
asteroid_speed = 400
asteroid_base_cooldown = 1
score = 0

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_length))
clock = pygame.time.Clock()
dt = 0.0
running = True
player_hitbox = pygame.Rect([screen_width / 2, 6 * screen_length / 7], (10, 10))
player_speed = 200
asteroids: list[pygame.Rect] = []

# --- Asteroid Initialization --- #
for i in range(3):
    first_asteroid_position = random.uniform(
        asteroids_width / 2, screen_width - asteroids_width
    )
    last_asteroid_position = random.uniform(
        first_asteroid_position + 2 * asteroids_width, screen_width - asteroids_width
    )
    asteroids.append(
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (
                first_asteroid_position,
                0.0 - i * asteroid_base_cooldown * asteroid_speed,
            ),
            asteroids_width / 2,
        )
    )
    asteroids.append(
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (last_asteroid_position, 0.0 - i * asteroid_base_cooldown * asteroid_speed),
            asteroids_width / 2,
        )
    )

# -------------------------------------#
# ------------- Game Loop -------------#
# -------------------------------------#
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # -------------------------------------#
    # ------------- Mechanics -------------#
    # -------------------------------------#

    # --- Manage Inputs --- #
    if keys[pygame.K_LEFT]:
        player_hitbox.x -= (
            player_speed * dt * 0.5
        )  # Jsp pourquoi j'ai besoin du 0.5 mais ça marche pas sans
    if keys[pygame.K_RIGHT]:
        player_hitbox.x += player_speed * dt
    if keys[pygame.K_e]:
        running = False

    for asteroid in asteroids:
        if asteroid.colliderect(player_hitbox):
            running = False

        if (asteroid.y > player_hitbox.y) and (
            asteroid.y <= player_hitbox.y + asteroid_speed * dt
        ):
            score += 0.5
            print(f"{score = }")

        if asteroid.y > screen.height:
            asteroid.y = 0.0

        asteroid[1] += asteroid_speed * dt

    # -------------------------------------#
    # ------------- Rendering -------------#
    # -------------------------------------#
    screen.fill("black")

    pygame.draw.rect(screen, (255, 255, 255), player_hitbox)

    for asteroid in asteroids:
        pygame.draw.circle(
            screen, (255, 255, 255), asteroid.center, asteroids_width / 2
        )

    pygame.display.flip()

    dt = clock.tick(fps) / 1000


pygame.quit()
