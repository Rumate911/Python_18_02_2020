def for_task2_increase_list(A,B):
    N = B
    for i in range(A, B-0+1):
        print(i, end=" ")
    if A > 0 and B > 0:
        print("\nN - number", N)

def for_task2_down_list(A,B):
    if A > B :
        print("A shoud be less than B")
    N = B
    for i in range(A-1, B, A-1):
        print(i, end=" ")
