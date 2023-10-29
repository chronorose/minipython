def format(cases, benchmarks, case_times):
    benchmarks.insert(0, "Benchmark")
    indents = [0 for i in range(0, len(benchmarks) + 2)]
    indents[0] = max(max(map(len, cases)), len(benchmarks[0]))
    for i in range(1, len(benchmarks)):
        indents[i] = len(benchmarks[i]) if len(benchmarks[i]) >= 4 else 4
    first_str = "|"
    for i in range(len(benchmarks)):
        first_str += f" {benchmarks[i]:<{indents[i]}} |"
    print(first_str)
    str = ""
    print(f"|{str:-<{sum(indents) + 3 * len(benchmarks) - 1}}|")
    for i in range(1, len(cases) + 1):
        str = ""
        for j in range(len(benchmarks)):
            if j == 0:
                str += f"| {cases[i - 1]:<{indents[j]}} |"
            else:
                time = f"{case_times[i - 1][j - 1]:2}"
                str += f" {time:<{indents[j]}} |"
        print(str)


format(["best case", "the worst case"],
       ["quick sort", "quack sort", "ooo"], [[1.23, 1.56, 2.0],
                                             [3.3, 2.9, 3.92]])
