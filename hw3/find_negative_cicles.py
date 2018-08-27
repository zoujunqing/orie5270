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

def find_negative_cicles(name_txt_file):
    graph = create_graph(name_txt_file)
    # initialize
    d = {}
    p = {}
    for vertex in graph:
        d[vertex] = float('Inf')
        p[vertex] = None
    d[0] = 0
    
    # relax
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                if d[v] > d[u] + graph[u][v]:
                    d[v] = d[u] + graph[u][v]
                    p[v] = u
    # check and find negative cycle
    for u in graph:
        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]:
                print("Negative cycle exist:")
                neg_cycle = [u]
                start = u
                trace_back = p[start]
                while start != trace_back and trace_back:
                    neg_cycle.append(trace_back)
                    trace_back = p[trace_back]
                neg_cycle.append(trace_back)
                neg_cycle = neg_cycle[::-1]
                return(neg_cycle)

if __name__ == '__main__':
    print(find_negative_cicles('find_negative_cicles.txt'))