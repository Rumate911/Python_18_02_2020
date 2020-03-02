def For_task2_increase_list(A,B):
A = int(input("Enter number A "))
B = int(input("Enter number B "))
if A > B :
    print("A shoud be less than B")
N = B
for i in range(A, B-0+1):
    print(i, end=" ")
if A > 0 and B > 0:
    print("\nN - number", N)