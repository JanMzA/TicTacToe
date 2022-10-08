

class TicTacToe:


    def __init__(self, win = False,groesse = 3):
        self.groesse = groesse
        self.spielfeld = [["_" for i in range(groesse)]for j in range(groesse)]
        self.win = win

    def print_spielfeld(self):
        for row in self.spielfeld:
            print(*row)

    def check_zug_gueltig(self,row,col):
        if row > 2 or col >2:
            return False
        if self.spielfeld[row][col] != "_":
            return True

    def set_stone(self,player_symbol):
        row = int(input("Geben Sie die Reihe ein: "))
        col = int(input("Geben Sie die Spalte ein: "))
        (self.spielfeld)[row][col] = player_symbol



    def check_win(self,player_symbol):
        directions = ["row", "col", "diagonal"]
        break_out_dir = False


        for dir in directions:

            if break_out_dir == True:
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




        return self.win



    def change_player_symbol(self,current_symbol):

        if current_symbol == "X":
            next_symbol = "O"

        else:
            next_symbol = "X"

        return next_symbol



    def check_spielfeld_voll(self):
        if "_" not in self.spielfeld[0] and "_" not in self.spielfeld[1] and "_"  not in self.spielfeld[2]:
            self.win = True

        return self.win



Spielfeld = TicTacToe()


player_symbol = "X"
Spielfeld.print_spielfeld()
while Spielfeld.check_win(player_symbol) == False:
    Spielfeld.set_stone(player_symbol)
    Spielfeld.check_win(player_symbol)
    Spielfeld.print_spielfeld()
    player_symbol = Spielfeld.change_player_symbol(player_symbol)
    Spielfeld.check_spielfeld_voll()













