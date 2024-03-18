import sys
import argparse
import os

def first_letters(big_block, keep_punctuation = True, keep_whitespace=False):
    for i in "|;:,.()[]-!?$#+%~<>/|}{\\\"":
        big_block=big_block.replace(i, " "+i*keep_punctuation+" ")
    for i in "\n\t":
        big_block=big_block.replace(i, " "+i*keep_whitespace+" ")
    words = big_block.split(" ")
    out = []
    for word in words:
        if word:
            out.append(word[0])
    return(" ".join(out).replace("\n ", "\n"))

def readFile(path):
    try:
        file = open(path, "r")
        words = file.read()
    except Exception as e:
        sys.stderr.write(f"something went wrong wile reading input file:\n {e}")
    finally:
        file.close()
        return words

def writeFile(text, path):
    try:
        file = open(path, "w")
        file.write(text)
    except Exception as e:
        sys.stderr.write(f"something went wrong wile writing output file:\n {e}")
    finally:
        file.close()

parser = argparse.ArgumentParser( description="this script takes the first letter of every word in a block of text and return them.")

parser.add_argument("-f","--file", action="store_true", help="a file path to read from")
parser.add_argument("-o", "--out", action="store", help="a file path to write to")
parser.add_argument("-p", "--punctuation", action="store_true", help="if true the program will try to preserve punctuation marks")
parser.add_argument("-s", "--whitespace", action="store_true", help="if true the program will try to preserve whitespace")
parser.add_argument("input_text", action="store" )


if __name__ == "__main__":
    args = parser.parse_args()
    print(os.getcwd())
    if args.file:
        words = readFile(args.input_text)
        print(args.punctuation)
        letters = first_letters(words, args.punctuation, args.whitespace)
        if args.out:
            writeFile(letters, args.out)
        else:
            print(letters)
    else:
        print(" ".join(first_letters(args.input_text)))
