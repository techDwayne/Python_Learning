def arithmetic_arranger(problems, show=False):
    if len(problems) > 5: return "Error: Too many problems."
    first = []
    second = []
    lens = []
    operator = ""
    for problem in problems:
        a, o, c = problem.split()
        if not a.isnumeric() or not c.isnumeric():
            return "Error: Numbers must only contain digits."
        first.append(a)
        operator += o
        second.append(c)
        lens.append(max(map(len, [a, c])))
    # Errors
    for i in lens:
        if i > 4: return "Error: Numbers cannot be more than four digits."
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."
    # Printing
    ret = "    ".join([first[i].rjust(lens[i] + 2)
                       for i in range(len(first))]) + "\n"
    ret += "    ".join([
        operator[i] + " " + second[i].rjust(lens[i])
        for i in range(len(second))
    ]) + "\n"
    ret += "    ".join(["-" * (lens[i] + 2) for i in range(len(lens))])
    # print(ret)
    if show:
        ret += "\n" + "    ".join([
            str(eval(problems[i])).rjust(lens[i] + 2)
            for i in range(len(first))
        ])
    return ret


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))