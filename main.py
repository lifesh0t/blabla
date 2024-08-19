from game import Game
from board import board
from squares import get_player_choice
import os

def main():
    game = Game()

    while True:  # Loop to allow replaying the game
        os.system('cls' if os.name == 'nt' else 'clear')
        game.intro()
        game.setup_symbols()

        while game.status == 'Running':
            os.system('cls' if os.name == 'nt' else 'clear')
            board(game.board)

            if game.current_player % 2 != 0:  # Player 1's turn
                print("Player 1's turn")
                Mark = game.symbol_1
                choice = get_player_choice()
                if game.check_position(choice):
                    game.board[choice] = Mark
                    game.current_player += 1
                    game.check_win()
            else:  # Computer's turn
                print("Computer's turn")
                Mark = game.symbol_2
                game.random_place(Mark)
                game.current_player += 1
                game.check_win()

            if game.status == 'Draw':
                os.system('cls' if os.name == 'nt' else 'clear')
                board(game.board)
                print("Game Draw")
                break
            elif game.status == 'Win':
                os.system('cls' if os.name == 'nt' else 'clear')
                board(game.board)
                game.current_player -= 1
                if game.current_player % 2 != 0:
                    print("Player 1 wins!")
                else:
                    print("Computer wins!")
                break

        play_again = input("Ar norite žaisti dar kartą? (taip/ne): ").strip().lower()
        if play_again != 'taip':
            print("Ačiū, kad žaidėte!")
            break
        else:
            game.reset()
if __name__ == "__main__":
    main()
    
# os.system('cls' if os.name == 'nt' else 'clear')
# Ekranas išvalomas prieš pradedant žaidimą.
# while game.status == 'Running':
# Šis ciklas vykdomas tol, kol žaidimo būsena yra Running. Tai reiškia, kad žaidimas dar nėra pasibaigęs (nei pergalė, nei lygiosios).
# game.current_player % 2 != 0, reiškia, kad dabar yra 1-ojo žaidėjo eilė.
# if game.check_position(choice) patikrina, ar pasirinktas langelis yra laisvas.
# Jei langelis laisvas, jis pažymimas žaidėjo simboliu, po kurio padidinamas žaidėjo numeris (game.current_player += 1).
# Tikrinama, ar po šio ėjimo žaidimas pasibaigė 
# Po kiekvieno ėjimo tikrinama žaidimo būsena
# if __name__ == "__main__" Šis blokas tikrina, ar skriptas vykdomas tiesiogiai, o ne importuojamas kaip modulis. Jei taip, iškviečiama main() funkcija, pradedanti žaidimą.