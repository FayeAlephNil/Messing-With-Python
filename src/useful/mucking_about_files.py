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
    number_wanted = int(input("Number to be exported (must be less than 1475 and greater than -1475)"))
    directory = 'out/fib.txt'
    fileout = open(directory, "w")
    fileout.truncate(0)
    a = 0
    if number_wanted > 0 and number_wanted < 1475:
        fibs = fib(number_wanted)
        fileout.write("F(0) = 0\n")
        while a < number_wanted:
            a = a + 1
            fileout.write("F(" + str(a) + ") = " + str(fibs[a-1]) + "\n")
            print("F(" + str(a) + ") = " + str(fibs[a-1]) + "")
    elif number_wanted < 0 and number_wanted > -1475:
        fibs = fib(number_wanted)
        fileout.write("F(0) = 0\n")
        while a > number_wanted:
            a = a - 1
            fileout.write("F(" + str(a) + ") = " + str(fibs[(-1 * a)-1]) + "\n")
            print("F(" + str(a) + ") = " + str(fibs[(-1 * a)-1]))
    elif number_wanted != 0 and (number_wanted >= 1475 or number_wanted <= 1475):
        print("You entered to large of a number! (must be less than 1475 and greater than -1475)")
        fileout.write("You entered to large of a number! (must be less than 1475 and greater than -1475)")
        q = input("Do you want to continue? (yes or no)")
        if q == "yes":
            print("\n")
            fileout.close()
            run()
run()