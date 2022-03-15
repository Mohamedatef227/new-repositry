# Tic Tac Toe With Numbers


#board list

Board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]


#First player is Even


First_player = 'even'


#Displaying Board



def Display_Board():
    print('|', Board[0], '|', Board[1], '|', Board[2], '|')
    print('|', Board[3], '|', Board[4], '|', Board[5], '|')
    print('|', Board[6], '|', Board[7], '|', Board[8], '|')


#move function



def move(M1, M2):
    if Board[M2-1] == 0:
        Board[M2-1] = M1
    else:
        current_player = First_player
        turn(current_player)
        return False
    Display_Board()


#moveing function for odd player


def odd(M, M2):
    while(M % 2 == 0):
        M = int(input ('enter an odd number'))

    move(M, M2)


#moveing function for Even player


def even(M, M2):
    while(M % 2 != 0):
        M = int(input ('enter an even number'))

    move(M, M2)


#check For Winner!


def winner():
    if (Board[0] + Board[1] + Board[2] == 15 or
        Board[0] + Board[3] + Board[6] == 15 or
        Board[1] + Board[4] + Board[7] == 15 or
        Board[3] + Board[4] + Board[5] == 15 or
        Board[2] + Board[5] + Board[8] == 15 or
        Board[6] + Board[7] + Board[8] == 15 or
        Board[0] + Board[4] + Board[8] == 15 or
        Board[2] + Board[4] + Board[6] == 15):
        print(First_player + ' is the winner')
        return True
    else:
        return False


#turn function to switch turn after every move
def turn(s):
    print('its ' + s + ' turn')
    M = int(input('enter the number: '))
    M1 = int(input('enter the places number: '))
    if First_player == 'even':
        even(M, M1)
    else:
        odd(M, M1)


#Game instructions.

print("                                 *welcome To TIC TAC TIE numbers*")
print("*EVEN PLAYER IS ALLOWED TO USE ONLY EVEN NUMBERS*")
print("*ODD  PLAYER IS ALLOWED TO USE ONLY ODD NUMBERS*")
print("*the player with the even numbers start*")
Display_Board()

while(True):
    turn(First_player)
    if winner():
        break
    else:
        if First_player == 'even' : First_player = 'odd'
        else:
            First_player = 'even'
