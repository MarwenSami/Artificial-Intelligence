import pprint
BLOCK_DIM = 25
TIME = 250
def create_graph(matrix):
    height = len(matrix)
    width = len(matrix[0])
    graph = {(i,j): [] for j in range(width) for i in range(height) if not matrix[i][j]}
    for row, col in graph.keys():
        if row < height -1 and not matrix[row +1][col]:
            graph[(row, col)].append(("S", (row+1, col)))
            graph[(row+1, col)].append(("N", (row, col)))
        if col < width -1 and not matrix[row][col+1]:
            graph[(row,col)].append(("E", (row, col+1)))
            graph[(row, col+1)].append(("W", (row, col)))
    return graph

def draw_step(mCanvas, x, y):
    def draw(mCanvas, x,y):
        mCanvas.create_oval((x*BLOCK_DIM)+BLOCK_DIM/4, (y*BLOCK_DIM)+BLOCK_DIM/4, (x*BLOCK_DIM)+(3*BLOCK_DIM/4), (y*BLOCK_DIM)+(3*BLOCK_DIM/4), fill="cyan")
        mCanvas.update()
    mCanvas.after(TIME, draw(mCanvas, x, y))
    return True

def draw_path(mCanvas, start, path):
    #clear_path(mCanvas)
    y,x  = start
    def draw(mCanvas, x, y):
        print("Drawing x: " +str(x)+" and y:"+str(y))
        mCanvas.create_rectangle(x*BLOCK_DIM, y*BLOCK_DIM, (x+1)*BLOCK_DIM, (y+1)*BLOCK_DIM, fill="red")
        mCanvas.update()

    mCanvas.after(TIME, draw(mCanvas, x, y))
    for i in path:
        if i == "E":
            x = x+1
        if i == "W":
            x= x-1
        if i == "S":
            y= y+1
        if i == "N":
            y= y -1
        mCanvas.after(TIME, draw(mCanvas, x, y))
    return True

def clear_path(mCanvas):
    mCanvas.create_rectangle(c*BLOCK_DIM, l*BLOCK_DIM, (c+1)*BLOCK_DIM, (l+1)*BLOCK_DIM, fill="green")

def heuristic(start, end):
    return abs(start[0]-end[0]) + abs(start[1] - end[1])
def a_star(mCanvas, graph, start, exit):
    from heapq import heappop, heappush
    q = []
    heappush(q, (heuristic(start, exit), 0, "", start))
    visited = set()
    while q:
        _,cost, path, current = heappop(q)
        if current == exit:
            draw_step(mCanvas, current[1], current[0])
            draw_path(mCanvas, start, path)
            pprint.pprint(path)
            return path
        if current in visited:
            continue
        visited.add(current)
        draw_step(mCanvas, current[1], current[0])
        for direction, neighbour in graph[current]:
            heappush(q, (cost+ heuristic(neighbour, exit), cost +1, path+direction, neighbour))

    return None

def best_first_search(mCanvas, graph, start, exit):
    from heapq import heappop, heappush
    q = []
    heappush(q, (heuristic(start, exit), 0, "", start))
    visited = set()
    while q:
        _,cost, path, current = heappop(q)
        if current == exit:
            draw_step(mCanvas, current[1], current[0])
            draw_path(mCanvas, start, path)
            pprint.pprint(path)
            return path
        for direction, neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                draw_step(mCanvas, current[1], current[0])
                heappush(q, (cost+heuristic(neighbour, exit), cost+1, path+direction, neighbour))
        visited.add(current)

    return None
def uniform_cost(mCanvas, graph, start, exit):
    from heapq import heappop, heappush
    q = []
    heappush(q, (0, "", start))
    cost_so_far = {}
    while q:
        cost, path, current = heappop(q)
        if current == exit:
            draw_step(mCanvas, current[1], current[0])
            draw_path(mCanvas, start, path)
            pprint.pprint(path)
            return path
        for direction, neighbour in graph[current]:
            new_cost = cost + 1
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                draw_step(mCanvas, current[1], current[0])
                heappush(q, (new_cost, path+direction, neighbour))
    return None
