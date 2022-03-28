# "random" library for computer decision.
import random

#A dictionary for our Tic Tac Toe grid table.
table = {
    '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6',
    '7': '7', '8': '8', '9': '9'
    }
turn = {'count': 1}
#Repeat until the game is not over.
while True:
        
    #Print Banner    
    print('\nTic tac Toe\nby Dan\n')

    #print tictac board.
    print(table['1']+'|'+table['2']+'|'+table['3'])
    print('-----');
    print(table['4']+'|'+table['5']+'|'+table['6'])
    print('-----');
    print(table['7']+'|'+table['8']+'|'+table['9'])

    #check both vertical/horizontal match and decide winner.
    if table['1']== 'X' and table['2']== 'X' and table['3'] == 'X' or table['4']== 'X' and table['5']== 'X' and table['6'] == 'X' or table['7']== 'X'  and table['8']== 'X' and table['9'] == 'X' or table['1']== 'X'  and table['4']== 'X' and table['7'] == 'X' or table['2']== 'X'  and table['5']== 'X' and table['8'] == 'X' or table['3']== 'X'  and table['6']== 'X' and table['9'] == 'X':
        print("Congrats!! you won.")
        break
    elif table['1'] == 'O' and table['2'] == 'O' and table['3'] == 'O' or table['4'] == 'O' and table['5'] == 'O' and table['6'] == 'O' or table['7'] == 'O'  and table['8'] == 'O' and table['9'] == 'O' or table['1']== 'X'  and table['4']== 'X' and table['7'] == 'Y' or table['2']== 'Y'  and table['5']== 'Y' and table['8'] == 'Y' or table['3']== 'Y'  and table['6']== 'Y' and table['9'] == 'Y':
        print("Bot won.")
        break
    #check diagonal match and decide winner.    
    elif table['1'] == 'X' and table['5'] == 'X' and table['9'] == 'X' or table['3'] == 'X' and table['5'] == 'X' and table['7'] == 'X':
        print("Congrats!! you won.")
        break
    elif table['1'] == 'O' and table['5'] == 'O' and table['9'] == 'O'  or table['3'] == 'O' and table['5'] == 'O' and table['7'] == 'O':
        print("Bot won.")
        break
    else:
        print("")
    
    #ask for user turn
    player = input("\nyour turn: ")
    
    #computer turn
    turn['count'] += 1
    if(turn['count'] == 6):
        table[player] = 'X'
        
        #Print Banner    
        print('\nTic tac Toe\nby Dan\n')

        #print dictionary table.
        print(table['1']+'|'+table['2']+'|'+table['3'])
        print('-----');
        print(table['4']+'|'+table['5']+'|'+table['6'])
        print('-----');
        print(table['7']+'|'+table['8']+'|'+table['9'])

        if table['1']== 'X' and table['2']== 'X' and table['3'] == 'X' or table['4']== 'X' and table['5']== 'X' and table['6'] == 'X' or table['7']== 'X'  and table['8']== 'X' and table['9'] == 'X' or table['1']== 'X'  and table['4']== 'X' and table['7'] == 'X' or table['2']== 'X'  and table['5']== 'X' and table['8'] == 'X' or table['3']== 'X'  and table['6']== 'X' and table['9'] == 'X':
            print("Congrats!! you won.")
            break
        elif table['1'] == 'O' and table['2'] == 'O' and table['3'] == 'O' or table['4'] == 'O' and table['5'] == 'O' and table['6'] == 'O' or table['7'] == 'O'  and table['8'] == 'O' and table['9'] == 'O' or table['1']== 'X'  and table['4']== 'X' and table['7'] == 'Y' or table['2']== 'Y'  and table['5']== 'Y' and table['8'] == 'Y' or table['3']== 'Y'  and table['6']== 'Y' and table['9'] == 'Y':
            print("Bot won.")
            break
        #check diagonal match and decide winner.    
        elif table['1'] == 'X' and table['5'] == 'X' and table['9'] == 'X' or table['3'] == 'X' and table['5'] == 'X' and table['7'] == 'X':
            print("Congrats!! you won.")
            break
        elif table['1'] == 'O' and table['5'] == 'O' and table['9'] == 'O'  or table['3'] == 'O' and table['5'] == 'O' and table['7'] == 'O':
            print("Bot won.")
            break
        else:
            print("Tie.")
            break
    else:
        computer = random.choice(list(table.keys()))

    #check for duplicates
    if table[player] == 'X' or table[player] == 'O':
        turn['count'] -= 1
        print("\n-- try again --")
    #if computer made a duplicate move, repeat new random choice.
    elif table[player] == table[computer] or table[computer] == 'O' or table[computer] == 'X':
        while True:
            if table[player] == table[computer] or table[computer] == 'O' or table[computer] == 'X':
                computer = random.choice(list(table.keys()))
            #save move to the dictionary.
            else:
                table[player] = 'X'
                table[computer] = 'O'
                break
    #save move to the dictionary.
    else:
        table[player] = 'X'
        table[computer] = 'O'