def arithmetic_arranger(problems, ans=False):
    # Checking if the problems are 5 or not, coz the limit is 5
    if len(problems) > 5:
        return "Error: Too many problems."

    fst_oper = []  # 1st operand
    sed_oper = []  # 2nd operand
    opert = []  # operator

    for prob in problems:
        pces = prob.split()  # pieces of list,get into another lists
        fst_oper.append(pces[0])
        opert.append(pces[1])
        sed_oper.append(pces[2])

    # Checking for the other than + and - operators
    if "*" in opert or "/" in opert:
        return "Error: Operator must be '+' or '-'."

    # Checking for the digits
    for i in range(len(fst_oper)):
        if not (fst_oper[i].isdigit() and sed_oper[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Checking for the length of the numbers
    for i in range(len(fst_oper)):
        if len(fst_oper[i]) > 4 or len(sed_oper[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Creating the string format which elementary school students like to use for calculation of arithmetic operations like + and -
    fst_line = []  # first line
    sed_line = []  # second line
    thd_line = []  # third line
    frt_line = []  # fourth line

    for i in range(len(fst_oper)):
        if len(fst_oper[i]) > len(sed_oper[i]):

            fst_line.append(" "*2 + fst_oper[i])
        else:
            fst_line.append(
                " "*(len(sed_oper[i]) - len(fst_oper[i]) + 2) + fst_oper[i])

    for i in range(len(sed_oper)):
        if len(sed_oper[i]) > len(fst_oper[i]):

            sed_line.append(opert[i] + " " + sed_oper[i])
        else:
            sed_line.append(
                opert[i] + " "*(len(fst_oper[i]) - len(sed_oper[i]) + 1) + sed_oper[i])

    for i in range(len(fst_oper)):
        thd_line.append("-"*(max(len(fst_oper[i]), len(sed_oper[i]))+2))

    if ans:
        for i in range(len(fst_oper)):
            if opert[i] == "+":
                answer = str(int(fst_oper[i]) + int(sed_oper[i]))
            else:
                answer = str(int(fst_oper[i]) - int(sed_oper[i]))

            # arranging the answer in the format
            if len(answer) > max(len(fst_oper[i]), len(sed_oper[i])):
                frt_line.append(" " + answer)
            else:
                frt_line.append(
                    " "*(max(len(fst_oper[i]), len(sed_oper[i])) - len(answer)+2) + answer)
        # getting the arithmetic format which school children used to do, here it is with answer
        arranged_problems = "    ".join(fst_line) + "\n" + "    ".join(
            sed_line) + "\n" + "    ".join(thd_line) + "\n" + "    ".join(frt_line)

    else:  # without answer
        arranged_problems = "    ".join(
            fst_line)+"\n"+"    ".join(sed_line)+"\n"+"    ".join(thd_line)
    return arranged_problems
