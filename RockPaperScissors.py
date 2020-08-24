import random, sys
print("ROCK, PAPER, SCISSORS")
moves = {'r': "ROCK", 'p': "PAPER", 's': "SCISSORS"}
rand_map = ['r', 'p', 's']
results = {'wins': 0, 'loss': 0, 'ties': 0}

while True:
    
    #when avoiding the end comma, instead of trying to remove the last one, put the commas
    #at the front of the items, and attempt to remove the first one instead
    format = "%d %s"
    for key, value in results.items():
        print(format %(value, key), end = "")
        format = ", %d %s"

    print("\nEnter your move: (r)ock, (p)aper, (s)cissors, or (q)uit")

    while True: #player input loop, to check if input is valid
        player_move = input().lower()

        if player_move == 'q':
            sys.exit()
            
        #To ensure valid input, check the input is equal to the valid input instead of not equal
        if player_move == 'p' or player_move == 'r' or player_move == 's':
            break

    print(moves[player_move] + " versus...")

    computer_move = rand_map[random.randint(0, 2)]
    print(moves[computer_move])

    #assuming the one on the right is the winning one, we increment one of the users and mod 3
    #if the result is equal to the other user, it means the original user was on the left of the other
    #user, thus the right user wins
    if player_move == computer_move:
        print("It's a tie!")
        results['ties'] += 1
        
    elif rand_map.index(computer_move) == (rand_map.index(player_move) + 1) % 3 :
        print("You Lose!")
        results['loss'] += 1

    else:
        print("You Win!")
        results['wins'] += 1
        
    

    

    

    
    
