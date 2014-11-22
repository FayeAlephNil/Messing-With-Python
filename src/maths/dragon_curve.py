def convert(char):
    if char == 'D':
        return "DL"
    elif char == 'L':
        return "FL"
    elif char == 'F':
        return "FR"
    elif char == 'R':
        return "DR"


def get_stage(stage):
    output = ""
    if stage == 1:
        return "D"
    elif 1 < stage < 998:
        last = get_stage(stage-1)
        for char in last:
            output += (convert(char))
    elif stage <= 0 or stage > 997:
        print("Stage must be greater than 0 and less than 998")
        yes_no = input("Do you want to go again? (yes or no)\n")
        if yes_no == "yes":
            run()
    return output


def run():
    stage = int(input("What stage of the dragon curve do you (must be greater than 0 and less than 998)\n"))
    print(get_stage(stage))

if __name__ == "__main__":
    run()