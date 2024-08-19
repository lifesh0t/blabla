import random
from board import board
from squares import empty

class Game:
    def __init__(self):
        self.board = [' '] * 10
        self.status = 'Running'
        self.symbol_1 = ''
        self.symbol_2 = ''
        self.current_player = 1

    def reset(self):
        """Reset the game state for a new game."""
        self.board = [' '] * 10
        self.status = 'Running'
        self.current_player = 1
        self.symbol_1 = ''
        self.symbol_2 = ''
        
    def intro(self):
        print("Tic Tac Toe game.")
        print("Spauskite Enter norėdami tęsti, arba parasykite q norėdami nutraukti.")
        while True:
            user_input = input().strip().lower()
            if user_input == '':
                break
            elif user_input == 'q':
                print("Žaidimas baigtas.")
                exit()

    def setup_symbols(self):
        self.symbol_1 = input("X ar O? ").upper()
        if self.symbol_1 == "X":
            self.symbol_2 = "O"
            print("Žaidėjas 2 bus O.")
        else:
            self.symbol_2 = "X"
            print("Žaidėjas 2 bus X.")
        input("Spausk Enter norėdamas tęsti.")

    def check_position(self, x):
        return self.board[x] == ' '

    def check_win(self):
        win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  
                          (1, 4, 7), (2, 5, 8), (3, 6, 9),  
                          (1, 5, 9), (3, 5, 7)]             

        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                self.status = 'Win'
                return

        if ' ' not in self.board[1:]:
            self.status = 'Draw'

    def random_place(self, player):
        selection = empty(self.board)
        if selection:
            current_loc = random.choice(selection)
            self.board[current_loc] = player


# self.board: Tai sąrašas, kuris reprezentuoja žaidimo lentą. Sąrašas turi 10 elementų, bet pirmas elementas (self.board[0]) yra ignoruojamas, 
# kad būtų lengviau dirbti su lentele. Kiekvienas elementas self.board[1] iki self.board[9] atitinka vieną iš devynių langelių lentoje.

# self.board[x]: Ši dalis prieina prie žaidimo lentos (self.board), kurioje yra saugomi visų langelių būsenos. x nurodo konkretų langelį lentoje.
# self.board[x] == ' ': Patikrina, ar pasirinkto langelio (nurodyto x) turinys yra tuščias (' ').

# win_conditions: Tai sąrašas, kuriame yra visos galimos laimėjimo linijos ant žaidimo lentos.
# Kiekvienas elementas yra trijų skaičių tuplas, atitinkanti langelius lentoje, kurie sudaro laimėjimo liniją
# self.board[a] == self.board[b] == self.board[c]: Patikrina, ar trijų langelių, nurodytų šioje sąlygoje, turinys yra vienodas (t.y., visi trys langeliai turi tą patį simbolį)
# self.board[a] != ' ': Patikrina, ar simbolis, esantis pirmame langelyje (kuris yra self.board[a]), nėra tuščias (' ').
# Tai užtikrina, kad tikrai yra simbolis (t.y., nebuvo praleista pozicija arba niekas ten nėra).

# ' ' not in self.board[1:] yra teisinga (t.y., jei nėra laisvų langelių), tai reiškia,
# kad žaidimo lenta yra pilna ir žaidimas baigėsi lygiosiomis, nes nė vienas žaidėjas nepasiekė laimėjimo sąlygų.

# laisva(self.board): Ši funkcija grąžina sąrašą su laisvų vietų numeriais ant žaidimo lentos. Tai rodo visus langelius, kurie yra laisvi ir į kuriuos galima atlikti ėjimą.
# self.board[current_loc] = player: Nustato pasirinktą langelį (current_loc) į kompiuterio simbolį (player). Tai užpildo pasirinktą langelį su kompiuterio simboliu ant žaidimo lentos.

# def CheckWin():
#     global Game

#     if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
#         Game = Win
#     elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
#         Game = Win
#     elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
#         Game = Win
#     elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
#         Game = Win
#     elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
#         Game = Win
#     elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
#         Game = Win
#     elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
#         Game = Win
#     elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
#         Game = Win
#     elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
#             board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
#             board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
#         Game = Draw
#     else:
#         Game = Running