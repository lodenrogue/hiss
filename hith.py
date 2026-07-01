from evaluate import Evaluator, Env, Variables

evaluate = Evaluator().evaluate


def start_repl():
    print("Welcome to Hith. A lisp written in Python.")
    print("Type exit to quit.")

    while True:
        try:
            exp = input(">>> ")

            if exp == "exit":
                exit()
            else:
                print(evaluate(exp))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    start_repl()
