# board yra sąrašas, kurio kiekvienas elementas atitinka vieną langelį lentoje.
# F-string yra formatavimo metodas, leidžiantis įterpti kintamuosius į tekstą. Pavyzdžiui, f" {board[1]} | {board[2]} | {board[3]} " 
# reiškia, kad bus išspausdinta pirmoji lentos eilutė, įterpiant simbolius iš board[1], board[2], ir board[3].

def board(board):
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")

# 
# 
# 
# 
# def DrawBoard(board):
#     print(" %c | %c | %c " % (board[1], board[2], board[3]))
#     print("___|___|___")
#     print(" %c | %c | %c " % (board[4], board[5], board[6]))
#     print("___|___|___")
#     print(" %c | %c | %c " % (board[7], board[8], board[9]))
#     print("   |   |   ")
