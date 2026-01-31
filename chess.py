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
white_rook = sprites.subsurface(800, 0, 200, 200)
white_rook = pygame.transform.scale(white_rook, (box_size, box_size))
white_queen = sprites.subsurface(0, 0, 200, 200)
white_queen = pygame.transform.scale(white_queen, (box_size, box_size)) 
white_king = sprites.subsurface(200, 0, 200, 200)
white_king = pygame.transform.scale(white_king, (box_size, box_size))
black_pawn = sprites.subsurface(1000, 200, 200, 200)
black_pawn = pygame.transform.scale(black_pawn, (box_size, box_size))
black_bishop = sprites.subsurface(400, 200, 200, 200)
black_bishop = pygame.transform.scale(black_bishop, (box_size, box_size))
black_knight = sprites.subsurface(600, 200, 200, 200)
black_knight = pygame.transform.scale(black_knight, (box_size, box_size))
black_rook = sprites.subsurface(800, 200, 200, 200)
black_rook = pygame.transform.scale(black_rook, (box_size, box_size))
black_queen = sprites.subsurface(0, 200, 200, 200)
black_queen = pygame.transform.scale(black_queen, (box_size, box_size)) 
black_king = sprites.subsurface(200, 200, 200, 200)
black_king = pygame.transform.scale(black_king, (box_size, box_size))

field=[[14,13,12,16,15,12,13,14],
       [11,11,11,11,11,11,11,11],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 1, 1, 1, 1, 1, 1, 1, 1],
       [ 4, 3, 2, 6, 5, 2, 3, 4]]

def draw_field():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    numbers = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    for i in range(8):
        font = pygame.font.SysFont('arial', 30)
        letter_surface = font.render(letters[i], True, (255, 255, 255))
        number_surface = font.render(numbers[i], True, (255, 255, 255))
        letter_rect = letter_surface.get_rect()
        number_rect = number_surface.get_rect()
        letter_rect.center = ((i+1)*box_size + box_size//2, 8*box_size + box_size//2)
        number_rect.center = (box_size//2, i*box_size + box_size//2)

        screen.blit(number_surface, number_rect)
        screen.blit(letter_surface, letter_rect)
    
    for row in range(8):
        for col in range(8):
            if (row+col) % 2 == 0:
                color = (235, 209, 166)
            else:
                color = (165, 94, 34)
            pygame.draw.rect(screen, color, 
                             ((col+1)*box_size, row*box_size, box_size, box_size))
            if field[row][col] == 1:
                screen.blit(white_pawn, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 2:
                screen.blit(white_bishop, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 3:
                screen.blit(white_knight, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 4:
                screen.blit(white_rook, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 5:
                screen.blit(white_queen, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 6:
                screen.blit(white_king, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 11:
                screen.blit(black_pawn, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 12:
                screen.blit(black_bishop, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 13:
                screen.blit(black_knight, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 14:
                screen.blit(black_rook, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 15:
                screen.blit(black_queen, ((col+1)*box_size, row*box_size))
            elif field[row][col] == 16:
                screen.blit(black_king, ((col+1)*box_size, row*box_size))
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
