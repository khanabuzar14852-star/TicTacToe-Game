# 🎮 2-Player Tic Tac Toe Game (Python GUI)

A simple, clean 2-player desktop Tic Tac Toe game built using Python's standard **Tkinter** library.

---

## 📌 Project Details
- **Project Name:** Tic Tac Toe GUI
- **Language:** Python 3
- **GUI Toolkit:** Tkinter (Standard library, no external installation required)
- **Controls:** Mouse click to mark cells
- **Target Audience:** College / School Python Project & Viva Submission

---

## ✨ Features
1. **2-Player Gameplay:**
   - Player 1 marks **X** (colored blue).
   - Player 2 marks **O** (colored red).
2. **Move Validation:**
   - Players cannot click an already occupied cell. A pop-up warning alerts them to pick an empty box.
3. **Automatic Win Detection:**
   - Checks after every single turn for all **8 winning combinations**:
     - 3 Horizontal Rows
     - 3 Vertical Columns
     - 2 Diagonals
4. **Winning Cells Highlight:**
   - The 3 winning squares automatically turn soft green to make the victory clear.
5. **Draw Detection:**
   - If all 9 boxes are filled and no player has won, an *"It's a Draw!"* notification appears.
6. **Restart Game Button:**
   - Resets the board, clears symbols, resets the colors, and starts a fresh game anytime.

---

## 📁 Project Structure
```text
TicTacToe/
│
├── tic_tac_toe.py     # Main Python script containing GUI and game logic
└── README.md          # Project documentation, running instructions, and viva prep
```

---

## 🚀 How to Run the Project

### Method 1: Using VS Code
1. Open **Visual Studio Code**.
2. Go to **File** ➔ **Open Folder...** and select this `TicTacToe` folder on your Desktop.
3. Open `tic_tac_toe.py`.
4. Click the **Run** button (▶) in the top-right corner, or press `F5` / `Ctrl + F5`.

### Method 2: Using Command Prompt / PowerShell
1. Open PowerShell or Command Prompt.
2. Navigate to this folder:
   ```powershell
   cd "$HOME\Desktop\TicTacToe"
   ```
   *(or if using OneDrive Desktop: `cd "$HOME\OneDrive\Desktop\TicTacToe"`)*
3. Run the script:
   ```powershell
   python tic_tac_toe.py
   ```
   *(If `python` is not recognized, use `py tic_tac_toe.py`).*

---

## 🧠 Core Programming Concepts Used (Viva Preparation)

Here is a quick guide on how to explain the code when asked by an examiner or teacher during your project viva:

### 1. Variables
- `self.current_player`: Stores a string (`"X"` or `"O"`) indicating which player's turn it is.
- `self.game_over`: A boolean flag (`True` / `False`) that blocks further moves once someone wins or when the game is a draw.

### 2. Lists & 2D Arrays (Matrices)
- `self.board`: A 3×3 matrix (list of lists) that stores the internal state (`""`, `"X"`, or `"O"`):
  ```python
  [
      ["", "", ""],
      ["", "", ""],
      ["", "", ""]
  ]
  ```
  *Why use this?* It separates the internal data logic from the visual GUI buttons.
- `self.buttons`: A 2D list storing references to the 9 Tkinter button objects so we can update their text and colors dynamically.

### 3. Loops (`for` loops)
- **Nested Loops:** We use two loops (`for row in range(3):` and `for col in range(3):`) to generate the 3x3 grid cleanly without copy-pasting button definitions 9 times.
- **Iteration:** Loops are also used in `check_winner()` to scan each row and column, and in `check_draw()` to scan for empty cells.

### 4. Conditional Statements (`if` / `elif` / `else`)
- **Move Validation:** Checks `if self.board[row][col] != ""` to prevent overwriting cells.
- **Winning Logic:** Uses chained conditions like `if self.board[r][0] == self.board[r][1] == self.board[r][2] != ""` to test if all three cells match and are not empty.
- **Turn Switch:** Switches between Player X and Player O after each valid move.

### 5. Functions & Methods
- `setup_ui()`: Creates and places labels, grid buttons, and the restart button.
- `make_move(row, col)`: The main event handler that runs when any square is clicked.
- `check_winner()`: Checks the 8 win patterns and returns the winning coordinates.
- `check_draw()`: Verifies if the board is completely full with no winner.
- `highlight_winning_cells()`: Tints the winning 3 buttons green.
- `restart_game()`: Clears the board and resets game variables.

### 6. GUI Buttons (`tk.Button`)
- Tkinter's `Button` widget handles clickable cells with customized fonts, sizes, and colors.

### 7. Event Handling & Lambdas
- In Tkinter, the `command` attribute connects button clicks to a Python function.
- We use a lambda function with default arguments:
  ```python
  command=lambda r=row, c=col: self.make_move(r, c)
  ```
  *Viva Tip:* Passing `r=row, c=col` captures the current loop's coordinate values at creation time so each button knows its own position when clicked.
