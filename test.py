# imports
import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import stdio
import stdarray
import stddraw
# Your imports go here

# global variables

# Your global variables go here


def draw_qr_grid(qr_grid):
    """
    Draws the given qr data onto the canvas of stddraw in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass

def print_qr_grid(qr_grid):
    """
    Prints the given qr data out to the standard output in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass

def make_position_pattern(pos_square_size):
    # Base Case
    if pos_square_size == 4:
        # Hardcode pattern for 4x4 to implement into larger sizes
        return[
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0]
        ]
    inner = make_position_pattern(pos_square_size - 2) # Recursive call to create inner pattern

    # Creating an empty size x size 2D array
    grid = stdarray.create2D(pos_square_size, pos_square_size, 0)

    for i in range(pos_square_size - 2): # Fill the inner pattern into the grid
        for j in range(pos_square_size - 2):
            grid[i + 1][j + 1] = inner[i][j] # Offset the inner pattern by 1

    if (pos_square_size // 2) % 2 == 0: # Ring refers to the outer ring of the hardcoded grid, checks if size is even
        ring = 1
    else: 
        ring = 0

    alt = 1 - ring

    # 1) Fill the top row from column 0 to column pos_square_size-1 with ring.
    for i in range(pos_square_size - 1):
        grid[0][i] = ring
    grid[0][pos_square_size - 1] = alt

    # 2) Fill the bottom row from column 0 to column pos_square_size
    for i in range(pos_square_size):
        grid[pos_square_size - 1][i] = alt
    
    # 3) Fill the left column from row=1 to row=(pos_square_size-1) with ring.
    for j in range(1, pos_square_size - 1):
        grid[j][0] = ring
    
    # 4) Fill the right column from row=1 to row=pos_square_size with alternating ring pattern.
    for j in range(1, pos_square_size):
        grid[j][pos_square_size - 1] = alt

    return grid
    # TODO: implement this function.

def make_alignment_pattern(align_square_size):
    # Base Case
    if align_square_size == 1:
        return [[1]] # Hard code 1x1 alignment pattern to center 1
    
    inner = make_alignment_pattern(align_square_size - 4) # Recursive call to create inner pattern
    grid2 = stdarray.create2D(align_square_size, align_square_size, 0) # Create a 2D array of size align_square_size x align_square_size

    # Fill the outer ring with 1
    for i in range(align_square_size):
        grid2[0][i] = 1
    for i in range(align_square_size): 
        grid2[align_square_size - 1][i] = 1
    for j in range(align_square_size): 
        grid2[j][0] = 1 
    for j in range(align_square_size):
        grid2[j][align_square_size - 1] = 1

    # Place the inner pattern in the middle, offset by (2,2)
    for j in range(align_square_size - 4):
        for i in range(align_square_size - 4):
            grid2[i + 2][j + 2] = inner[i][j]
    return grid2

def rotate90_pattern_clockwise(data):
    pos_square_size = len(data) # Get the size of the data
    rotated = stdarray.create2D(pos_square_size, pos_square_size, 0) # Create a 2D array of size pos_square_size x pos_square_size
    # Rotate the data 90 degrees clockwise
    for i in range(pos_square_size): 
        for j in range(pos_square_size): 
            rotated[i][j] = data[pos_square_size - 1 - j][i] # The new position of the data is rotated 90 degrees clockwise
    return rotated

def rotate180_pattern_clockwise(data): # Rotate the data 180 degrees clockwise
    pos_square_size = len(data)
    rotated = stdarray.create2D(pos_square_size, pos_square_size, 0)
    for i in range(pos_square_size):
        for j in range(pos_square_size):
            rotated[i][j] = data[pos_square_size - 1 - i][pos_square_size - 1 - j]
    return rotated

def add_data_at_anchor(qr_grid, anchor_x, anchor_y, data):
    rows = len(data)
    cols = len(data[0])
    for i in range(rows):
        for j in range(cols):
            # Place the data if it's non-zero (or always, if you like)
            if data[i][j] != 0:
                qr_grid[anchor_x + i][anchor_y + j] = data[i][j]
    """
    Places values contained in data to the qr_grid starting as positions given
    by achnor_x and anchor_y.

    Args:
        qr_grid (2D array of int): The QR grid
        anchor_x (int): the x position from where the data should be added
        anchor_y (int): the y position from where the data should be added
        data (2D array of int): The data that should be added to the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_snake(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the snake layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_real(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the real layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def apply_mask(qr_grid, reserved_positions, mask_id):
    """
    Applies the masking pattern specified by mask_id to the QR grid following
    the masking rules as specified by the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        reserved_positions (2D array of int): the reserved positions
        mask_id (str): The mask id to apply to the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass

def encode_real(size, message, information_bits, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    real layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        information_bits (array of int): the 15-bit information pattern
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def encode_snake(size, message, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    snake layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def main(args):
    if len(sys.argv) != 3:
        stdio.writeln("Usage: python3 script.py <pos_square_size> <align_square_size>")
        sys.exit(1)

    # 1) Parse input
    pos_square_size = int(sys.argv[1])
    align_square_size = int(sys.argv[2])

    # 2) Define a size that can fit all patterns
    size = max(21, pos_square_size * 2 + align_square_size + 4)

    # 3) Create an empty QR grid
    qr_grid = stdarray.create2D(size, size, 0)

    # 4) Generate patterns (assumes you already have these functions)
    pos_pattern = make_position_pattern(pos_square_size)
    align_pattern = make_alignment_pattern(align_square_size)

    # 5) Add position patterns using your add_data_at_anchor()
    add_data_at_anchor(qr_grid, 0, 0, pos_pattern)
    add_data_at_anchor(
        qr_grid, 
        0, 
        size - pos_square_size, 
        rotate90_pattern_clockwise(pos_pattern)
    )
    add_data_at_anchor(
        qr_grid, 
        size - pos_square_size, 
        0, 
        rotate180_pattern_clockwise(pos_pattern)
    )

    # 6) Add alignment pattern (bottom-right corner example)
    ax = size - align_square_size - 2
    ay = size - align_square_size - 2
    add_data_at_anchor(qr_grid, ax, ay, align_pattern)

    # 7) Output the final 2D array
    for row in qr_grid:
        stdio.writeln(" ".join(map(str, row)))

    sys.exit(0)

if __name__ == "__main__":
    """USage: echo 'message' | python3 SUXXXXXXXX.py 'encoding_string' 'size' 'pos_size' 'align_size'"""
    main(sys.argv)# imports
import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import stdio
import stdarray
import stddraw
# Your imports go here

# global variables

# Your global variables go here


def draw_qr_grid(qr_grid):
    """
    Draws the given qr data onto the canvas of stddraw in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass

def print_qr_grid(qr_grid):
    """
    Prints the given qr data out to the standard output in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass

def make_position_pattern(pos_square_size):
    # Base Case
    if pos_square_size == 4:
        # Hardcode pattern for 4x4 to implement into larger sizes
        return[
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0]
        ]
    inner = make_position_pattern(pos_square_size - 2) # Recursive call to create inner pattern

    # Creating an empty size x size 2D array
    grid = stdarray.create2D(pos_square_size, pos_square_size, 0)

    for i in range(pos_square_size - 2): # Fill the inner pattern into the grid
        for j in range(pos_square_size - 2):
            grid[i + 1][j + 1] = inner[i][j] # Offset the inner pattern by 1

    if (pos_square_size // 2) % 2 == 0: # Ring refers to the outer ring of the hardcoded grid, checks if size is even
        ring = 1
    else: 
        ring = 0

    alt = 1 - ring

    # 1) Fill the top row from column 0 to column pos_square_size-1 with ring.
    for i in range(pos_square_size - 1):
        grid[0][i] = ring
    grid[0][pos_square_size - 1] = alt

    # 2) Fill the bottom row from column 0 to column pos_square_size
    for i in range(pos_square_size):
        grid[pos_square_size - 1][i] = alt
    
    # 3) Fill the left column from row=1 to row=(pos_square_size-1) with ring.
    for j in range(1, pos_square_size - 1):
        grid[j][0] = ring
    
    # 4) Fill the right column from row=1 to row=pos_square_size with alternating ring pattern.
    for j in range(1, pos_square_size):
        grid[j][pos_square_size - 1] = alt

    return grid
    # TODO: implement this function.

def make_alignment_pattern(align_square_size):
    # Base Case
    if align_square_size == 1:
        return [[1]] # Hard code 1x1 alignment pattern to center 1
    
    inner = make_alignment_pattern(align_square_size - 4) # Recursive call to create inner pattern
    grid2 = stdarray.create2D(align_square_size, align_square_size, 0) # Create a 2D array of size align_square_size x align_square_size

    # Fill the outer ring with 1
    for i in range(align_square_size):
        grid2[0][i] = 1
    for i in range(align_square_size): 
        grid2[align_square_size - 1][i] = 1
    for j in range(align_square_size): 
        grid2[j][0] = 1 
    for j in range(align_square_size):
        grid2[j][align_square_size - 1] = 1

    # Place the inner pattern in the middle, offset by (2,2)
    for j in range(align_square_size - 4):
        for i in range(align_square_size - 4):
            grid2[i + 2][j + 2] = inner[i][j]
    return grid2

def rotate90_pattern_clockwise(data):
    pos_square_size = len(data) # Get the size of the data
    rotated = stdarray.create2D(pos_square_size, pos_square_size, 0) # Create a 2D array of size pos_square_size x pos_square_size
    # Rotate the data 90 degrees clockwise
    for i in range(pos_square_size): 
        for j in range(pos_square_size): 
            rotated[i][j] = data[pos_square_size - 1 - j][i] # The new position of the data is rotated 90 degrees clockwise
    return rotated

def rotate180_pattern_clockwise(data): # Rotate the data 180 degrees clockwise
    pos_square_size = len(data)
    rotated = stdarray.create2D(pos_square_size, pos_square_size, 0)
    for i in range(pos_square_size):
        for j in range(pos_square_size):
            rotated[i][j] = data[pos_square_size - 1 - i][pos_square_size - 1 - j]
    return rotated

def add_data_at_anchor(qr_grid, anchor_x, anchor_y, data):
    rows = len(data)
    cols = len(data[0])
    for i in range (rows):
        for j in range (cols):
            qr_grid[anchor_y + i][anchor_x + j] = data[i][j]
    return qr_grid


def add_data_snake(qr_grid, reserved_positions, data):
    size = len(qr_grid)
    bit_index = 0
    # Snake pattern typically starts from the rightmost column going upward,
    # then stepping left, going downward, etc. Check your specification for 
    # the exact route. Below is just a schematic approach.

    # Example: We iterate column by column from right to left:
    for col in range(size-1, -1, -1):  # from size-1 down to 0
        if (col % 2) == (size % 2):
            # move from top row to bottom row
            row_iter = range(size)
        else:
            # move from bottom row to top row
            row_iter = range(size-1, -1, -1)

        for row in row_iter:
            # If not reserved, place next bit
            if reserved_positions[row][col] == 0:
                if bit_index < len(data):
                    qr_grid[row][col] = data[bit_index]
                    bit_index += 1
                else:
                    qr_grid[row][col] = 0  # or pad with 0 if out of bits

    # If you have leftover bits or run out of bits early, follow your spec’s instructions 
    # (e.g., pad with 0, or ignore them, etc.).
    """
    Places values contained in data to the qr_grid in the snake layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_real(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the real layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def apply_mask(qr_grid, reserved_positions, mask_id):

    size = len(qr_grid)
    # For a mask 'fn(x, y)', if the condition is True, flip (xor) the cell.
    # Example mask conditions (as typically defined for QR):
    #   mask 000: (row + col) mod 2 == 0
    #   mask 001: row mod 2 == 0
    #   mask 010: col mod 3 == 0
    # or as per your project specification. 
    # The snippet below is an example only:

    for r in range(size):
        for c in range(size):
            if reserved_positions[r][c] == 1:
                continue  # never mask reserved cells
            flip = False
            if mask_id == "000":
                # Example: flip if (r + c) % 2 == 0
                flip = ((r + c) % 2 == 0)
            elif mask_id == "001":
                # Example: flip if (r % 2) == 0
                flip = ((r % 2) == 0)
            elif mask_id == "010":
                # Example: flip if (c % 3) == 0
                flip = ((c % 3) == 0)
            else:
                # By spec, if mask is not in {000, 001, 010}, produce error
                stdio.writeln("Error: Unsupported mask id for Hand-in 2.")
                sys.exit(1)

            if flip:
                qr_grid[r][c] = 1 - qr_grid[r][c]  # XOR flip


def encode_real(size, message, information_bits, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    real layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        information_bits (array of int): the 15-bit information pattern
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def encode_snake(size, message, pos_square_size, align_square_size, mask_id):
    """
    Generates the QR code according to the project specifications using the
    snake layout, placing:
      - three position patterns 
      - one alignment pattern
      - the data bits in a snake pattern
      - applying the mask
    Skips format info, timing strips, dark cell, ECC, etc.
    """
    # Create the 2D grid
    qr_grid = stdarray.create2D(size, size, 0)
    # We need an array to mark reserved vs. data cells
    reserved_positions = stdarray.create2D(size, size, 0)

    # 1) Place the three position patterns
    pos_pattern = make_position_pattern(pos_square_size)
    # top-left
    add_data_at_anchor(qr_grid, reserved_positions, 0, 0, pos_pattern)
    # top-right (rotated 90 deg?), or possibly just anchor at [size - pos_square_size, 0]
    #   according to your spec’s instructions. For example:
    pos_pattern_NE = rotate90_pattern_clockwise(pos_pattern)
    add_data_at_anchor(qr_grid, reserved_positions,
                            size - pos_square_size, 0, pos_pattern_NE)
    # bottom-left (rotated 180 deg?), or anchor at [0, size - pos_square_size]
    pos_pattern_SW = rotate180_pattern_clockwise(pos_pattern)
    add_data_at_anchor(qr_grid, reserved_positions,
                            0, size - pos_square_size, pos_pattern_SW)

    # 2) Place the alignment pattern somewhere in the interior. 
    #    The anchor for the alignment pattern depends on your specification.
    align_pattern = make_alignment_pattern(align_square_size)
    # Suppose the alignment is anchored near the bottom-right corner. 
    # Example anchor:
    align_x = size - align_square_size - 2  # or wherever your spec says
    align_y = size - align_square_size - 2
    add_data_at_anchor(qr_grid, reserved_positions, align_x, align_y, align_pattern)

    # 3) Insert the data bits in a snake layout
    add_data_snake(qr_grid, reserved_positions, message)

    # 4) Apply the chosen mask
    apply_mask(qr_grid, reserved_positions, mask_id)

    return qr_grid

def main(args):
      # We expect 5 arguments total:
    #   1) encoding_parameter ("SNK" or "REAL" or other)
    #   2) size (integer)
    #   3) pos_square_size (integer)
    #   4) align_square_size (integer)
    #   5) mask_id (e.g., "000", "001", "010")
    if len(sys.argv) != 6:
        stdio.writeln("Usage: python3 SU28941675.py <encoding_parameter> <size> "
                      "<pos_square_size> <align_square_size> <mask_id>")
        sys.exit(1)

    encoding_parameter = sys.argv[1]
    size_str = sys.argv[2]
    pos_str = sys.argv[3]
    align_str = sys.argv[4]
    mask_id = sys.argv[5]

    # Convert the numeric arguments
    try:
        size = int(size_str)
        pos_size = int(pos_str)
        align_size = int(align_str)
    except ValueError:
        stdio.writeln("Error: <size>, <pos_square_size>, and <align_square_size> must be integers.")
        sys.exit(1)

    # Terminate immediately if encoding_parameter indicates the "real layout"
    # for Hand-in 3:
    if encoding_parameter.upper() == "REAL":
        # No output, just terminate
        sys.exit(0)

    # Otherwise, check that encoding_parameter is the "snake" layout
    # (or some recognized label from your instructions).
    # If it is not recognized, terminate with an error.
    valid_snake_labels = ["SNK", "SNAKE"]  # or whichever codes you use
    if encoding_parameter.upper() not in valid_snake_labels:
        stdio.writeln("Error: Invalid encoding_parameter for Hand-in 2. Must be SNK (or REAL).")
        sys.exit(1)

    # Validate pos_size, align_size, etc., based on your project specs
    if pos_size < 4 or (pos_size % 2) != 0:
        stdio.writeln("Error: pos_square_size must be an even integer >= 4.")
        sys.exit(1)
    if align_size < 1 or ((align_size - 1) % 4 != 0):
        stdio.writeln("Error: align_square_size must be 1,5,9,13,...")
        sys.exit(1)
    if size < (pos_size * 2):  # or any other check for reasonableness
        stdio.writeln("Error: <size> seems too small for the position patterns.")
        sys.exit(1)

    # --------------------------------
    # Read the message from stdin
    # --------------------------------
    raw_message = sys.stdin.read().rstrip("\n")
    # Convert this raw_message to bits (per your specification).
    # For example:
    message_bits = []
    for ch in raw_message:
        # Example simplistic approach: just take ASCII code & store 8 bits each
        val = ord(ch)
        for i in range(8):
            # Extract bits from most-significant to least-significant
            bit = (val >> (7 - i)) & 1
            message_bits.append(bit)

    # --------------------------------
    # Build the QR code using the "snake" layout
    # --------------------------------
    qr_grid = encode_snake(size, message_bits, pos_size, align_size, mask_id)

    # --------------------------------
    # Print out the resulting QR grid 
    # or draw it, depending on your spec
    # --------------------------------
    # For instance, print to stdout:
    for row in qr_grid:
        line = "".join(str(cell) for cell in row)
        stdio.writeln(line)

if __name__ == "__main__":
    """USage: echo 'message' | python3 test.py 'encoding_string' 'size' 'pos_size' 'align_size'"""
    main(sys.argv)