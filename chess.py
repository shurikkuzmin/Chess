import pygame
pygame.init()

fps = 60
clock = pygame.time.Clock()

box_size = 80
size = (9 * box_size, 9 * box_size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")

sprites = pygame.image.load("sprites_classical.png")
white_pawn = sprites.subsurface(1000, 0, 200, 200)
white_pawn = pygame.transform.scale(white_pawn, (box_size, box_size))
white_bishop = sprites.subsurface(400, 0, 200, 200)
white_bishop = pygame.transform.scale(white_bishop, (box_size, box_size))
white_knight = sprites.subsurface(600, 0, 200, 200)
white_knight = pygame.transform.scale(white_knight, (box_size, box_size))


field=[[14,13,12,16,15,12,13,14],
       [11,11,11,11,11,11,11,11],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 1, 1, 1, 1, 1, 1, 1, 1],
       [ 4, 3, 2, 6, 5, 2, 3, 4]]

def draw_field():
    for row in range(8):
        for col in range(8):
            if field[row][col] == 1:
                screen.blit(white_pawn, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 2:
                screen.blit(white_bishop, ((col+1)*box_size, row*box_size))
            pygame.draw.rect(screen, (255, 255, 255), 
                             ((col+1)*box_size, row*box_size, box_size, box_size), 2)

running = True
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_field()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
