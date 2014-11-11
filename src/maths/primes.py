def check(n, primes):
    count = 0
    for num in primes:
        if n % num != 0:
            count += 1
    return len(primes) == count


def prime(n):
    a = 2
    primes = []
    if n > 0:
        primes = [2]
        while len(primes) < n:
            a += 1
            if check(a, primes):
                primes.append(a)
    return primes


def print_primes_easily(n):
    a = 2
    if n > 0:
        print("2")
        primes = [2]
        while len(primes) < n:
            a += 1
            if check(a, primes):
                primes.append(a)
                print(a)


def print_all():
    primes = [2]
    a = 2
    while 1:
        a += 1
        if check(a, primes):
            primes.append(a)
            print(a)


def run():
    all_or_some = input("Do you want to print all the primes or only a certain number?(all or some)")
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
                primes = prime(number_wanted)
                for num in primes:
                    print(num)
            elif way == "s":
                print_primes_easily(number_wanted)
            else:
                print("Try s or all next time")
                yes_or_no = input("Try again? (yes or no) \n")
                if yes_or_no == "yes":
                    run()
    elif all_or_some == "all":
        print_all()
    else:
        print("You can only enter all or some!")
        yes_or_no = input("Try again? (yes or no) \n")
        if yes_or_no == "yes":
            run()
if __name__ == "__main__":
    run()