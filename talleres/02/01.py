n=int(input())
raw_values = input().split()
accum = int(raw_values[-1])
for i in range(n-2, -1, -1):
    current = int(raw_values[i])
    accum+=current
    print(accum)

