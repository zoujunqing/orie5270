import heapq

def create_edges(line):
    edges = {}
    paren = 0
    tup = "("
    for i in line:
        if i == '(':
            paren += 1
        elif i == ')':
            paren += -1
            tup += ')'
            tup_eval = eval(tup)
            edges[float(tup_eval[0])] = float(tup_eval[1])
            tup = '('
        elif paren == 1:
            tup += i
    return edges

def create_graph(name_txt_file):
    file = open(name_txt_file, "r")
    lines = file.readlines()
    graph = dict()
    line_len = len(lines)
    if line_len % 2 == 0:
        for i in range(line_len):
            if i % 2 == 1:
                graph[float(lines[i-1])] = create_edges(lines[i])
    else:
        for i in range(line_len):
            if i % 2 == 1:
                graph[float(lines[i-1])] = create_edges(lines[i])
        graph[float(lines[-1])] = {}
    return graph

def find_shortest_path(name_txt_file, source, destination):
    graph = create_graph(name_txt_file)
    S = set()
    F = [(0, source)]
    heapq.heapify(F)
    d = {source: 0}
    p = {}
    while len(F) > 0:
        # f is the item with smallest d from F
        f = heapq.heappop(F)
        S.add(f[1])
        for item in graph[f[1]].keys():
            if item not in S and item not in [i[1] for i in F]:
                d[item] = d[f[1]]+graph[f[1]][item]
                heapq.heappush(F, (d[item], item))
                p[item] = f[1]
            elif d[f[1]]+graph[f[1]][item] < d[item]:
                d[item] = d[f[1]]+graph[f[1]][item]
                p[item] = f[1]
    # print path
    path = [destination]
    if destination not in S:
        d[destination] = None
        path = None
    else:
        path = [destination]
        trace_back = p[destination]
        while trace_back and source != trace_back:
            path.append(trace_back)
            trace_back = p[trace_back]
        path.append(trace_back)
        path = path[::-1]
    return(d[destination], path)

if __name__ == '__main__':
    print(find_shortest_path('find_shortest_path.txt', 1, 4))