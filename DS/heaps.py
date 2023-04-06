import heapq

H = [2, 1, 5, 4, 7]

# Heapify
heapq.heapify(H)
print(H)

# Push
heapq.heappush(H, 0)
print(H)

# Pop
heapq.heappop(H)
print(H)

# Replace
heapq.heapreplace(H, 2)
print(H)
