'''
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.
'''
class Solution:
    def canVisitAllRooms(self, rooms):
        memo = [0 for _ in range(len(rooms))]
        def dfs(cur):
            memo[cur] = 1
            for i in rooms[cur]:
                if not memo[i]:
                    dfs(i)
        dfs(0)
        return all(memo)
st,rooms = "",[]
for i in input():
    # temp = []
    if(i == '['):
        st = ""
    elif(i == ']'):
        try:
            temp = list(map(int,st.split(',')))
        except:
            temp = [0]
        rooms.append(temp)
    else:
        st+=i
rooms = rooms[:len(rooms)-1]
s = Solution()
print(s.canVisitAllRooms(rooms))