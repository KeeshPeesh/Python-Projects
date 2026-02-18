class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def print_board(self):
        print('\n')
        for i in range(3):
            print(f' {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ')
            if i < 2:
                print('-----------')
        print('\n')
    
    def is_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)
    
    def is_board_full(self):
        return ' ' not in self.board
    
    def play(self):
        while True:
            self.print_board()
            
            while True:
                try:
                    position = int(input(f"Player {self.current_player}, enter position (0-8): "))
                    if 0 <= position <= 8 and self.board[position] == ' ':
                        self.board[position] = self.current_player
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Enter a number between 0 and 8.")
            
            if self.is_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break
            
            self.current_player = 'O' if self.current_player == 'X' else 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.play()