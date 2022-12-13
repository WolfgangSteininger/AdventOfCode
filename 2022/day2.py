# Rock      1 0  X   A
# Paper     2 1  Y   B
# Scissors  3 2  Z   C
# lost 0
# draw 3
# won  6

# symbol    lost   draw   won
# 0     +2    2       0    +1   1
# 1         0       1       2
# 2         1       2       0
#
#

with open('2022/inputs/day2.txt', 'r') as f:
    lines = f.readlines()
    bets = [entry.strip().split() for entry in lines]

total = 0
lost = 0
draw = 3
won = 6

for bet in bets:
    playerA = ord(bet[0]) - ord('A')
    playerB = ord(bet[1]) - ord('X')

    counter = 0
    outcome = playerA - playerB
    outcomeStr = ""
    if (outcome == 0):
        #draw
        outcomeStr = "draw"
        counter = counter + draw
    elif (outcome == -1 or outcome == 2):
        # won
        outcomeStr = "won"
        counter = counter + won
    else:
        outcomeStr = "lost"

    # add played symbol
    counter += playerB + 1
    total += counter

    print(f"outcome:{outcomeStr}({outcome}) counter:{counter} A:{playerA} B:{playerB}")

print(f"solution 1: {total}")


### part 2
# X lose
# Y draw
# Z win
total = 0
for bet in bets:
    playerA = ord(bet[0]) - ord('A')
    counter = 0

    if (bet[1] == 'X'):
        outcomeStr = "lost"
        counter = counter + lost + (playerA + 2)%3 + 1
    elif (bet[1] == 'Y'):
        outcomeStr = "draw"
        counter = counter + draw + playerA + 1
    elif (bet[1] == 'Z'):
        outcomeStr = "won"
        counter = counter + won + (playerA + 1)%3 + 1

    total += counter
    print(f"outcome:{outcomeStr}({bet[1]}) counter:{counter} A:{bet[0]}")

print(f"solution 2: {total}")