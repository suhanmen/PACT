#We can solve this problem using a modified BFS.
#We will start BFS from each cell and keep track of the shortest path of length k 
# found so far. We can use a set to keep track of the visited cells in each path.

from queue import Queue

def minPath(grid, k):
    
    #initialize required variables
    n = len(grid)
    candidates = []
    visited = set()
    res = []

    for i in range(n):
        for j in range(n):
            
            #start BFS from this cell
            q = Queue()
            q.put((grid[i][j],[i,j],0))
            visited.add((i,j))
            
            while not q.empty():
                node = q.get()
                currval, currpos, currlen = node[0], node[1], node[2]
                
                #if path of length k is found
                if currlen == k:
                    candidates.append((currval, res))
                    res = []
                    break
                
                #iterate over all neighbors and add them to queue
                for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    x, y = currpos[0]+dx, currpos[1]+dy
                    if x>=0 and x<n and y>=0 and y<n and (x,y) not in visited:
                        visited.add((x,y))
                   
