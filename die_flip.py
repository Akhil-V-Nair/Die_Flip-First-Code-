#A game where a coin is flipped and a die is rolled simultaneously for a 
#certain number of times and if the coin flipped is Heads and die rolled is 
#an even number then a Win is registered.
#Also if the coin flipped is Tails and die rolled is an odd number, once again 
#a win is registered.
#If the wins are more than the losses, the user wins the game of "DIE FLIP"


import random

def die_flip():
    number = int(input('Enter the number of times the die to be rolled and coin to be flipped: '))
    recorder = []
    for i in range(number):
        flip = random.randint(0,1)
        if flip == 0:
           recorder.append('Heads')
        else:
           recorder.append('Tails')
    H = recorder.count('Heads')
    T = recorder.count('Tails')
    
    
    result_counter = []
    for roll in range(number):
        roll = random.randrange(1,7)
        if roll in [2,4,6] and flip == 0:
            result_counter.append('W')
        elif roll in [1,3,5] and flip == 1:
            result_counter.append('W')
        elif roll in [2,4,6] and flip == 1:
            result_counter.append('L')
        elif roll in [1,3,5] and flip == 0:
            result_counter.append('L')
            
    W = result_counter.count('W')
    L = result_counter.count('L') 
    
    print(f'Heads: {H},Tails: {T},Wins: {W}, Losses: {L}')
    if W > L:
        print('\nUser won for the chosen number times the coin was flipped and die was rolled ')
    elif W == L:
        print('\nit is a draw, please try again')
    else:
        print('\nYou lost the game')
        
        
if __name__ =='__main__':
     die_flip()
    
            
    





    
 

           
           
           
               
        

    
     
    