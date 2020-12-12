# ## Part one
# def print_dict(seat_dict, rows, cols):
#     for i in range(rows):
#         print(' '.join([seat_dict[(i, j)] for j in range(cols)]))
#     print('_______________')

# def get_adjecent_seats(point, seat_dict):
#     y, x = point
#     return [seat_dict[(i, j)] for j in range(x - 1, x + 2) for i in range(y - 1, y + 2) if (i, j) in seat_dict and (i, j) != point]
    
# def change_seat(point, seat_dict):
#     seat = seat_dict[point]
#     if seat == '.':
#         return '.'
#     elif seat == 'L' and get_adjecent_seats(point, seat_dict).count('#') == 0:
#         return '#'
#     elif seat == '#' and get_adjecent_seats(point, seat_dict).count('#') >= 4:
#         return 'L'
#     else:
#         return seat
    



# #read data
# rows = []
# with open('data/day11.txt') as reader:
#     rows = [list(line.strip()) for line in reader.readlines()]

# seat_map = {}
# for i, row in enumerate(rows):
#     seat_map.update({(i, j): col for j, col in enumerate(row)})

# len_rows = len(rows)
# len_columns = len(rows[0])


# print_dict(seat_map, len_rows, len_columns)

# new_seat_man = seat_map
# while True:
#     seat_map = new_seat_man.copy()
#     new_seat_man = {point: change_seat(point, seat_map) for point in seat_map}
#     if seat_map == new_seat_man:
#         break


# print_dict(new_seat_man, len_rows, len_columns)
# print([seat for seat in new_seat_man.values()].count('#'))

## part two

## Part one
def print_dict(seat_dict, rows, cols):
    for i in range(rows):
        print(' '.join([seat_dict[(i, j)] for j in range(cols)]))
    print('_______________')

def get_adjecent_seats(point, seat_dict):
    y, x = point
    return [seat_dict[(i, j)] for j in range(x - 1, x + 2) for i in range(y - 1, y + 2) if (i, j) in seat_dict and (i, j) != point]
    
def sees_occupied_seat(point, seat_dict, threshold):
    y, x = point
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    found = 0
    for direction in directions:
        j, i = direction
        point_to_check = (y + j, x + i)
        while point_to_check in seat_dict:
            # print('checking', point, point_to_check)
            current_seat = seat_dict[point_to_check]
            found += 1 if current_seat == '#' else 0
            if found > threshold:
                return True
            if current_seat == 'L' or current_seat == '#':
                break
            y_1, x_1 = point_to_check
            point_to_check = (y_1 + j, x_1 + i)
    return False

    
def change_seat(point, seat_dict):
    seat = seat_dict[point]
    if seat == '.':
        return '.'
    elif seat == 'L' and not sees_occupied_seat(point, seat_dict, 0):
        return '#'
    elif seat == '#' and  sees_occupied_seat(point, seat_dict, 4):
        return 'L'
    else:
        return seat
    



#read data
rows = []
with open('data/day11.txt') as reader:
    rows = [list(line.strip()) for line in reader.readlines()]

seat_map = {}
for i, row in enumerate(rows):
    seat_map.update({(i, j): col for j, col in enumerate(row)})

len_rows = len(rows)
len_columns = len(rows[0])

print_dict(seat_map, len_rows, len_columns)
loops = 0
new_seat_man = seat_map
while True:
    seat_map = new_seat_man.copy()
    new_seat_man = {point: change_seat(point, seat_map) for point in seat_map}
    loops += 1
    if seat_map == new_seat_man:
        break


# print_dict(new_seat_man, len_rows, len_columns)
print([seat for seat in new_seat_man.values()].count('#'))
