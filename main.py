import pygame
import math

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("WASD Controlled Rectangle")

# Define rectangle properties
rect_width = 50
rect_height = 70
center_x = 200
center_y = 150
angle = 0
speed = 5

# Define clock
clock = pygame.time.Clock()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard input for movement and rotation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        # Move sideways based on the current angle
        center_x += speed * math.sin(math.radians(angle))
        center_y -= speed * math.cos(math.radians(angle))
    if keys[pygame.K_s]:
        center_x -= speed * math.sin(math.radians(angle))
        center_y += speed * math.cos(math.radians(angle))
    if keys[pygame.K_a]:
        angle += speed
    if keys[pygame.K_d]:
        angle -= speed

    # Clear the screen
    screen.fill(WHITE)

    # Calculate rotation matrix
    rotation_matrix = [[math.cos(math.radians(angle)), -math.sin(math.radians(angle))],
                       [math.sin(math.radians(angle)), math.cos(math.radians(angle))]]

    # Define original rectangle points
    points = [(0, 0), (rect_width, 0), (rect_width, rect_height), (0, rect_height)]

    # Rotate points around center
    rotated_points = []
    for point in points:
        x_offset = point[0] - rect_width / 2
        y_offset = point[1] - rect_height / 2
        rotated_x = rotation_matrix[0][0] * x_offset + rotation_matrix[0][1] * y_offset + center_x
        rotated_y = rotation_matrix[1][0] * x_offset + rotation_matrix[1][1] * y_offset + center_y
        rotated_points.append((rotated_x, rotated_y))

    # Draw the rotated rectangle
    pygame.draw.polygon(screen, RED, rotated_points)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
