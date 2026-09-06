import numpy as np
with open ('input.txt', 'r+') as file:
    f = file.readlines()
    s = [int(i) for i in f[0][:-1].split()]
    a = 0
    if f[1] == '+':
        a = np.sum(s)
    elif f[1] == '*':
        a = np.prod(s)
    elif f[1] == '-':
        a = s[0] - (np.sum(s[1:]))
    print(a)
with open ('output.txt', 'w+') as file:
    file.write(str(a))