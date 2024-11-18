import tkinter as tk
import random
WIDTH = 5  # Number of columns in the grid
HEIGHT = 5  # Number of rows in the grid
MINES = 5  # Total number of mines in the grid


class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        self.grid = self.create_grid()
        self.revealed = set()
        self.buttons = {}
        for x in range(HEIGHT):
            for y in range(WIDTH):
                button = tk.Button(root, width=4, height=2,
                                   command=lambda x=x, y=y: self.reveal(x, y))
                button.grid(row=x, column=y)
                self.buttons[(x, y)] = button

    def create_grid(self):
        grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        mines = set()
        while len(mines) < MINES:
            x, y = random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)
            mines.add((x, y))
        for x, y in mines:
            grid[x][y] = -1
        for x in range(HEIGHT):
            for y in range(WIDTH):
                if grid[x][y] == -1:
                    continue
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and grid[nx][ny] == -1:
                            grid[x][y] += 1
        return grid

    def reveal(self, x, y):
        if (x, y) in self.revealed:
            return
        self.revealed.add((x, y))
        button = self.buttons[(x, y)]
        if self.grid[x][y] == -1:
            button.config(text="*", bg="red")
            self.game_over()
        else:
            button.config(
                text=str(self.grid[x][y]) if self.grid[x][y] > 0 else "", relief="sunken")
        if len(self.revealed) == HEIGHT * WIDTH - MINES:
            self.win_game()

    def game_over(self):
        for (x, y), button in self.buttons.items():
            if self.grid[x][y] == -1:
                button.config(text="*", bg="red")
        self.show_message("Game Over!")

    def win_game(self):
        self.show_message("Congratulations, You Win!")

    def show_message(self, message):
        message_label = tk.Label(
            self.root, text=message, font=("Helvetica", 16))
        message_label.grid(row=HEIGHT, column=0, columnspan=WIDTH)


def start_game():
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()


if __name__ == "__main__":
    start_game()
