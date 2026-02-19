n = int(input())
chars = input().replace(' ', '').replace(',', '')
accum = ''
for i in range(n//2):
    accum += chars[i]
    accum += chars[-i-1]
if n%2 == 1:
    accum += chars[n//2]
print(accum)