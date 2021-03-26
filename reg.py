import re
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('fname')
    args = parser.parse_args()

    searchFile = open(args.fname)
    lineNum = 0

    for line in searchFile.readlines():
        line = line.strip('\n\r')
        lineNum += 1
        searchResult = re.search(args.word, line, re.M | re.I)
        if searchResult:
            print(lineNum.__str__() + ": " + line)


if __name__ == '__main__':
    run()
