n, m = map(int, input().split())

s = []
def f():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        s.append(i)
        f()
        s.pop()

f()