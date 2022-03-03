T = int(input())
x = 0
for x in range(T):
    A, B = map(int, input().split())
    C = A + B
    print("Case #%s: %s + %s = %s"%(x + 1, A, B, C))
