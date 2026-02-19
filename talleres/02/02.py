n = int(input())
game = []
for _ in range (3):
    row = [int(x) for x in input().split(',')]
    game.append(row)
points = [0,0,0]
is_even = lambda x : x % 2 == 0
for i in range(n):
    round = [row[i] for row in game]
    sum_is_even = is_even(sum(round))
    for index, val in enumerate(round):
        points[index] += 1 if is_even(val) and sum_is_even else 0     
        points[index] += 1 if not is_even(val) and not sum_is_even else 0     
   
print(f'SO:{points[0]}, LAR:{points[1]}, IS:{points[2]}')