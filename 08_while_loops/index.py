c = 0
while c < 5:
    print(c)
    c = c + 1

print("-"*10)

d = 0
while d < 5:
    print(d)
    if d == 3:
        break
    d = d + 1

print("-"*10)

c = 0
while c < 5:
    c = c + 1
    if c == 2:
        continue
    print(c)

print("-"*10)

c = 0
while c < 5:
    c = c + 1
    if c == 3:
        pass
    print(c)
