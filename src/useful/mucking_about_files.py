from src.maths import fib


def run():
    number_wanted = int(input("Number to be exported (must be less than 1475 and greater than -1475)"))
    directory = 'out/fib.txt'
    fileout = open(directory, "w")
    fileout.truncate(0)
    a = 0
    if 0 < number_wanted < 1475:
        fibs = fib.fib(number_wanted)
        fileout.write("F(0) = 0\n")
        while a < number_wanted:
            a += 1
            fileout.write("F(" + str(a) + ") = " + str(fibs[a-1]) + "\n")
            print("F(" + str(a) + ") = " + str(fibs[a-1]) + "")
    elif 0 > number_wanted > -1475:
        fibs = fib.fib(number_wanted)
        fileout.write("F(0) = 0\n")
        while a > number_wanted:
            a -= 1
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
if __name__ == "__main__":
    run()