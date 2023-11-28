def str_generate(string, indent, sep="", start=" ", finish=" ", палка="|"):
    str = палка
    if isinstance(string, list):
        for i in range(len(string)):
            str += f"{start}{string[i]:{sep}<{indent[i]}}{finish}|"
    else:
        str += f"{start}{string:{sep}<{indent}}{finish}|"
    return str


def format(cases, benchmarks, case_times):
    # print(list(map(len, list(map(str, case_times[0])))))
    benchmarks.insert(0, "Benchmark")
    indents = [0 for i in range(0, len(benchmarks) + 1)]
    indents[0] = max(max(map(len, map(str, cases))), len(benchmarks[0]))
    for i in range(1, len(benchmarks)):
        leni = max(max(map(len, list(map(str, case_times[i - 1])))),
                   len(benchmarks[i]))
        indents[i] = leni if leni >= 4 else 4
    print(str_generate(benchmarks, indents))
    print(str_generate(string="", sep="-", start="", finish="",
                       indent=(sum(indents) + 3 * len(benchmarks) - 1)))
    for i in range(1, len(cases) + 1):
        for j in range(len(benchmarks)):
            if j == 0:
                string = str_generate(cases[i - 1], indents[j])
            else:
                time = f"{case_times[i - 1][j - 1]:2}"
                string += str_generate(time, indents[j], палка="")
        print(string)


format(["b", "th"],
       ["quick sort", "quack sort"], [[1.23, 1.56123123123132, 2.0],
                                             [3.3, 2.9, 3.92]])
