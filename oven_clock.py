A, B = map(int, input().split())
C = int(input())
x = 0
y = 0
if 0 <= A <= 23 and 0 <= B <= 59:
    if C + B > 59:
        B = C + B
        x = B // 60
        y = B % 60
        A = A + x

        if A % 24 == 0:
            A = 0
            print(A, y)
        else:
            print(A, y)
    elif C + B < 59:
        B = B + C
        print(A, B)
    #elif (B + C) // 60 == 0:
      #  A = 0
      #  B = B + C
      #  x = (B + C) // 60
      #  A = A + x
     #   print(A, B)





