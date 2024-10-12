class DisjointSet:
    def __init__(self, n: int):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, node: int) -> int:
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u: int, v: int):
        ultParentU = self.find(u)
        ultParentV = self.find(v)

        if ultParentU == ultParentV:
            return

        if self.rank[ultParentU] < self.rank[ultParentV]:
            self.parent[ultParentU] = ultParentV
        elif self.rank[ultParentU] > self.rank[ultParentV]:
            self.parent[ultParentV] = ultParentU
        else:
            self.parent[ultParentV] = ultParentU
            self.rank[ultParentU] += 1

    def unionBySize(self, u: int, v: int):
        ultParentU = self.find(u)
        ultParentV = self.find(v)

        if ultParentU == ultParentV:
            return  
        if self.size[ultParentU] < self.size[ultParentV]:
            self.parent[ultParentU] = ultParentV
            self.size[ultParentV] += self.size[ultParentU] 
        else:
            self.parent[ultParentV] = ultParentU
            self.size[ultParentU] += self.size[ultParentV] 

if __name__ == "__main__":
    ds = DisjointSet(7)
    ds2 = DisjointSet(7)
    ds.unionByRank(2, 3)
    ds.unionByRank(1, 2)
    ds.unionByRank(4, 5)
    ds.unionByRank(6, 7)
    ds.unionByRank(5, 6)

    ds2.unionBySize(2, 3)
    ds2.unionBySize(1, 2) 
    ds2.unionBySize(4, 5)
    ds2.unionBySize(6, 7)
    ds2.unionBySize(5, 6)

    if ds.find(3) == ds.find(7):
        print("Same")
    else:
        print("Not Same!")
    
    if ds2.find(3) == ds2.find(7):
        print('Same')
    else:
        print('Not Same!')

    ds.unionByRank(3, 7)
    ds2.unionBySize(3, 7)

    if ds.find(3) == ds.find(7):
        print("Same")
    else:
        print("Not Same!")
    
    if ds2.find(3) == ds2.find(7):
        print('Same')
    else:
        print('Not Same!')
