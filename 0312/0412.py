'''replay = 'y'

while replay == 'y':
    print('hello')
    replay = input('입력:')'''

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')