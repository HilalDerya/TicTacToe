from tkinter import * 
from tkinter import messagebox 
import random

current_player = 'X'
stop_game = False

def clicked(r,c):
  global current_player
  if board[r][c]["text"] == "" and not stop_game:
        board[r][c]["text"] = current_player
        states[r][c] = current_player
        check_if_win()
        current_player = 'O' if current_player == 'X' else 'X'
        if current_player == 'O':
            computer_move()
 
def computer_move():
    global stop_game
    if not stop_game:
        empty_cells = [(r, c) for r in range(3) for c in range(3) if states[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            clicked(r, c)


def check_if_win():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] !=0:
            stop_game=True
            if states[i][0] == 'X':
                winner = messagebox.showinfo("Winner", "Human Won")
            else:
                winner = messagebox.showinfo("Winner", "Computer Won")
            return

        if states[0][i] == states[1][i] == states[2][i] !=0:
            stop_game=True
            if states[0][i] == 'X':
                winner = messagebox.showinfo("Winner", "Human Won")
            else:
                winner = messagebox.showinfo("Winner", "Computer Won")
            return

    if states[0][0] == states [1][1] == states [2][2] !=0:
        stop_game= True
        if states[0][0] == 'X':
            winner = messagebox.showinfo("Winner", "Human Won")
        else:
            winner = messagebox.showinfo("Winner", "Computer Won")
        return
    
    if states[0][2] == states[1][1] == states[2][0] !=0:
        stop_game = True
        if states[0][2] == 'X':
            winner = messagebox.showinfo("Winner", "Human Won")
        else:
            winner = messagebox.showinfo("Winner", "Computer Won")
        return
 
    if all(all(cell != 0 for cell in row) for row in states):
        stop_game = True
        winner = messagebox.showinfo("Tie", "It's a Tie!")


root = Tk()

root.title("Tic Tac Toe: Human Against Computer")
root.resizable(0,0)

board=[[0,0,0] for _ in range(3)]

states = [[0,0,0] for _ in range(3)]

for i in range(3):
    for j in range(3):
        board[i][j] = Button(
            height = 3, width=8,
            font = ("Helvetica","20"),
            command = lambda r = i, c = j : clicked(r,c))
        board[i][j].grid(row = i, column = j)

mainloop()