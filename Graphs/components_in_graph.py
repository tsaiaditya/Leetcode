'''
There are 2n values to represent nodes in a graph. They are divided into two sets G and B. Each set has exactly N values. 
Set G is represent by G1 to Gn.  can contain any value between 1 to N(inclusive). 
Set B is represented by B1 to Bn. B can contain any value between N+1 to 2N (inclusive). Same value can be chosen any number of times.

Here (G1,B1),(G2,B2),...(Gn,Bn) represents the edges of the graph.

Your task is to print the number of vertices in the smallest and the largest connected components of the graph.

Note Single nodes should not be considered in the answer.

Sample Input

5
1 6 
2 7
3 8
4 9
2 6
Sample Output

2 4
'''
class UF:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)
        
    def _parent(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
    
    def _size(self, a):
        return self.size[self._parent(a)]
    
    def merge(self, a, b):
        a, b = self._parent(a), self._parent(b)
        if a != b:
            if self._size(a) < self._size(b):
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

    def __repr__(self):
        return self.parent.__str__() + "\n" + self.size.__str__()

T = int(input())
uf = UF(T * 2)
for _ in range(T):
    uf.merge(*map(int, input().split()))
print(min(sz for node, sz in zip(range(T * 2 + 1), uf.size) if sz != 1 and node == uf._parent(node)), end=" ")
print(max(uf.size))
