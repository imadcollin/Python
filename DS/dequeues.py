import collections

dequeue = collections.deque([1,2,3])

print(dequeue)

# Left 
dequeue.appendleft(4)
print(dequeue)
dequeue.popleft()

# Right 
dequeue.append(5)
print(dequeue)
dequeue.pop()
print(dequeue)

# Reverse
dequeue.reverse()
print(dequeue)

# Copy 
de2 =dequeue.copy() 
print(de2)
