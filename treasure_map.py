row1 = ['⬜️', '⬜️', '⬜️']

row2 = ['⬜️', '⬜️', '⬜️']

row3 = ['⬜️', '⬜️', '⬜️' ]

treasure_map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

treasure_pos = input('Where do you want to put your tresure? ')

if(len(treasure_pos) != 2):
    print('Invalid positioning')
else:
    row = int(treasure_pos[0]) - 1
    col = int(treasure_pos[1]) - 1
    treasure_map[row][col] = 'X '

print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}")