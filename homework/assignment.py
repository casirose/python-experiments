import sys

address = sys.argv[1]+sys.argv[2]


def main():
    f = open(address, "w+")
    f.close()


main()
