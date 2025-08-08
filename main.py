# In your main.py file, replace all the existing code

import pygame
from chess_engine import draw_game_state, WIDTH, HEIGHT, GameState, load_images, SQ_SIZE, Move, DIMENSION
from data_handler import text_to_binary, binary_to_text

# Define the location of your input file
INPUT_FILE = "input_data.txt"

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Useless Chess Project")
    
    load_images() 
    
    gs = GameState()
    clock = pygame.time.Clock()
    MAX_FPS = 1 # We'll slow the game down so you can see the bots move
    
    running = True
    valid_moves = gs.get_all_legal_moves()
    move_made = False

    # --- NEW CODE STARTS HERE ---
    
    # 1. Get the binary stream from our input file
    binary_stream = text_to_binary(INPUT_FILE)
    if binary_stream is None:
        running = False # Exit if the file wasn't found
    
    bit_index = 0
    
    # --- NEW CODE ENDS HERE ---

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # --- NEW CODE STARTS HERE ---
        # 2. This is the bot's move logic
        if bit_index < len(binary_stream):
            bit = binary_stream[bit_index]
            
            # Simple bot logic:
            # - Move the first available pawn if the bit is '1'
            # - Move the first available rook if the bit is '0'
            move = None
            if bit == '1':
                for m in valid_moves:
                    if gs.board[m.start_row][m.start_col][1] == 'P':
                        move = m
                        break
            elif bit == '0':
                for m in valid_moves:
                    if gs.board[m.start_row][m.start_col][1] == 'R':
                        move = m
                        break
            
            if move is not None:
                gs.make_move(move)
                move_made = True
            
            bit_index += 1
            
        else:
            print("Encryption complete! No more binary data to process.")
            running = False # Stop the game when all data is processed
        
        # --- NEW CODE ENDS HERE ---

        if move_made:
            valid_moves = gs.get_all_legal_moves()
            move_made = False
            
        draw_game_state(screen, gs)
        pygame.display.flip()
        
        clock.tick(MAX_FPS) 

    pygame.quit()

if __name__ == "__main__":
    main()