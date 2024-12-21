import string

from utils import PriorityQueue


def init_map(map_str: string):
    str2cost = {
        # plain, cost = 1
        '0': 1,
        # wall, cost = infinity
        '1': float('inf'),
        # swamp, cost = 5
        '2': 5,
        # also wall, cost = infinity
        '3': float('inf')
    }
    # 初始化一个50*50的二维数组
    cost_map = [[float('inf') for _ in range(50)] for _ in range(50)]
    # 遍历map_str，将每个点的cost填入cost_map
    for i in range(0, 2500):
        x = i % 50
        y = i // 50
        cost_map[y][x] = {'x': x, 'y': y, 'cost': str2cost[map_str[i]]}

    return cost_map


def get_neighbors(cost_map, x, y):
    neighbors = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < 50 and 0 <= y + dy < 50:
                neighbors.append(cost_map[y + dy][x + dx])

    return neighbors


def point2key(point):
    return f'{point["x"]},{point["y"]}'


def bfs_fill(cost_map, gx: int, gy: int):
    # 初始化一个二维数组，用于记录每个点的到goal的总cost
    cost_total = [[float('inf') for _ in range(50)] for _ in range(50)]
    # 初始化一个优先队列
    q = PriorityQueue()
    # 初始化一个dict，用于记录每个点是否被访问过
    visited = {}
    # 将point放入优先队列，标记为已访问
    goal = cost_map[gy][gx]
    q.enqueue({'point': goal, 'priority': 0})
    visited[point2key(goal)] = True
    # 初始化goal的cost为0
    cost_total[gy][gx] = 0
    while not q.is_empty():
        # 取出优先队列的头部元素
        cur = q.dequeue()
        # 取出当前点的坐标
        x, y, cur_cost = cur['point']['x'], cur['point']['y'], cur['priority']
        # 获取当前点的邻居
        neighbors = get_neighbors(cost_map, x, y)
        for neighbor in neighbors:
            # 如果邻居未被访问过
            if neighbor['cost'] < float('inf') and not visited.get(point2key(neighbor)):
                # 将邻居放入优先队列
                q.enqueue({'point': neighbor, 'priority': cur_cost + neighbor['cost']})
                # 标记邻居为已访问
                visited[point2key(neighbor)] = True
                # 更新邻居的cost
                cost_total[neighbor['y']][neighbor['x']] = cur_cost + neighbor['cost']

    return cost_total


def get_best_neighbor(cost_grid, x, y):
    min_cost = float('inf')
    best_neighbor = None
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < 50 and 0 <= y + dy < 50:
                if cost_grid[y + dy][x + dx] < min_cost:
                    min_cost = cost_grid[y + dy][x + dx]
                    best_neighbor = (x + dx, y + dy)

    return best_neighbor


def get_direction(dx, dy):
    return dy * 3 + dx + 4


def config_direction(cost_grid):
    dir_grid = [['⨂' for _ in range(50)] for _ in range(50)]
    goal_symbol = '★'
    dir_symbol = ['↖', '↑', '↗', '←', '?', '→', '↙', '↓', '↘']
    for y in range(0, 50):
        for x in range(0, 50):
            if cost_grid[y][x] == float('inf'):
                continue
            elif cost_grid[y][x] == 0:
                dir_grid[y][x] = goal_symbol
                continue
            best_neighbor = get_best_neighbor(cost_grid, x, y)
            # 取出最佳邻居的坐标
            dx, dy = best_neighbor[0] - x, best_neighbor[1] - y
            dir_idx = get_direction(dx, dy)
            dir_grid[y][x] = dir_symbol[dir_idx]

    return dir_grid


def config_direction_idx(cost_grid):
    dir_grid = [[9 for _ in range(50)] for _ in range(50)]
    for y in range(0, 50):
        for x in range(0, 50):
            if cost_grid[y][x] == float('inf'):
                continue
            elif cost_grid[y][x] == 0:
                continue
            best_neighbor = get_best_neighbor(cost_grid, x, y)
            dx, dy = best_neighbor[0] - x, best_neighbor[1] - y
            dir_idx = get_direction(dx, dy)
            dir_grid[y][x] = dir_idx

    return dir_grid
