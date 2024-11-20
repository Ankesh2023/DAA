def is_safe(x, y, N, visited):
    # Check if the position is within bounds and not yet visited
    return 0 <= x < N and 0 <= y < N and not visited[x][y]

def knight_tour_util(x, y, move_count, N, visited, move_x, move_y, board):
    # Base case: if all cells are visited
    if move_count == N * N:
        return True

    # Try all 8 possible moves for the knight
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        
        # Check if the next move is safe
        if is_safe(next_x, next_y, N, visited):
            visited[next_x][next_y] = True
            board[next_x][next_y] = move_count
            
            # Recur to the next move
            if knight_tour_util(next_x, next_y, move_count + 1, N, visited, move_x, move_y, board):
                return True
            
            # Backtrack if no solution found
            visited[next_x][next_y] = False
            board[next_x][next_y] = -1

    return False

def knight_tour(N, start_x, start_y):
    visited = [[False for _ in range(N)] for _ in range(N)]  # Create a visited array
    board = [[-1 for _ in range(N)] for _ in range(N)]  # Create the board
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]  # Possible x moves for the knight
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]  # Possible y moves for the knight

    visited[start_x][start_y] = True  # Mark the starting position as visited
    board[start_x][start_y] = 0  # Set the first move to 0 (starting position)

    # Try to find a solution using backtracking
    if knight_tour_util(start_x, start_y, 1, N, visited, move_x, move_y, board):
        print("Knight's tour found!")
        print_board(board)
    else:
        print("No solution exists.")

def print_board(board):
    N = len(board)
    for row in range(N):
        for col in range(N):
            print(f"{board[row][col]:2}", end=" ")
        print()

def main():
    N = int(input("Enter the size of the chessboard (N x N): "))
    start_x = int(input("Enter the starting row (0 to {}): ".format(N - 1)))
    start_y = int(input("Enter the starting column (0 to {}): ".format(N - 1)))

    if 0 <= start_x < N and 0 <= start_y < N:
        knight_tour(N, start_x, start_y)
    else:
        print("Invalid starting position!")

if __name__ == "__main__":
    main()

