print("""Numero primo""")
def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input("ubique un numero:"))
    result = isPrime(num)

    if result is True:
        print('si es primo!!')
    else:
        print('no es primo !!')

if __name__ == '__main__':
    app()