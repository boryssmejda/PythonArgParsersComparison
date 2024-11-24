import argparse
import os


def file_exists(filepath: str) -> str:
    """Check if a file exists.

    Args:
        filepath (str): The path to the file to validate.

    Returns:
        str: The validated file path.

    Raises:
        argparse.ArgumentTypeError: If the file does not exist.
    """

    if not os.path.isfile(filepath):
        raise argparse.ArgumentTypeError(f"The file '{filepath}' does not exist.")
    return filepath


def parseArguments() -> argparse.Namespace:
    wc_description = """
This is a Python implementation of the wc command. You can use it to count
lines, words, or characters in one or more files. If no option is specified,
it will count lines, words, and characters by default.
"""

    parser = argparse.ArgumentParser(
        prog="wc_argparse.py",
        description=wc_description
    )
    parser.add_argument('-c', '--bytes', action='store_true', help="print the byte counts")
    parser.add_argument('-m', '--chars', action='store_true', help="print the character counts")
    parser.add_argument('-l', '--lines', action='store_true', help="print the newline counts")
    parser.add_argument('-L', '--max-line-length', action='store_true', help="print the length of the longest line")
    parser.add_argument('-w', '--words', action='store_true', help="print the word counts")
    parser.add_argument('--version', action='store_true', required=False, help="output version information and exit")
    parser.add_argument('<file>', metavar='FILE', nargs='+', type=file_exists)

    return parser.parse_args()


def printConfiguration(args: argparse.Namespace) -> None:
    print(args)

    if args.bytes:
        print('Print bytes in file.')

    if args.chars:
        print('Print character in file.')

    if args.lines:
        print('Print number of lines in file.')

    if args.words:
        print('Print number of words in file.')

    if args.max_line_length:
        print('Print maximum length of the line.')

    if not (args.bytes or args.chars or args.lines or args.words) and not args.max_line_length:
        print('Print bytes, characters, lines and words!')


def main() -> None:
    args = parseArguments()
    printConfiguration(args)

if __name__ == '__main__':
    main()
