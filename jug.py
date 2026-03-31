from collections import deque 

jug1 = 5
jug2 = 3
target = 2

visited = set()

def dfs(x,y):
    if(x,y) in visited:
        return
    visited.add((x,y))

    print(x,y)

    if x == target or y == target:
        print("target Reched!")
        return
    #Fill jug1
    dfs(jug1,y)

    #Fill jug2
    dfs(x,jug2)

    #Empty jug1
    dfs(0,y)

    #Empty jug2
    dfs(x,0)

    #pour jug -> jug2
    pour = min(x,jug2-y)
    dfs(x-pour,y+pour)

    #pour jug2 -> jug1
    pour = min(y,jug1-x)
    dfs(x+pour,y-pour)

print("steps:")
dfs(0,0)
    


