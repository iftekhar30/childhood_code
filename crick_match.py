import crick_innings
import print_blocker
import time

print("Team 1 batting.....")
t1 = crick_innings.play_innings(99999)
print("Score:", t1)

target = int(t1.split('/')[0]) + 1

print("Target:", target)
print("")

print("Team 2 batting.....")
t2 = crick_innings.play_innings(target)
print("")
print("Team 1:", t1)
print("Target:", target)
print("Team 2:", t2)

run_chased = int(t2.split('/')[0])


if target - 1 == run_chased:
    print("Draw")
elif target <= run_chased:
    print(f"Team 2 won by {5 - int(t2.split('/')[1])} wickets")
elif target > run_chased:
    print(f"Team 1 won by {target - run_chased} runs")