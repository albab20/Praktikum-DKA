def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


def cetakFibonacci(n):
    if n <= 0:
        print("Input harus lebih dari 0")
        return
    
    a, b = 0, 1
    print("Deret Fibonacci:")
    
    for i in range(1, n + 1):
        if i == 1:
            print(a)
        elif i == 2:
            print(b)
        else:
            a, b = b, a + b
            print(b)
    print()


n = int(input("Masukkan nilai n: "))

hasil = fibonacci(n)
print("Fibonacci ke-", n, "adalah:", hasil)

cetakFibonacci(n)