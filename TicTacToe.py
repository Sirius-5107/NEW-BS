theboard = {'11':' ','12':' ','13':' ',
            '21':' ','22':' ','23':' ',
            '31':' ','32':' ','33':' '}

turn='X'
move=''

def printboard(board):
    print(board['11']+' | '+board['12']+' | '+board['13'])
    print('--+---+--')
    print(board['21']+' | '+board['22']+' | '+board['23'])
    print('--+---+--')
    print(board['31']+' | '+board['32']+' | '+board['33'])

def wingame(board):
    if board['11']==board['12'] and board['11']==board['13'] and board['11']!=' ':
        print('Game over \nWinner is: '+board['11'])
        return True
    elif board['21']==board['22'] and board['21']==board['23'] and board['21']!=' ':
        print('Game over \nWinner is: '+board['21']) 
        return True
    elif board['31']==board['32'] and board['31']==board['33'] and board['31']!=' ':
        print('Game over \nWinner is: '+board['31']) 
        return True
    elif board['11']==board['21'] and board['11']==board['31'] and board['11']!=' ':
        print('Game over \nWinner is: '+board['11']) 
        return True
    elif board['12']==board['22'] and board['12']==board['32'] and board['12']!=' ':
        print('Game over \nWinner is: '+board['12']) 
        return True
    elif board['13']==board['23'] and board['13']==board['33'] and board['13']!=' ':
        print('Game over \nWinner is: '+board['13']) 
        return True
    elif board['11']==board['22'] and board['11']==board['33'] and board['11']!=' ':
        print('Game over \nWinner is: '+board['11']) 
        return True
    elif board['13']==board['22'] and board['13']==board['31'] and board['13']!=' ':
        print('Game over \nWinner is: '+board['13'])
        return True
    else:
        return False

def switch(current):
    if current =='X':
        return 'O'
    else:
        return 'X'



while True:
    
    printboard(theboard)
    
    move = input('Choose your box, player '+turn+' : ')
    
    if move not in theboard:
        print("Invalid box!")
        continue

    if theboard[move] != ' ':
        print("Box already taken!")
        continue

    theboard[move] = turn

    if wingame(theboard) != False:
        printboard(theboard)
        break

    turn = switch(turn)
    wingame(theboard)
    if ' ' not in theboard.values():
        printboard(theboard)
        print("It's a draw!")
        break