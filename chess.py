import pygame
pygame.init()

fps = 60
clock = pygame.time.Clock()

box_size = 80
size = (9 * box_size, 9 * box_size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")

chosen_piece = 0
chosen_col = -1
chosen_row = -1
offset = 0
white_king_moved = False
black_king_moved = False
white_left_rook_moved = False
white_right_rook_moved = False
black_left_rook_moved = False
black_right_rook_moved = False

sprites = pygame.image.load("sprites_classical.png")
white_pawn = sprites.subsurface(1000, 0, 200, 200)
white_pawn = pygame.transform.scale(white_pawn, (box_size, box_size))
white_bishop = sprites.subsurface(400, 0, 200, 200)
white_bishop = pygame.transform.scale(white_bishop, (box_size, box_size))
white_knight = sprites.subsurface(600, 0, 200, 200)
white_knight = pygame.transform.scale(white_knight, (box_size, box_size))
white_rook = sprites.subsurface(800, 0, 200, 200)
white_rook = pygame.transform.scale(white_rook, (box_size, box_size))
white_queen = sprites.subsurface(200, 0, 200, 200)
white_queen = pygame.transform.scale(white_queen, (box_size, box_size)) 
white_king = sprites.subsurface(0, 0, 200, 200)
white_king = pygame.transform.scale(white_king, (box_size, box_size))
black_pawn = sprites.subsurface(1000, 200, 200, 200)
black_pawn = pygame.transform.scale(black_pawn, (box_size, box_size))
black_bishop = sprites.subsurface(400, 200, 200, 200)
black_bishop = pygame.transform.scale(black_bishop, (box_size, box_size))
black_knight = sprites.subsurface(600, 200, 200, 200)
black_knight = pygame.transform.scale(black_knight, (box_size, box_size))
black_rook = sprites.subsurface(800, 200, 200, 200)
black_rook = pygame.transform.scale(black_rook, (box_size, box_size))
black_queen = sprites.subsurface(200, 200, 200, 200)
black_queen = pygame.transform.scale(black_queen, (box_size, box_size)) 
black_king = sprites.subsurface(0, 200, 200, 200)
black_king = pygame.transform.scale(black_king, (box_size, box_size))

field=[[14,13,12,15,16,12,13,14], 
       [11,11,11,11,11,11,11,11],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 0, 0, 0, 0, 0, 0, 0],
       [ 1, 1, 1, 1, 1, 1, 1, 1],
       [ 4, 3, 2, 5, 6, 2, 3, 4]]

def draw_piece(piece, x, y):
    if piece == 1:
        screen.blit(white_pawn, (x, y))
    elif piece == 2:
        screen.blit(white_bishop, (x, y))
    elif piece == 3:
        screen.blit(white_knight, (x, y))
    elif piece == 4:
        screen.blit(white_rook, (x, y))
    elif piece == 5:
        screen.blit(white_queen, (x, y))
    elif piece == 6:
        screen.blit(white_king, (x, y))
    elif piece == 11:
        screen.blit(black_pawn, (x, y))
    elif piece == 12:
        screen.blit(black_bishop, (x, y))
    elif piece == 13:
        screen.blit(black_knight, (x, y))
    elif piece == 14:
        screen.blit(black_rook, (x, y))
    elif piece == 15:
        screen.blit(black_queen, (x, y))
    elif piece == 16:
        screen.blit(black_king, (x, y))

def is_valid_move(row, col):
    global white_king_moved, black_king_moved, \
        white_left_rook_moved, white_right_rook_moved, \
        black_left_rook_moved, black_right_rook_moved
    if chosen_piece in [1, 11]:  # Pawn
        direction = -1 if chosen_piece == 1 else 1
        if chosen_row + direction == row: 
            if field[row][col] != 0 and abs(chosen_col - col) == 1:
                return True
            if field[row][col] == 0 and col == chosen_col:
                return True
        if (chosen_row == 6 and chosen_piece == 1) \
            or (chosen_row == 1 and chosen_piece == 11):
            if (chosen_row + 2*direction == row) and col == chosen_col \
                and field[row][col] == 0 and field[chosen_row + direction][col] == 0: 
                 return True
        return False
    if chosen_piece in [2, 12]:
        if abs(chosen_row - row) == abs(chosen_col - col):  # Bishop
            dir_row = 1 if row > chosen_row else -1
            dir_col = 1 if col > chosen_col else -1
            for i in range(1, abs(chosen_row - row)):
                if field[chosen_row + i*dir_row][chosen_col + i*dir_col] != 0:
                    return False
            return True
    if chosen_piece in [3, 13]:  # Knight
        if (abs(chosen_row - row) == 2 and abs(chosen_col - col) == 1) or \
           (abs(chosen_row - row) == 1 and abs(chosen_col - col) == 2):
            return True
    if chosen_piece in [4, 14]:  # Rook
        if chosen_row == row:
            dir_col = 1 if col > chosen_col else -1
            for i in range(1, abs(chosen_col - col)):
                if field[chosen_row][chosen_col + i*dir_col] != 0:
                    return False
            return True
        if chosen_col == col:
            dir_row = 1 if row > chosen_row else -1
            for i in range(1, abs(chosen_row - row)):
                if field[chosen_row + i*dir_row][chosen_col] != 0:
                    return False
            return True
    if chosen_piece in [5, 15]:  # Queen
        if abs(chosen_row - row) == abs(chosen_col - col):  # Diagonal
            dir_row = 1 if row > chosen_row else -1
            dir_col = 1 if col > chosen_col else -1
            for i in range(1, abs(chosen_row - row)):
                if field[chosen_row + i*dir_row][chosen_col + i*dir_col] != 0:
                    return False
            return True
        if chosen_row == row:  # Horizontal
            dir_col = 1 if col > chosen_col else -1
            for i in range(1, abs(chosen_col - col)):
                if field[chosen_row][chosen_col + i*dir_col] != 0:
                    return False
            return True
        if chosen_col == col:  # Vertical
            dir_row = 1 if row > chosen_row else -1
            for i in range(1, abs(chosen_row - row)):
                if field[chosen_row + i*dir_row][chosen_col] != 0:
                    return False
            return True
    if chosen_piece in [6, 16]:  # King
        if abs(chosen_row - row) <= 1 and abs(chosen_col - col) <= 1:
            return True
        if abs(chosen_col - col) == 2 and chosen_row == row:
            if chosen_piece == 6 and not white_king_moved:
                if col == 6 and not white_right_rook_moved and\
                        field[chosen_row][5] == 0 and field[chosen_row][6] == 0:
                    return True
                if col == 2 and not white_left_rook_moved and\
                        field[chosen_row][1] == 0 and field[chosen_row][2] == 0 \
                        and field[chosen_row][3] == 0:
                    return True
            if chosen_piece == 16 and not black_king_moved:
                if col == 6 and not black_right_rook_moved and \
                    field[chosen_row][5] == 0 and field[chosen_row][6] == 0:
                    return True
                if col == 2 and not black_left_rook_moved and \
                    field[chosen_row][1] == 0 and field[chosen_row][2] == 0 \
                        and field[chosen_row][3] == 0:
                    return True 
    return False

        #start_row = 6 if chosen_piece == 1 else 1
        #if (chosen_row + direction == new_row and field[new_row][new_col] == 0) or \
        #   (chosen_row == start_row and chosen_row + 2*direction == new_row \
        #    and field[new_row][new_col] == 0 and field[chosen_row + direction][new_col] == 0) \
        #        or

