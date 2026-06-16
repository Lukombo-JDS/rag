from scripts.output import output
from scripts.var import *
from scripts.vectorisation import *
from scripts.init import initLLM
from rich.traceback import install


def main():

    install()
    # for chunk in output():
    #     print(chunk, end="", flush=True)

    initLLM()

    output(REQUEST_DEFAULT)


if __name__ == "__main__":
    main()
