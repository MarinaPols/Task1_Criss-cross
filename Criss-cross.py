#game field - 3x3; 2 players
#1: Instruction
selection = (input("Enter Yes if you want to play, or No to enter:"))
player1 = "X"
player2 = "0"
win = 0 #флаг для победы
counter = 0 #счетчик ходов

if ("yes" in selection):
    instr = 1
else: instr = 0
def Game_field(field):
    print("-------------")
    for i in range(3):
        print( "|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-------------")

def Instrustion():
    print("""
Welcome to my first game - Criss-Cross
You will play now,
Let's start
    """)
    Game_field(field)
# create a field
field = list(range(1, 10))
score = 0

def Move(player):
    valid = False
    while not valid:
        question = input("Please enter " + player)
        try:
            question = int(question)
        except:
            print ("Incorrect. Please enter the nummber")
            continue
        if question >= 1 and question <= 9:
            if (str(field[question-1]) not in "XO"):
                field[question-1] = player
                valid = True
            else:
                print ("Not a right step")
        else:
            print ("Incorrect input. Enter the number in a range 1-9")
def check_win(field):
    win_code = [
        [0, 1, 2]
        , [0, 3, 6]
        , [1, 4, 7]
        , [2, 5, 8]
        , [6, 7, 8]
        , [3, 4, 5]
        , [2, 4, 6]
        , [0, 4, 8]
    ]
    for each in win_code:
        if field[each[0]] == field[each[1]] == field[each[2]]:
           return field[each[0]]
    return False
#main program
if (instr != 1):
    print("See you next time")
    exit()
if (instr == 1):
    #input the selection
    Instrustion()
    while win == 0:
        #Game_field(field)
        if (counter % 2 == 0):
            Move(player1)
        else:
            Move(player2)
        counter += 1
        if counter > 4:
           score = check_win(field)
           print(score)
        if score:
            print("Congratulations! You are won!")
            win = 1
            break
        if (counter == 9):
            print("No winners, play again")
            break
        Game_field(field)








