import sys
sys.path.append('src')
from tmLogic import tmLogic


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Hello World!")
    logic = tmLogic()
    logic.run()


if __name__ == "__main__":
    main()
