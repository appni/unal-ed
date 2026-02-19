def image(text):
    chars = list(text)
    for i in range(len(chars)//2):
        aux = chars[i]
        chars[i] = chars[-i-1]
        chars[-i-1] = aux
    return ''.join(chars)
    
def m_to_m2(text):
    chars = list(text)
    for i in range(1, len(chars), 2):
        aux = chars[i-1]
        chars[i-1] = chars[i]
        chars[i] = aux
    return ''.join(chars)

def m2_to_m(text):
    chars = list(text)
    for i in range(0, len(chars)-1, 2):
        aux = chars[i]
        chars[i] = chars[i+1]
        chars[i+1] = aux
    return ''.join(chars)

def decript(txt):
    return m_to_m2(image(txt))

c = int(input())
rows = []
for _ in range (c):
    rows.append(input().replace(' ', ''))
for row in rows:
    print(decript(row))