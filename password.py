import argparse
import pyperclip
import random
import string
import sys

def main() -> None:
    letters = string.ascii_letters
    punctuation = string.punctuation
    digits = string.digits

    parser = argparse.ArgumentParser(
        prog="Password generator",
        description="Generates a random password of n characters in length"
    )
    parser.add_argument("--copy", action="store_true", help="If set, will copy the generated password to the clipboard. Set to false by default")
    parser.add_argument("--hide", action="store_true", help="If set, will hide the output. Use in conjunction with -c, --copy. Set to false by default.")
    parser.add_argument("--length", type=int, default=0, help="Specify the desired password length")
    parser.add_argument("--alphanum", action="store_true", help="Limit character choice to letters and numbers only.")
    parser.add_argument("-d", action="store_true", help="Sets usage to default settings, overwriting any other flags.")
    args = parser.parse_args()

    if not args.d:
        options = {
            "copy": args.copy,
            "hide": args.hide,
            "length": args.length,
            "alphanum": args.alphanum
        }
    else:
        options = {
            "copy": True,
            "hide": True,
            "length": 20,
            "alphanum": True
        }
    
    if not options["copy"] and options["hide"]:
        sys.exit("Hide set to true and copy set to false. Invalid combination. Exiting...")

    if options["length"] == 0:
        while True:
            length = input("Enter password length: ")
            try:
                length = int(length)
                if length < 5:
                    raise ValueError
                break
            except ValueError:
                pass
        options["length"] = length
    
    if options["alphanum"]:
        choices = list(letters + digits)
    else:
        choices = list(letters + digits + punctuation)
      
    random.shuffle(choices)
    result = ''.join([random.choice(choices) for _ in range(options["length"])])
    
    if options["copy"]:
        pyperclip.copy(result)
        print("Copied to clipboard.")
    if not options["hide"]:
        print(result)


if __name__ == "__main__":
    main()