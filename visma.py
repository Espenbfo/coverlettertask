from constraint import *

def concat_to_int(*args) -> int:
    """Convert a set of variables one digit a, b, c ... to the number abc... """
    return sum(arg * 10 ** i for i, arg in enumerate(args[::-1]))


def left_equation(v, i, s, m, a, p, n, e, h, *args) -> int:
    return concat_to_int(v, i, s, m, a) + \
           concat_to_int(a, p, i) + \
           concat_to_int(a, i) + \
           concat_to_int(s, a, a, s)


def right_equation(v, i, s, m, a, p, n, e, h, _) -> int:
    return concat_to_int(h, e, a, v, e, n)


def constraint_equation(*args) -> bool:
    return left_equation(*args) == right_equation(*args)


def main():
    possible_values = list(range(10))
    problem = Problem()

    letters = ["v", "i", "s", "m", "a", "p", "n", "e", "h", "l"]

    for letter in letters:
        problem.addVariable(letter, possible_values)

    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(constraint_equation, letters)
    problem.addConstraint(lambda a: a != 1, ("a",))
    problem.addConstraint(lambda m: m != 2, ("m",))

    csp_solution = problem.getSolutions()[0]

    number_to_letter = {csp_solution[l]: l for l in letters}

    solution_word = "".join(number_to_letter[i] for i in [3,1,2,0,3])
    print(solution_word)

if __name__ == "__main__":
    main()