def allowed_cell():
    x, y = pygame.mouse.get_pos()
    col = x // box_size - 1
    row = y // box_size
    if 0 <= row < 8 and 0 <= col < 8:
        counter_offset = 10 if offset == 0 else 0
        if field[row][col] == 0 or \
            (1 + counter_offset <= field[row][col] <= 6 + counter_offset):
            if row != chosen_row or col != chosen_col:
                if is_valid_move(row, col):
                    return True, row, col
    return False, -1, -1


def handle_castling(piece, old_row, old_col, new_row, new_col):
    """Move the rook when castling occurs"""
    # White King castling
    if piece == 6 and old_row == 7:
        if new_col == 6:  # King-side castling (right)
            field[7][5] = field[7][7]  # Move rook from h1 to f1
            field[7][7] = 0
        elif new_col == 2:  # Queen-side castling (left)
            field[7][3] = field[7][0]  # Move rook from a1 to d1
            field[7][0] = 0
    # Black King castling
    elif piece == 16 and old_row == 0:
        if new_col == 6:  # King-side castling (right)
            field[0][5] = field[0][7]  # Move rook from h8 to f8
            field[0][7] = 0
        elif new_col == 2:  # Queen-side castling (left)
            field[0][3] = field[0][0]  # Move rook from a8 to d8
            field[0][0] = 0

def highlight_cell():
    allowed, row, col = allowed_cell()
    if allowed:
        pygame.draw.rect(screen, (255, 255, 0), 
                             ((col+1)*box_size, row*box_size, box_size, box_size), 3)
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
            pygame.draw.rect(screen, (255, 255, 255), 
                             ((col+1)*box_size, row*box_size, box_size, box_size), 2)
            draw_piece(field[row][col], (col+1)*box_size, row*box_size)
    if chosen_piece != 0:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        highlight_cell()
        draw_piece(chosen_piece, mouse_x - box_size // 2, mouse_y - box_size // 2)

def handle_movement_flags(piece, old_row, old_col):
    """Update movement tracking flags for castling rights"""
    global white_king_moved, black_king_moved, \
        white_left_rook_moved, white_right_rook_moved, \
        black_left_rook_moved, black_right_rook_moved
    if piece == 6:  # White King
        white_king_moved = True
    elif piece == 16:  # Black King        
        black_king_moved = True
    elif piece == 4 and old_row == 7:  # White Rook         
        if old_col == 0:
            white_left_rook_moved = True
        elif old_col == 7:
            white_right_rook_moved = True
    elif piece == 14 and old_row == 0:  # Black Rook
        if old_col == 0:
            black_left_rook_moved = True
        elif old_col == 7:
            black_right_rook_moved = True

running = True
while running:
    screen.fill("black")
    piece = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            chosen_col = mouse_x // box_size - 1
            chosen_row = mouse_y // box_size
            chosen_piece = 0
            if 0 <= chosen_row < 8 and 0 <= chosen_col < 8:
                if 1 + offset <= field[chosen_row][chosen_col] <= 6 + offset:
                    chosen_piece = field[chosen_row][chosen_col]
                    field[chosen_row][chosen_col] = 0
        if event.type == pygame.MOUSEBUTTONUP:
            if chosen_piece != 0:
                allowed, new_row, new_col = allowed_cell()
                if allowed:
                    # Handle castling - move rook if needed
                    handle_castling(chosen_piece, chosen_row, chosen_col, new_row, new_col)
                    
                    # Update movement tracking flags when move is completed
                    handle_movement_flags(chosen_piece, chosen_row, chosen_col)
                    
                    offset = 10 if offset == 0 else 0
                    chosen_row, chosen_col = new_row, new_col
                field[chosen_row][chosen_col] = chosen_piece
                chosen_piece = 0
    
    draw_field()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
