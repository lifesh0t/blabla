# Funkcija get_player_choice leidžia žaidėjui pasirinkti vieną iš laisvų lentos langelių, kurio numeris yra nuo 1 iki 9.
# Begalinis ciklas while True Funkcija veikia tol, kol žaidėjas įveda teisingą pasirinkimą.
# Funkcija possibilities nustato, kurie langeliai lentoje yra laisvi, t.y., kuriuose dar nėra įrašytas simbolis (X arba O).
# Tikrinama, ar kiekviename lentos langelyje (board[i]) nėra įrašytas joks simbolis (' ').
def get_player_choice():
    while True:
        try:
            choice = int(input("Choose a cell [1-9]: "))
            if choice in range(1, 10):
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def empty(board):
    return [i for i in range(1, 10) if board[i] == ' ']
