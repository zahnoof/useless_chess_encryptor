# In your main.py file, replace the entire main() function

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
    MAX_FPS = 1
    
    running = True
    valid_moves = gs.get_all_legal_moves()
    move_made = False

    binary_stream = text_to_binary(INPUT_FILE)
    if binary_stream is None:
        running = False
    
    bit_index = 0
    final_board_binary = ""
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if bit_index < len(binary_stream):
            bit = binary_stream[bit_index]
            
            move = None
            found_move = False
            
            # --- NEW BOT LOGIC ---
            for m in valid_moves:
                is_white_square = ((m.end_row + m.end_col) % 2) == 0
                if (bit == '1' and is_white_square) or (bit == '0' and not is_white_square):
                    move = m
                    found_move = True
                    break
            
            # If no move to the correct color was found, take any other legal move
            if not found_move and valid_moves:
                move = valid_moves[0]
            # --- END NEW BOT LOGIC ---

            if move is not None:
                gs.make_move(move)
                move_made = True
            
            bit_index += 1
            
        else:
            print("Encryption complete! No more binary data to process.")
            running = False
            
        if move_made:
            valid_moves = gs.get_all_legal_moves()
            move_made = False
            
        draw_game_state(screen, gs)
        pygame.display.flip()
        

    # --- NEW DECRYPTION LOGIC STARTS HERE ---
    
    print("\n--- DECRYPTION PROCESS ---")
    decryption_binary_stream = ""
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            # Let's define white squares as '1' and black squares as '0'
            is_white_square = ((r + c) % 2) == 0
            if is_white_square:
                if gs.board[r][c] != "--":
                    decryption_binary_stream += '1'
            else:
                if gs.board[r][c] != "--":
                    decryption_binary_stream += '0'
    
    # Pad the binary stream to be a multiple of 8
    while len(decryption_binary_stream) % 8 != 0:
        decryption_binary_stream += '0'
    
    print("\n--- DECRYPTION PROCESS ---")
    decryption_binary_stream = gs.decryption_stream
    
    print("Reconstructed Binary Stream:", decryption_binary_stream)
    
    original_text = binary_to_text(decryption_binary_stream)
    print("Original Text:", original_text)

    pygame.quit()

if __name__ == "__main__":
    main()