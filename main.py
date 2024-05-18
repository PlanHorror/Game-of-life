import ita
def list_input_txt():
    a = open('input.txt', 'r')
    map = []
    data = a.read().split('\n')
    for i in range(len(data)):
        data[i] = data[i].split(' ')
        for j in range(len(data[i])):
            if data[i][j] == '':
                data[i].pop(j)
        for j in range(len(data[i])):
            data[i][j] = data[i][j].replace(',', '').replace(']', '').replace('[', '').replace(' ', '')
            data[i][j] = int(data[i][j])
    map = list(filter(None, data))
    return map
def count_neighbours(map, x, y):
    count = 0
    if x - 1 >= 0 and y - 1 >= 0:
        if map[x - 1][y - 1] == 1:
            count += 1
    if x - 1 >= 0:
        if map[x - 1][y] == 1:
            count += 1
    if y - 1 >= 0:
        if map[x][y - 1] == 1:
            count += 1
    if y + 1 < len(map[x]):
        if x - 1 >= 0:
            if map[x - 1][y + 1] == 1:
                count += 1
        if map[x][y + 1] == 1:
            count += 1
    if x + 1 < len(map):
        if y - 1 >= 0:
            if map[x + 1][y - 1] == 1:
                count += 1
        if map[x + 1][y] == 1:
            count += 1
    if x + 1 < len(map) and y + 1 < len(map[x]):
        if map[x + 1][y + 1] == 1:
            count += 1
    return count
def lifegame_rule(cur, neighbours):
    if cur == 1:
        if neighbours < 2:
            return 0
        elif neighbours == 2 or neighbours == 3:
            return 1
        elif neighbours > 3:
            return 0
    elif cur == 0:
        if neighbours == 3:
            return 1
        else:
            return 0
    else:
        return -1
def lifegame_step(map, step):
    results = ita.array.make1d(step)
    for i in range(step):
        new_map = ita.array.make2d(len(map), len(map[0]))
        for x in range(len(map)):
            for y in range(len(map[x])):
                neighbours = count_neighbours(map, x, y)
                new_map[x][y] = lifegame_rule(map[x][y], neighbours)
        map = new_map
        results[i] = map
    return results
     
def main():
    list_input_txt()
    map = list_input_txt()
    ani = lifegame_step(ita.lifegame_acorn(), 30)
    # ita.plot.animation_show(ani)
    ita.plot.image_show(ita.lifegame_acorn())
def draw_


if __name__ == '__main__':
    main()

    
