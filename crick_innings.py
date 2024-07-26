import random
import sys
import time



def play_shot():
    run = 0
    results = [0, 1, 2, 3, 4, 6, 'no', 'wide', 'out']
    result = random.choice(results)
    if type(result) == int:
        run += result
    elif type(result) == str:
        if (result == 'no' or result == 'wide'):
            run += 1

    return result, run


def play_innings(target):
    score = 0
    wickets = 0
    over = 5
    for i in range(over):
        print("Over: ",i)
        time.sleep(1)
        balls = 0
        while balls != 6:
            if wickets == 5:
                print("All out")
                print("score: ", score)
                return f"{score}/{wickets}"
            if score >=  target:
                return f"{score}/{wickets}"
            shot = play_shot()
            balls += 1
            if shot[0] == 'no':
                balls -= 1
                if balls == 0:
                    balls += 1
            elif shot[0] == 'wide':
                balls -= 1    
                if balls == 0:
                    balls += 1
            elif shot[0] == 'out':
                wickets += 1
                
            if shot[0] == 6:
                    print(f"{i}.{balls}", 'six')
            elif shot[0] == 4:
                    print(f"{i}.{balls}", 'four')
            else:
                print(f"{i}.{balls}", shot[0])
            score+= shot[1]
            print('score:', score)
            print("wickets:", wickets)
        
        print("")
    
    return f"{score}/{wickets}" 



