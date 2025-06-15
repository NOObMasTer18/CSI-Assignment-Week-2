n = int(input())
s = set(map(int, input().split()))

# Read number of commands
N = int(input())


for _ in range(N):
    parts = input().split()
    cmd = parts[0]
    if cmd == "pop":
        
        s.pop()

    elif cmd == "remove":
        
        s.remove(int(parts[1]))

    elif cmd == "discard":
        
        s.discard(int(parts[1]))


print(sum(s))
