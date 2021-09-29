Class EI:
    """

     This file is the core of the El-Tetris algorithm.

     Features that are used by the algorithm are implemented here.
    """
    def get_landing_height(last_move, board):
        return last_move.landing_height + ((last_move.piece.length - 1) / 2)

 
    def get_row_transitions(board, num_columns):
    """
    The total number of row transitions.
    A row transition occurs when an empty cell is adjacent to a filled cell
    on the same row and vice versa.
    """
        transitions = 0
        last_bit = 1

        for i in range(len(board)):
            row = board[i]
            for j in range(num_columns):
                bit = (row >> j) & 1
                if bit != last_bit):
                    transitions +=1

            last_bit = bit

            if (bit == 0):
                transitions +=1
            last_bit = 1
        return transitions;


    def get_column_transitions(board, num_columns):
        """
        The total number of column transitions.
        A column transition occurs when an empty cell is adjacent to a filled cell
        on the same row and vice versa.
        """
        var transitions = 0;
        var last_bit = 1;

        for i in range(num_columns):
            for j in range(len(board)):
                var row = board[j];
                var bit = (row >> i) & 1;
      
                if (bit != last_bit):
                    transitions +=1;
            last_bit = bit;
        last_bit = 1;
        return transitions;

    def get_hole_number(board, num_columns):
        """
        
        """
        holes = 0;
        row_holes = 0x0000;
        previous_row = board[board.length - 1];

        for i in range(len(board) - 2,-1,-1):
            row_holes = ~board[i] & (previous_row | row_holes)
            for j in range(num_columns):
                holes += ((row_holes >> j) & 1)
            previous_row = board[i];
        return holes;

    def get_well_sums(board, num_columns):
        """
         A well is a sequence of empty cells above the top piece in a column such
         that the top cell in the sequence is surrounded (left and right) by occupied
         cells or a boundary of the board.
      
         Args:
            board - The game board (an array of integers)
           num_columns - Number of columns in the board
        
         Return:
            The well sums. For a well of length n, we define the well sums as
            1 + 2 + 3 + ... + n. This gives more significance to deeper holes.
        """
        var well_sums = 0;

        # Check for well cells in the "inner columns" of the board.
        # "Inner columns" are the columns that aren't touching the edge of the board.
        for i in range(num_columns - 1):
            for j in range(board.length - 1, -1, -1):
                if ((((board[j] >> i) & 1) == 0) && 
                      (((board[j] >> (i - 1)) & 1) == 1) &&
                      (((board[j] >> (i + 1)) & 1) == 1)) {

                    # Found well cell, count it + the number of empty cells below it.
                    well_sums +=1

                    for k in range(j - 1, -1, -1):
                        if (((board[k] >> i) & 1) == 0):
                            well_sums +=1;
                        else:
                            break;

        # Check for well cells in the leftmost column of the board.
        for j in range(len(board)-1, -1, -1):
            if ((((board[j] >> 0) & 1) == 0) && 
              (((board[j] >> (0 + 1)) & 1) == 1)):

                 # Found well cell, count it + the number of empty cells below it.
                 #++well_sums;

                 for k in range(j - 1, -1, -1):
                    if (((board[k] >> 0) & 1) == 0):
                        well_sums +=1;
                    else:
                        break;
                        
                        
        # Check for well cells in the rightmost column of the board.
        for (var j = board.length - 1; j >= 0; --j) {
            if ((((board[j] >> (num_columns - 1)) & 1) == 0) && 
                  (((board[j] >> (num_columns - 2)) & 1) == 1)) {
                      # Found well cell, count it + the number of empty cells below it.

                    well_sums +=1
                    for k in range(j - 1, -1, -1):
                        if (((board[k] >> (num_columns - 1)) & 1) == 0):
                            well_sums +=1;
                        else:
                            break;

        return well_sums;
