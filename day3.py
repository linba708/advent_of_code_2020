
ski_map = []
with open('data/day3.txt') as reader:
    for line in reader.readlines():
        ski_map.append([char for char in line.strip()])

strategies = [{"x": 1, "y":1}, {"x": 3, "y":1}, {"x": 5, "y":1} , {"x": 7, "y":1}, {"x": 1, "y":2}]
trees_array = []
tree_multi = 1

for strategy in strategies:
    trees = 0
    x = 0
    y = 0
    while y < len(ski_map):
        if ski_map[y][x] == '#': trees += 1
        
        x += strategy["x"]
        if x >= len(ski_map[y]):
            x -= len(ski_map[y])
        y += strategy["y"]
    trees_array.append(trees)
    tree_multi *= trees
print(trees_array)
print(tree_multi)