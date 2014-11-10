phi = (1 + 5**0.5) / 2

def F(n):
    return int(round((phi**n - (1-phi)**n) / 5**0.5))
def fib(n):
    a = 0
    fibs = []
    if n > 0:
        while a < n:
            a = a + 1
            fibs.append(F(a))
    elif n < 0:
        while a > n:
            a = a - 1
            fibs.append(F(a))
    return fibs
def run():
    number_wanted = int(input("Stage of Fibs wanted"))
    fibs = fib(number_wanted)
    print("F(0) = 0")
    a = 0
    if number_wanted > 0:
        while a < number_wanted:
            a = a + 1
            print("F(" + str(a) + ") = " + str(fibs[a-1]))
    elif number_wanted < 0:
        while a > number_wanted:
            a = a - 1
            print("F(" + str(a) + ") = " + str(fibs[(-1 * a)-1]))

run()
