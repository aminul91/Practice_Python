
listA = []
path = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def path_f(temp_list,graph):
    for eachnn in temp_list:
        if len(graph[eachnn])!=0:
            return graph[eachnn]

def graph_f(graph, node):
    queue.append(node)
    path.append(node)
    while len(graph[node])!=0:
        listA=[]
        listA.append(node)
        s= graph[node].pop(0)
        path.append(s)
        listA.append(s)
        mm = path_f(s,graph)
        listA.append(mm[0])
        print(listA)
    
# Driver Code
graph = {
  'A' : ['B','C'],
  'B' : ['D'],
  'C' : ['D'],
  'D' : [],
 
}
graph_f( graph, 'A')