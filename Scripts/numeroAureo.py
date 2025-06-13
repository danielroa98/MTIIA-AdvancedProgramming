def fib(n=10):
    lista = [0,1]
    for _ in range(n):
        lista.append(lista[-1] + lista[-2])
    return lista


if __name__ == "__main__":
    print(fib(5))
