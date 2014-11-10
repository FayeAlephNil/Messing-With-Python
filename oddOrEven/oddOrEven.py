def check(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
def evens(numberWanted):
    evens = []
    a = -1
    while a < numberWanted:
        a = a + 1
        if check(a) == "even":
            evens.append(a)
    return evens
def odds(numberWanted):
    odds = []
    a = -1
    while a < numberWanted:
        a = a + 1
        if check(a) == "odd":
            odds.append(a)
    return odds
def run():
    oddOrEven = input("Do you want to print the odd or even numbers? (odd or even)")
    numberWanted = int(input("How many do you want to print? (must be positive)"))
    if oddOrEven == "odd":
        for num in odds(numberWanted):
            print(num)
    elif oddOrEven == "even":
        for num in evens(numberWanted):
            print(num)
run()