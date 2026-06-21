from scripts.output import output
from scripts.var import DEFAULT_REQUEST
from rich.traceback import install


def main():

    install()

    # initLLM()

    output(DEFAULT_REQUEST)


if __name__ == "__main__":
    main()
