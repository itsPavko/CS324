def fibonaci(n):
    if n <= 0:
        return "Unesite pozitivan broj"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

n = int(input("Unesite broj n za fibonacijev niz: "))

rezultat = fibonaci(n)
print(f"Element fibonacijevog niza za n = {n} je {rezultat}")
