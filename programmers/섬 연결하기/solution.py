def solution(n, costs):
    parent = list(range(n))
    
    def find(x) :
        if parent[x] != x :
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b) :
        ra = find(a)
        rb = find(b)
        if ra == rb :
            return False
        parent[rb] = ra
        return True
    
    costs.sort(key=lambda x: x[2])
    
    total = 0
    edges = 0
    
    for a, b, cost in costs :
        if union(a, b) :
            total += cost
            edges += 1
            if edges == n - 1 :
                break
    return total