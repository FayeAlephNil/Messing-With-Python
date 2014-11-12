from src.maths import primes


def write_primes_easily(n, file):
    a = 2
    if n > 0:
        file.write("2\n")
        primes_array = [2]
        while len(primes_array) < n:
            a += 1
            if primes.check(a, primes_array):
                primes_array.append(a)
                file.write(str(a) + "\n")


def write_all(directory):
    file = open(directory, "w")
    primes_array = [2]
    a = 2
    print("2")
    file.write("2\n")
    while 1:
        a += 1
        if primes.check(a, primes_array):
            primes_array.append(a)
            print(a)
            file.write(str(a) + "\n")


def run():
    directory = 'out/primes.txt'
    fileout = open(directory, "w")
    fileout.truncate(0)
    all_or_some = input("Do you want to get all the primes or only a certain number?(all or some)")
    if all_or_some == "some":
        number_wanted = int(input("Number of Primes (must be positive and not equal to 0)"))
        way = input("Do you want to print primes successively or all at once (s or all)?")
        if number_wanted <= 0:
            print("Number of Primes must be positive and not equal to 0")
            yes_or_no = input("Try again? (yes or no) \n")
            if yes_or_no == "yes":
                run()
        else:
            if way == "all":
                primes_array = primes.prime(number_wanted)
                for num in primes_array:
                    print(num)
                    fileout.write(str(num) + "\n")
            elif way == "s":
                primes.print_primes_easily(number_wanted)
                write_primes_easily(number_wanted, fileout)
            else:
                print("Try s or all next time")
                yes_or_no = input("Try again? (yes or no) \n")
                if yes_or_no == "yes":
                    run()
    elif all_or_some == "all":
        write_all(directory)
    else:
        print("You can only enter all or some!")
        yes_or_no = input("Try again? (yes or no) \n")
        if yes_or_no == "yes":
            run()


if __name__ == "__main__":
    run()