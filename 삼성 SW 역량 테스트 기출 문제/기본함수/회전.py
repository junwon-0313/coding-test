def rotate(graph, opt):
    n, m = len(graph), len(graph[0])
    if opt==1 or opt==3:
        new_graph = [[-1]*n for _ in range(m)]
    else:
        new_graph = [[-1]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if opt ==1: # 시계방향 90도 회전
                new_graph[y][-x-1] = graph[x][y]
            elif opt==2: # 180도 회전
                new_graph[-1-x][-1-y] = graph[x][y]
            elif opt==3:
                new_graph[-1-y][x] = graph[x][y]

    return new_graph

def print_g(graph):
    n, m = len(graph), len(graph[0])
    for x in range(n):
        for y in range(m):
            print(graph[x][y], end =' ')
        print()

graph = [[1,2,3],[4,5,6]]
print_g(graph)
print('ROTATE 90')
print_g(rotate(graph,1))
print('ROTATE 180')
print_g(rotate(graph,2))
print('ROTATE 270')
print_g(rotate(graph,3))
