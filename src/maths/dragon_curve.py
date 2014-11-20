
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
    elif stage > 1:
        output = get_stage(stage-1)
        for char in output:
            output + convert(char)
    elif stage <= 0:
        print("Stage must be greater than 0")
        yes_no = input("Do you want to go again?")
        if yes_no == "yea":
            run()
    return output


def run():
    stage = int(input("What stage of the dragon curve do you (must be greater than 0)\n"))
    print(get_stage(stage))

if __name__ == "__main__":
    run()