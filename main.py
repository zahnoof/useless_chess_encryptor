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
    MAX_FPS = 5
    
    running = True
    valid_moves = []
    move_made = False

    binary_stream = ""
    bit_index = 0
    final_decryption_stream = ""
    
    pygame.font.init()
    font_small = pygame.font.SysFont('Arial', 24)
    font_large = pygame.font.SysFont('Arial', 48)

    current_state = "START_SCREEN"
    input_box = pygame.Rect(0, 0, 230, 32)
    input_text = ""
    is_active = True
    color_passive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_active
    start_button = pygame.Rect(0, 0, 100, 40)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if current_state == "START_SCREEN":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        is_active = not is_active
                    else:
                        is_active = False
                    color = color_active if is_active else color_passive
                    
                    if start_button.collidepoint(event.pos):
                        binary_stream = text_to_binary(input_text, is_file=False)
                        if binary_stream:
                            bit_index = 0
                            gs = GameState()
                            final_decryption_stream = ""
                            valid_moves = gs.get_all_legal_moves()
                            current_state = "GAME_RUNNING"
                            print("New encryption started.")
                        else:
                            print("Input text is empty or invalid. Please try again.")

                if event.type == pygame.KEYDOWN:
                    if is_active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode
            
            elif current_state == "GAME_RUNNING":
                pass

        if current_state == "START_SCREEN":
            # --- START SCREEN DRAWING LOGIC ---
            screen.fill(pygame.Color(50, 50, 50))

            title_text = font_large.render("Useless Chess Encryptor", True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title_text, title_rect)

            input_box.center = (WIDTH // 2, 200)
            pygame.draw.rect(screen, color, input_box, 2)
            text_surface = font_small.render(input_text, True, (255, 255, 255))
            screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
            input_box.w = max(230, text_surface.get_width() + 10)

            start_button.center = (WIDTH // 2, 250)
            pygame.draw.rect(screen, (0, 200, 0), start_button)
            start_text = font_small.render("Start", True, (255, 255, 255))
            start_text_rect = start_text.get_rect(center=start_button.center)
            screen.blit(start_text, start_text_rect)

            pygame.display.flip()

        elif current_state == "GAME_RUNNING":
            if gs.game_over:
                final_decryption_stream += gs.decryption_stream
                gs = GameState()
                valid_moves = gs.get_all_legal_moves()
                print("Checkmate! Starting a new game from the last bit.")

            if bit_index < len(binary_stream):
                bit = binary_stream[bit_index]
                move = None
                found_move = False
                for m in valid_moves:
                    is_white_square = ((m.end_row + m.end_col) % 2) == 0
                    if (bit == '1' and is_white_square) or (bit == '0' and not is_white_square):
                        move = m
                        found_move = True
                        break
                if not found_move and valid_moves:
                    move = valid_moves[0]
                if move is not None:
                    gs.make_move(move)
                    final_decryption_stream += gs.decryption_stream[-1]
                    move_made = True
                bit_index += 1
            else:
                print("Encryption complete! No more binary data to process.")
                running = False
            if move_made:
                valid_moves = gs.get_all_legal_moves()
                move_made = False
            
            screen.fill(pygame.Color("white"))
            draw_game_state(screen, gs)
            
            pygame.draw.rect(screen, (240, 240, 240), pygame.Rect(512, 0, 256, 512))
            
            moves_remaining = len(binary_stream) - bit_index
            moves_remaining_text = font_small.render(f"Moves Remaining: {moves_remaining}", True, (0, 0, 0))
            screen.blit(moves_remaining_text, (522, 10))

            pygame.display.flip()
            
            clock.tick(MAX_FPS)

    print("\n--- DECRYPTION PROCESS ---")
    decryption_binary_stream = final_decryption_stream
    decryption_binary_stream = decryption_binary_stream[:len(binary_stream)]
    print("Reconstructed Binary Stream:", decryption_binary_stream)
    
    original_text = binary_to_text(decryption_binary_stream)
    print("Original Text:", original_text)

    pygame.quit()

if __name__ == "__main__":
    main()