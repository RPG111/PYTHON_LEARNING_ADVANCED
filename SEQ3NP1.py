def seq2np1(n):
    while n != 1:
        print(n, end=", ")
        if n%2 == 0:
            n = n//2
        else:
            n = n*3+1
    print(n, end=", ")

N = int(input())
seq2np1(N)