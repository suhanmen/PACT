#To find the minimum path of length k in the grid
def minPath(grid, k):
    #Finding the size of the grid
    n = len(grid)
    #Intializing start, end, ans and visited
    start = [(grid[i][0], i, 0) for i in range(n)]
    end = [(grid[i][n-1], i, n-1) for i in range(n)]
    ans = None
    visited = set()
    #Defining dfs function
    def dfs(a, idx):
        #If the index is equal to k
        if idx == k:
            #If ans == None or the value of ans is greater than a
            nonlocal ans
            if ans == None or ans > a:
                ans = a
            return
        #If ans != None and the value of ans is less than or equal to a
        if ans != None and ans <= a:
            return
        #For each element in start and end
        for i, j, u in start + end:
            #If (i, j) is not in visited
            if (i, j) not in visited:
                #Adding (i, j) in visited
                visited.add((i, j))
                #If idx == k-1
                if idx == k-1:
                    #Calling dfs with a + [i] as parameter
