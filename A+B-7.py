T = input()
T = int(T)
x = 0

for x in range(T):
    A, B = map(int, input().split())
    sum = A + B
    print("Case #%s: %s" %(x + 1, sum))
