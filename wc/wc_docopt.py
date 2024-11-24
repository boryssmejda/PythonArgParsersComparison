"""
This is a Python implementation of the wc command. You can use it to count
lines, words, or characters in one file. If no option is specified,
it will count lines, words, and characters by default.

Usage:
    wc [options] <file>
    wc <file>
    wc --help
    wc --version

Options:
    -c, --bytes             print the byte counts
    -m, --chars             print the character counts
    -l, --lines             print the newline counts
    -L, --max-line-length   print the length of the longest line
    -w, --words             print the word counts
    --help                  display this help and exit
    --version               output version information and exit
"""

from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
