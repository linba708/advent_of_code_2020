# Part one
def move(pos, direction, val):
    y, x = pos
    if 'N' == direction:
        return (y + val, x)
    if 'S' == direction:
        return (y - val, x)
    if 'E' == direction:
        return (y, x  + val)
    if 'W' == direction:
        return (y, x - val)

def rotate(start, rot_direction, degree):
    left_right = 1 if rot_direction == 'R' else - 1
    index = round(degree / 90) * left_right
    if 'N' == start:
        return ['N', 'E', 'S', 'W'][index]
    if 'S' == start:
        return ['S', 'W', 'N', 'E'][index]
    if 'E' == start:
        return ['E', 'S', 'W', 'N'][index]
    if 'W' == start:
        return ['W', 'N', 'E', 'S'][index]
    

pos = (0,0) # y,x
direction = 'E'

#read data
with open('data/day12.txt') as reader:
    for line in reader.readlines():
        instruction = line[0]
        val = int(line.strip()[1:])
        if instruction == 'L' or instruction == 'R':
            direction = rotate(direction, instruction, val)
        elif instruction == 'F':
            pos = move(pos, direction, val)
        else:
            pos = move(pos, instruction, val)

print(pos)
x, y = pos 
print(abs(x)+abs(y))


# Part two
def moveWaypoint(pos, direction, val):
    y, x = pos
    if 'N' == direction:
        return (y - val, x)
    if 'S' == direction:
        return (y + val, x)
    if 'E' == direction:
        return (y, x  + val)
    if 'W' == direction:
        return (y, x - val)

def farward(pos, waypoint, val):
    y, x = pos
    w_y, w_x = waypoint
    return (y + w_y*val, x + w_x*val)

def rotateWaypoint(waypoint, rot_direction, degree):
    y, x = waypoint
    left_right = 1 if rot_direction == 'R' else - 1
    index = round(degree / 90) * left_right
    return [(y,x), (x, -1*y), (-1*y,-1*x), (-1*x, y)][index]

pos = (0, 0)  # y,x
waypoint = (-1, 10)

#read data
with open('data/day12.txt') as reader:
    for line in reader.readlines():
        instruction = line[0]
        val = int(line.strip()[1:])
        if instruction == 'L' or instruction == 'R':
            waypoint = rotateWaypoint(waypoint,instruction, val)
        elif instruction == 'F':
            pos = farward(pos, waypoint, val)
        else:
            waypoint = moveWaypoint(waypoint, instruction, val)
        # print(instruction, val,pos, waypoint)

print(pos)
x, y = pos 
print(abs(x)+abs(y))

# to high 

# (35546, -89795)
# 125341