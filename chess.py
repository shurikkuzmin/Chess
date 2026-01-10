import pygame
pygame.init()

fps = 60
clock = pygame.time.Clock()

box_size = 80
size = (9 * box_size, 9 * box_size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")

field=[[14,13,12,16,15,12,13,14],
       [11,11,11,11,11,11,11,11],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 1, 1, 1, 1, 1, 1, 1, 1],
       [ 4, 3, 2, 6, 5, 2, 3, 4]]

#def draw_field():

running = True
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
