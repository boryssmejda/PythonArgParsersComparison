"""
This is a Python implementation of the wc command. You can use it to count
lines, words, or characters in one or more files. If no option is specified,
it will count lines, words, and characters by default.

Usage:
    wc [options] <file>...
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
import os
from typing import Dict, Any


def file_exists(filepath: str) -> str:
    """Check if a file exists.

    Args:
        filepath (str): The path to the file to validate.

    Returns:
        str: The validated file path.

    Raises:
        RuntimeError: If the file does not exist.
    """

    if not os.path.isfile(filepath):
        raise RuntimeError(f"The file '{filepath}' does not exist.")
    return filepath


def printConfiguration(args: Dict[str, Any]) -> None:
    print(args)

    if args['--bytes']:
        print('Print bytes in file.')

    if args['--chars']:
        print('Print character in file.')

    if args['--lines']:
        print('Print number of lines in file.')

    if args['--words']:
        print('Print number of words in file.')

    if args['--max-line-length']:
        print('Print maximum length of the line.')

    if not (args['--bytes'] or args['--chars'] or args['--lines'] or args['--words']) and not args['--max-line-length']:
        print('Print bytes, characters, lines and words!')


def main() -> None:
    arguments = docopt(__doc__)
    printConfiguration(arguments)


if __name__ == '__main__':
    main()
