# Import necessary modules
# sys: for system-specific parameters and functions
# copy: for creating deep copies of objects (so we don't modify the original)
import sys, copy

# Dictionary that stores the starting position of all chess pieces
# Keys are square positions (e.g., 'a8', 'e1')
# Values are piece codes: 'w' = white, 'b' = black, followed by piece type
# K=King, Q=Queen, R=Rook, B=Bishop, N=Knight, P=Pawn
STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

# Dictionary that maps piece codes to Unicode chess symbols for better visual display
# This makes the board look more like a real chessboard with proper piece symbols
PIECE_SYMBOLS = {
    'wK': '♔', 'wQ': '♕', 'wR': '♖', 'wB': '♗', 'wN': '♘', 'wP': '♙',  # White pieces
    'bK': '♚', 'bQ': '♛', 'bR': '♜', 'bB': '♝', 'bN': '♞', 'bP': '♟'   # Black pieces
}

def print_chessboard(board):
    """Print the chessboard with pieces.
    
    Args:
        board (dict): Dictionary representing the current state of the board
                      Keys are square positions (e.g., 'e4'), values are piece codes (e.g., 'wP')
    """
    # Print the header with file labels
    print("    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")
    
    # Loop through each rank (row) from top to bottom (8 to 1)
    for y in '87654321':
        # Start the row with the rank number
        row = f"{y} |"
        # f is used to format the string
        # y is the rank number
        # | is the separator between the rank number and the pieces
        # f"{y} |" is the same as "y |"
        # example of row for each iteration:
        # 8 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ |
        # 7 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ |
        # 6 |   |   |   |   |   |   |   |   |
        # 5 |   |   |   |   |   |   |   |   |
        # 4 |   |   |   |   |   |   |   |   |
        # 3 |   |   |   |   |   |   |   |   |
        # 2 |   |   |   |   |   |   |   |   |
        # Loop through each file (column) from left to right (a to h)
        for x in 'abcdefgh':
            # Combine file and rank to create the square position (e.g., 'e4')
            square = x + y
            
            # Check if there's a piece on this square
            if square in board:
                # Get the piece code (e.g., 'wP' for white pawn)
                piece = board[square]
                # Convert piece code to Unicode symbol for better display
                # If the piece code isn't in our symbols dictionary, use the code itself
                display_piece = PIECE_SYMBOLS.get(piece, piece)
                row += f" {display_piece} |"
            else:
                # No piece on this square, so display an empty square
                row += "   |"
        
        # Print the completed row
        print(row)
        
        # Print the border line (except after the last row)
        if y != '1':
            print("  +---+---+---+---+---+---+---+---+")
    
    # Print the bottom border
    print("  +---+---+---+---+---+---+---+---+")

def is_valid_square(square):
    """Check if a square is valid on the chessboard.
    
    Args:
        square (str): Square position to validate (e.g., 'e4')
    
    Returns:
        bool: True if the square is valid, False otherwise
    """
    # A valid square must be exactly 2 characters long (file + rank)
    if len(square) != 2:
        return False
    
    # Extract the file (column) and rank (row) from the square
    file, rank = square[0], square[1]
    
    # Check if file is a-h and rank is 1-8
    # This ensures the square is within the chessboard boundaries
    return file in 'abcdefgh' and rank in '12345678'

def get_piece_color(piece):
    """Get the color of a piece (w for white, b for black).
    
    Args:
        piece (str): Piece code (e.g., 'wP', 'bK')
    
    Returns:
        str or None: 'w' for white, 'b' for black, None if piece is invalid
    """
    # The first character of a piece code indicates its color
    # 'w' = white, 'b' = black
    return piece[0] if piece else None

