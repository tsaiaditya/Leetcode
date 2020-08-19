'''
-1 - obstacle
0 - gate
INF - empty room
fill the values of the empty rooms if we can reach a gate from the room or else leave the value as inf
'''
import collections
def wallsgates(rooms):
    if not rooms or not rooms[0]:
        return
    
    m,n = len(rooms), len(rooms[0])

    gates = []
    for i in range(m):
        for j in range(n):
            if(rooms[i][j] == 0):
                gates.append((i,j))

    queue = collections.deque(gates)

    def neighbours(r,c):
        for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0<=nr<m and 0<=nc<n and rooms[nr][nc] == float("inf"):
                yield (nr,nc)

    while queue:
        r,c = queue.popleft()
        for nr, nc in neighbours(r,c):
            rooms[nr][nc] = rooms[r][c] + 1
            queue.append((nr,nc))