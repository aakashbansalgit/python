def func(grid):
    #return minimum health score
    i,j = 0,0
    N = len(grid)
    M = len(grid[0])
    health = 200*200*1000
    curhealth = 0
    def dfs(i,j,N,M,health,curhealth):
        if i<0 or i>=N or j<0 or j>=M:
            return
        curhealth = curhealth+grid[i,j]
        if i == N-1 amd j == M-1:
            health = min(health,curhealth)
        k = dfs(i+1,j,N,M,health,curhealth)
        l = dfs(i+1,j,N,M,health,curhealth)
        if k:
            health = min(health,k)
        if l:
            health = min(health,l)
        return health
    health = dfs(i,j,N,M,vis,health,curhealth)
    if health:
        ans = 1-health
    else:
        ans = health
    return ans