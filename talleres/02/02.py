n = int(input())
game = []
for _ in range (3):
    row = [int(x) for x in input().split(',')]
    game.append(row)
points = [0,0,0]
current = 3
is_even = lambda x : x % 2 == 0
for i in range(n):
    current = current + 1 if current < 2 else 0
    round = [row[i] for row in game]
    if is_even(round[current]) :
        points[current] += 1 if is_even(sum(round)) else 0
    else: 
        points[current] += 1 if not is_even(sum(round)) else 0
print(f'SO:{points[0]}, LAR:{points[1]}, IS:{points[2]}')