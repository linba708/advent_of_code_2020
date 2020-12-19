import itertools

def add_coordinates(a,b):
    return tuple(sum(x) for x in zip(a,b))

def get_neighbor(point, neighbor_cube_set):
    return {add_coordinates(point, cube) for cube in neighbor_cube_set}

initial_set = set()
with open('data/day17.txt') as data:
    for y, line in enumerate(data.readlines()):
        initial_set = initial_set | {(x,y,0,0) for x, active in enumerate(line.strip()) if active == '#' }

origin = (0,0,0,0)
neighbor_cubes = set(itertools.product((-1,0,1),repeat=len(origin))).difference({origin})
active_set = initial_set

for i in range(1,7): 
    
    still_active = {point for point in active_set if len(get_neighbor(point, neighbor_cubes) & active_set) in (2,3)}
    all_neighbors = set().union(*(get_neighbor(cube, neighbor_cubes) for cube in active_set))
    new_active = {point for point in all_neighbors if len(get_neighbor(point, neighbor_cubes) & active_set) == 3}
    active_set = still_active | new_active
print(len(active_set))
