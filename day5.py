
def get_row(line):
    return int(line[0:7].replace('F','0').replace('B', '1'),2)

def get_column(line):
    return int(line[7:].replace('L','0').replace('R', '1'),2)

def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)

max_seat = 0
seat_ids = []
with open('data/day5.txt') as reader:
    for line in reader.readlines():
        line = line.strip()
        row = get_row(line)
        column = get_column(line)
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
        if seat_id > max_seat:
            max_seat = seat_id
        # print(f'{line} row {row}, column {column}, seat ID {seat_id}')
seat_ids.sort()
for prev,item,next in neighborhood(seat_ids):
    if prev is not None and next is not None and  prev + 2 == item:
        print(prev,prev +1, item)
    
print(max_seat)
