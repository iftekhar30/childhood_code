import random
import sys
import time


class CricketGame:
    def __init__(self):
        self.team1_score = 0
        self.team2_score = 0
        self.target_score = 0

    def play_shot(self):
        run = 0
        results = [0, 1, 2, 3, 4, 6, 'no', 'wide', 'out']
        result = random.choice(results)
        if isinstance(result, int):
            run += result
        elif isinstance(result, str):
            if result == 'no' or result == 'wide':
                run += 1

        return result, run

    def play_innings(self, target):
        score = 0
        wickets = 0
        overs = 5

        for i in range(overs):
            print("Over:", i)
            time.sleep(1)
            balls = 0

            while balls != 6:
                if wickets == 5:
                    print("All out")
                    print("Score:", score)
                    return f"{score}/{wickets}"

                if score >= target:
                    return f"{score}/{wickets}"

                shot = self.play_shot()
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

                score += shot[1]
                print('Score:', score)
                print("Wickets:", wickets)

            print("")

        return f"{score}/{wickets}"


if __name__ == '__main__':
    game = CricketGame()

    print("Team 1 batting.....")
    t1 = game.play_innings(99999)
    print("Score:", t1)

    game.target_score = int(t1.split('/')[0]) + 1

    print("Target:", game.target_score)
    print("")

    print("Team 2 batting.....")
    t2 = game.play_innings(game.target_score)
    print("")
    print("Team 1:", t1)
    print("Target:", game.target_score)
    print("Team 2:", t2)

    run_chased = int(t2.split('/')[0])

    if game.target_score - 1 == run_chased:
        print("Draw")
    elif game.target_score <= run_chased:
        print(f"Team 2 won by {5 - int(t2.split('/')[1])} wickets")
    elif game.target_score > run_chased:
        print(f"Team 1 won by {game.target_score - run_chased} runs")
