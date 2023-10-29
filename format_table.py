def str_generate(xs, indent, sep="", start=" ", finish=" ", палка="|"):
    str = палка
    if isinstance(xs, list):
        for i in range(len(xs)):
            str += f"{start}{xs[i]:{sep}<{indent[i]}}{finish}|"
    else:
        str += f"{start}{xs:{sep}<{indent}}{finish}|"
    return str


def format(cases, benchmarks, case_times):
    benchmarks.insert(0, "Benchmark")
    indents = [0 for i in range(0, len(benchmarks) + 1)]
    indents[0] = max(max(map(len, cases)), len(benchmarks[0]))
    for i in range(1, len(benchmarks)):
        indents[i] = len(benchmarks[i]) if len(benchmarks[i]) >= 4 else 4
    print(str_generate(benchmarks, indents))
    print(str_generate(xs="", sep="-", start="", finish="",
                       indent=(sum(indents) + 3 * len(benchmarks) - 1)))
    for i in range(1, len(cases) + 1):
        for j in range(len(benchmarks)):
            if j == 0:
                string = str_generate(cases[i - 1], indents[j])
            else:
                time = f"{case_times[i - 1][j - 1]:2}"
                string += str_generate(time, indents[j], палка="")
        print(string)


format(["best case", "the worst case"],
       ["quick sort", "quack sort", "ooo"], [[1.23, 1.56, 2.0],
                                             [3.3, 2.9, 3.92]])
