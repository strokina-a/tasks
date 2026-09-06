import numpy as np
with open ('input6.txt', 'r+') as file:
    f = file.readlines()
    b = int(f[2])
    s = [int(i, b) for i in f[0][:-1].split()]
    a = 0
    print(f[1][0])
    if f[1][0] == '+':
        a = np.sum(s)
    elif f[1][0] == '*':
        a = np.prod(s)
    elif f[1][0] == '-':
        a = s[0] - (np.sum(s[1:]))
    print(a)
with open ('output6.txt', 'w+') as file:
    file.write(str(a))