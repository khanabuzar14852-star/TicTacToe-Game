# 2-Player Tic Tac Toe Game (Python GUI)

A simple, clean 2-player desktop Tic Tac Toe game built using Python's standard **Tkinter** library.

---

##  Project Details
- **Project Name:** Tic Tac Toe GUI
- **Language:** Python 3
- **GUI Toolkit:** Tkinter (Standard library, no external installation required)
- **Controls:** Mouse click to mark cells
- **Target Audience:** College / School Python Project & Viva Submission

---

##  Features
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

##  Project Structure
```text
TicTacToe/
│
├── tic_tac_toe.py     # Main Python script containing GUI and game logic
└── README.md          # Project documentation, running instructions, and viva prep
```

---

##  How to Run the Project

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

