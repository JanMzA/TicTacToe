import random as rd


def change_player_symbol(current_symbol):
    if current_symbol == "X":
        next_symbol = "O"

    else:
        next_symbol = "X"

    return next_symbol


def eingabe_position():
    try:
        row = int(input("Geben Sie die Reihe ein: "))
        col = int(input("Geben Sie die Spalte ein: "))
        return row, col

    except:
        print("Geben Sie Zahlen ein")
        TicTacToe().eingabe_position()


class TicTacToe:

    def __init__(self, win=False, groesse=3):
        self.groesse = groesse
        self.spielfeld = [["_" for i in range(groesse)] for j in range(groesse)]
        self.win = win

    def print_spielfeld(self):
        for row in self.spielfeld:
            print(*row)

    def check_zug_gueltig(self, row, col):
        if row > 2 or col > 2 or self.spielfeld[row][col] != "_":
            print("ungültige Eingabe, Eingabe wiederholen")
            return False

        if self.spielfeld[row][col] == "_":
            return True

    def set_stone(self, row, col, player_symbol):
        self.spielfeld[row][col] = player_symbol

    def check_win(self, player_symbol):
        directions = ["row", "col", "diagonal"]
        break_out_dir = False

        for dir in directions:

            if break_out_dir:
                break

            if dir == "row":

                for row in range(self.groesse):
                    if self.spielfeld[row][0] == self.spielfeld[row][1] == self.spielfeld[row][2] == player_symbol:
                        self.win = True
                        break_out_dir = True
                        break

            elif dir == "col":

                for col in range(self.groesse):
                    if self.spielfeld[0][col] == self.spielfeld[1][col] == self.spielfeld[2][col] == player_symbol:
                        self.win = True
                        break_out_dir = True
                        break

            elif dir == "diagonal":
                ways = ["uptodown", "downtoup"]

                for way in ways:

                    if way == "uptodown":
                        if self.spielfeld[0][0] == self.spielfeld[1][1] == self.spielfeld[2][2] == player_symbol:
                            self.win = True
                            break_out_dir = True
                            break

                    elif way == "downtoup":
                        if self.spielfeld[2][0] == self.spielfeld[1][1] == self.spielfeld[0][2] == player_symbol:
                            self.win = True
                            break_out_dir = True
                            break

        if self.win:
            print("Player " + player_symbol + " hat gewonnen")

        return self.win

    def check_spielfeld_voll(self):
        if "_" not in self.spielfeld[0] and "_" not in self.spielfeld[1] and "_" not in self.spielfeld[2]:
            self.win = True

        if self.win:
            print("Spiel endet unentschieden")
        return self.win


Spielfeld = TicTacToe()
symbole = ["X", "O"]

player_symbol = symbole[rd.randint(0, 1)]

Spielfeld.print_spielfeld()

while not Spielfeld.check_win(player_symbol):
    print(player_symbol + " ist an der Reihe")
    eingabegueltig = False
    while not eingabegueltig:
        row, col = Spielfeld.eingabe_position()
        eingabegueltig = Spielfeld.check_zug_gueltig(row, col)
    Spielfeld.set_stone(row, col, player_symbol)
    win = Spielfeld.check_win(player_symbol)
    if win:
        break
    Spielfeld.print_spielfeld()
    player_symbol = change_player_symbol(player_symbol)
    full = Spielfeld.check_spielfeld_voll()
    if full:
        break

# Konsole zum Spielen öffnen (pygame)
