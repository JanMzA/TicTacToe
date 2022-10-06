

class TicTacToe:


    def __init__(self, win = False,groesse = 3):
        self.groesse = groesse
        self.spielfeld = [["_" for i in range(groesse)]for j in range(groesse)]
        self.win = win

    def print_spielfeld(self):
        for row in self.spielfeld:
            print(*row)


    def set_stone(self,row,col,player_symbol):
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



    def check_win_row(self):
        pass


Spielfeld = TicTacToe()

Spielfeld.set_stone(2,0,"X")
Spielfeld.set_stone(1,1,"X")
Spielfeld.set_stone(0,2,"X")
Spielfeld.print_spielfeld()

Spielfeld.check_win("X")
print(Spielfeld.win)