def is_valid_move(board, from_square, to_square, current_player):
    """Check if a move is valid for the current player.
    
    Args:
        board (dict): Current state of the board
        from_square (str): Starting square position
        to_square (str): Destination square position
        current_player (str): 'w' for white, 'b' for black
    
    Returns:
        bool: True if the move is valid, False otherwise
    """
    # First, check if both squares are valid positions on the board
    if not is_valid_square(from_square) or not is_valid_square(to_square):
        return False
    
    # Check if there's actually a piece on the starting square
    if from_square not in board:
        return False
    
    # Get the piece that's being moved
    piece = board[from_square]
    # Get the color of that piece
    piece_color = get_piece_color(piece)
    
    # Check if the piece belongs to the current player
    # Players can only move their own pieces
    if piece_color != current_player:
        return False
    
    # Check if the destination square has a piece of the same color
    # Players cannot capture their own pieces
    if to_square in board and get_piece_color(board[to_square]) == current_player:
        return False
    
    # Basic move validation (simplified - doesn't check for check/checkmate)
    # In a real chess game, you'd also check if the move puts your own king in check
    return True

def make_move(board, from_square, to_square):
    """Make a move on the board.
    
    Args:
        board (dict): Current state of the board
        from_square (str): Starting square position
        to_square (str): Destination square position
    
    Returns:
        bool: True if the move was successful, False otherwise
    """
    # Check if there's a piece on the starting square
    if from_square in board:
        # Move the piece from the starting square to the destination square
        board[to_square] = board[from_square]
        # Remove the piece from the starting square
        del board[from_square]
        return True
    return False

def get_player_move(board, current_player):
    """Get a valid move from the current player.
    
    Args:
        board (dict): Current state of the board
        current_player (str): 'w' for white, 'b' for black
    
    Returns:
        tuple or None: (from_square, to_square) if valid move, None if player quits
    """
    # Keep asking for input until we get a valid move
    while True:
        try:
            # Tell the player whose turn it is
            print(f"\n{current_player.upper()} player's turn")
            # Get input from the player
            move = input("Enter move (e.g., 'e2 e4' or 'quit' to exit): ").strip().lower()
            
            # Allow the player to quit the game
            if move == 'quit':
                return None
            
            # Check if the input has the correct format (two squares separated by space)
            if ' ' not in move:
                print("Invalid format. Use 'from_square to_square' (e.g., 'e2 e4')")
                continue
            
            # Split the input into starting and destination squares
            from_square, to_square = move.split()
            
            # Validate the move
            if is_valid_move(board, from_square, to_square, current_player):
                return from_square, to_square
            else:
                print("Invalid move. Try again.")
                
        except (ValueError, IndexError):
            # Handle any errors in input processing
            print("Invalid input. Use format 'e2 e4'")

def main():
    """Main game loop - this is where the chess game runs."""
    # Welcome message and instructions
    print("Welcome to Terminal Chess!")
    print("White pieces: ♔♕♖♗♘♙")
    print("Black pieces: ♚♛♜♝♞♟")
    print("Enter moves as 'from_square to_square' (e.g., 'e2 e4')")
    print("Type 'quit' to exit the game\n")
    
    # Create a copy of the starting board so we don't modify the original
    board = copy.deepcopy(STARTING_PIECES)
    
    # White always goes first in chess
    current_player = 'w'
    
    # Main game loop - continues until the game ends
    while True:
        # Display the current state of the board
        print_chessboard(board)
        
        # Get the current player's move
        move = get_player_move(board, current_player)
        
        # If the player chose to quit, end the game
        if move is None:
            print("Game ended.")
            break
        
        # Unpack the move into starting and destination squares
        from_square, to_square = move
        
        # Attempt to make the move
        if make_move(board, from_square, to_square):
            # Move was successful
            print(f"Moved {board[to_square]} from {from_square} to {to_square}")
            
            # Switch to the other player's turn
            # If current player is 'w' (white), switch to 'b' (black), and vice versa
            current_player = 'b' if current_player == 'w' else 'w'
        else:
            # Move failed for some reason
            print("Invalid move. Try again.")

# This is a special Python construct that ensures the main() function only runs
# if this script is executed directly (not if it's imported as a module)
if __name__ == "__main__":
    main()




