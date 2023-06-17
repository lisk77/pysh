# pysh - The Python Shell

pysh is a shell written in python which pipes the inputs into bash.

## Why pysh?

pysh, being programmed in python, can be customized with python. It can also do calculations inside of the terminal. Just type in your equation and it will print out the result

## Installation

As of right now this is a WIP. So if you want to use pysh, you will have to chmod the file yourself to turn it into an executable and put it ins your `/usr/bin` directory. (Linux only as of right now)  

## Functionality

- [x] bash capabilities
- [x] costumizable prompt
- [x] prompt calculator
- [x] aliases
- [ ] syntax highlighting
- [ ] up/down arrow capability

## Customization

To customize your prompt, edit the pyshPrompt.py file in the .config/pysh folder (LINUX). The `__repr__` method will be what is shown on screen. You can use any python library to customize the prompt and let it suite your astethic needs.
