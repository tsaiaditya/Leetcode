'''
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

Note: 1 <= N <= 10000
'''
import collections

class Solution:
    def sumOfDistancesInTree(self, N, edges):
        sumofdist = [0]*N
        count = [0]*N
        
        tree = collections.defaultdict(list)
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
            
        def dfs1(prev,now):
            dsum = nsum = 0
            for i in tree[now]:
                if i == prev:
                    continue
                n,d = dfs1(now,i)
                dsum += n+d
                nsum += n
            count[now] = nsum+1
            sumofdist[now] = dsum
            return count[now],sumofdist[now]
        
        dfs1(-1,0)
        
        def rootchange(prev,now):
            if now!=0:
                sumofdist[now] = sumofdist[prev]-2*count[now]+N
            for i in tree[now]:
                if i == prev:
                    continue
                rootchange(now,i)
        
        rootchange(0,0)
        
        return sumofdist

s = Solution()
print(s.sumOfDistancesInTree(6,[[0,1],[0,2],[2,3],[2,4],[2,5]]))