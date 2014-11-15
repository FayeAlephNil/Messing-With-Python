
##TODO


def run():
    which = input("BBCode to Markdown or Markdown to BBCode (M->B or B->M)")
    directory_in = 'in/input.txt'
    directory_out = 'out/out.txt'
    filein = open(directory_in, "w")
    fileout = open(directory_out, "w")
    if which == "M->B":
        a = filein.readlines()
        fileout.writelines(a)
    elif which == "B->M":
        b = 1
    else:
        print("Please only enter M->B or B->M")
        run()

if __name__ == "__main__":
    run()