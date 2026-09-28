import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        # Player 1 is 'X', Player 2 is 'O'
        self.current_player = "X"
        self.game_over = False

        # 3x3 board representation
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        # Will hold our 3x3 grid of Tkinter button widgets
        self.buttons = []

        self.setup_ui()

    def setup_ui(self):
        # Header / Status text
        self.status_label = tk.Label(
            self.root,
            text="Player X's Turn",
            font=("Arial", 14, "bold"),
            pady=10
        )
        self.status_label.pack()

        # Board container frame
        board_frame = tk.Frame(self.root)
        board_frame.pack(padx=15, pady=5)

        # Create 3x3 grid of buttons using nested loops
        for row in range(3):
            row_buttons = []
            for col in range(3):
                btn = tk.Button(
                    board_frame,
                    text="",
                    font=("Arial", 22, "bold"),
                    width=4,
                    height=2,
                    bg="#ffffff",
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                btn.grid(row=row, column=col, padx=3, pady=3)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        # Restart button at the bottom
        restart_btn = tk.Button(
            self.root,
            text="Restart Game",
            font=("Arial", 11),
            bg="#e0e0e0",
            relief="groove",
            command=self.restart_game
        )
        restart_btn.pack(pady=12)

    def make_move(self, row, col):
        # Don't do anything if game has already ended
        if self.game_over:
            return

        # Check if the clicked box is already taken
        if self.board[row][col] != "":
            messagebox.showwarning("Invalid Move", "This box is already taken!")
            return

        # Place player's mark on the board
        self.board[row][col] = self.current_player
        
        # Color X in blue and O in red so it's easy to read
        text_color = "#1565c0" if self.current_player == "X" else "#c62828"
        self.buttons[row][col].config(text=self.current_player, fg=text_color)

        # Check if this move wins the game
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.highlight_winning_cells(winner)
            self.status_label.config(text=f"Player {self.current_player} Wins!", fg="#2e7d32")
            messagebox.showinfo("Game Over", f"Player {self.current_player} Wins!")
            return

        # Check if the board is full (draw)
        if self.check_draw():
            self.game_over = True
            self.status_label.config(text="It's a Draw!", fg="#ef6c00")
            messagebox.showinfo("Game Over", "It's a Draw!")
            return

        # Switch to the other player
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(
            text=f"Player {self.current_player}'s Turn",
            fg="#000000"
        )

    def check_winner(self):
        # Check 3 rows
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] != "":
                return [(r, 0), (r, 1), (r, 2)]

        # Check 3 columns
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] != "":
                return [(0, c), (1, c), (2, c)]

        # Check main diagonal (top-left to bottom-right)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return [(0, 0), (1, 1), (2, 2)]

        # Check anti-diagonal (top-right to bottom-left)
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return [(0, 2), (1, 1), (2, 0)]

        return None

    def check_draw(self):
        # If any cell is still empty, game is not a draw
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def highlight_winning_cells(self, cells):
        # Highlight the 3 winning buttons in light green
        for r, c in cells:
            self.buttons[r][c].config(bg="#c8e6c9")

    def restart_game(self):
        # Reset turn and game state
        self.current_player = "X"
        self.game_over = False

        # Reset board data
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        # Reset status label
        self.status_label.config(text="Player X's Turn", fg="#000000")

        # Clear button text and reset background color
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", bg="#ffffff")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
