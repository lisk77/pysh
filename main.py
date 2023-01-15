from pyshPrompt import Prompt
from pyshMath import *
from prompt_toolkit import prompt
import os
import sys

### THE SHELL ###

def main():
    run = True
    while run:
        pr = Prompt().__repr__()
        line = prompt(pr)
        if "exit" == line:
            run = False
        else:
            try:
                print(eval(line))
            except:
                try:
                    os.system(line)
                except:
                    print("pysh: Unknown command!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(" ")
        sys.exit(0)
