def task_ar_Odd_list():
    import random
    numbers = []
    for i in range(10):
        numbers.append(int(random.random() * 10))
    print(numbers)
    even = 0
    print("Odd numbers in range:")
    for i in numbers:
        if i < 0:
            break
        if i % 2 == 0:
            even += 1
        else:
            print(i, end=" ")
def exponation_fuc():
    number_ex = int(input("Enter number to exponentiation: "))
    max_res = int(input("Enter max number of exponation: "))
    max_ex = 2
    while number_ex**max_ex <= max_res :
        if number_ex < 0:
            print("It shoud be positive num")
            break
        print (number_ex**max_ex, end=' ')
        number_ex += 1

def arifm_progresion():
    # Array 3: A, A+D, A+2*D, A+3*D
    import math

    while True:
        a = []
        N = int(input("Enter the size of massive: "))
        if N < 1:
            print("The N num shoud be more than '1'")
            continue
        A = int(input("Enter nuber A: "))
        D = int(input("Enter D of the Arithmetic progression: "))
        i = 1
        for q in range(N):
            print(A)
            i += 1
            for w in range(N):
                print(A + D)
                for w in range(N):
                    print(A + i * D)
                    i += 1
                    for e in range(N):
                        print(A + i * D)
                        i += 1

