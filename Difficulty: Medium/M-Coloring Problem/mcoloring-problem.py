#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def isSafe(node, color, graph, n, col):
    for j in range(n):
        if graph[j][node] == 1 and color[j] == col:
            return False
    return True

def solve(node, color, k, V, graph):
    if node == V:
        return True

    for i in range(1, k + 1):
        if isSafe(node, color, graph, V, i):
            color[node] = i  
            if solve(node + 1, color, k, V, graph):
                return True
            color[node] = 0 
    return False

def graphColoring(graph, k, V):
    color = [0] * V  
    if solve(0, color, k, V, graph):
        return 1  
    return 0 

     
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        V = int(input())
        k = int(input())
        m = int(input())
        l = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[l[cnt] - 1][l[cnt + 1] - 1] = 1
            graph[l[cnt + 1] - 1][l[cnt] - 1] = 1
            cnt += 2
        if (graphColoring(graph, k, V) == True):
            print(1)
        else:
            print(0)

        t = t - 1

# } Driver Code Ends