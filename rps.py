import sys
import random
#WALA AKONG MAGAWA POTA
def starter(game):
    print('Our Game is ' + game)
    
starter('ROCK, PAPER, SCISSOR')

def choose(wins, losses, ties):
    while True:
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True:
            player = input('Enter your Next move: (r)ock, (p)aper, (s)cissors, or (q)uit: ')
            if player == 'q':
                print('Thanks For Playing!')
                sys.exit()
            if player == 'r' or player == 'p' or player == 's':
                break
            print('Invalid Input! \n Please Type only r, p, s or q.')
            
        if player == 'r':
            print('ROCK versus...')
        elif player == 'p':
            print('PAPER versus...')
        elif player == 's':
            print('SCISSOR versus...')
                
        randomNum = random.randint(1,3)
        if randomNum == 1:
            computerMove = 'r'
            print('ROCK')
        elif randomNum == 2:
            computerMove = 'p'
            print('PAPER')
        elif randomNum == 3:
            computerMove = 's'
            print('SCISSOR')
                    
        if player == computerMove:
            print("It's A Tie!")
            ties = ties + 1
        elif player == 'r' and computerMove == 's':
            print('You Win!')
            wins = wins + 1
        elif player == 'p' and computerMove == 'r':
            print('You Win!!')
            wins = wins + 1
        elif player == 's' and computerMove == 'p':
            print('You Win!')
            wins = wins + 1
        if player == 's' and computerMove == 'r':
            print('haha talo BOBO MO')
            losses = losses + 1
        elif player == 'r' and computerMove == 'p':
            print('Tanga mo naman natatalo kapa dito')
            losses = losses + 1
        elif player == 'p' and computerMove == 's':
            print('Wag kana maglaro bobo mo Talo sa computer amputa')
            losses = losses + 1
            
choose(0,0,0)
                    
                    
                    
                
                
                    
                
    
     
            
    

            


    
    
    


