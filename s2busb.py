#!/usr/bin/python3

from argparse import ArgumentParser
import os
import re


def main():
    parser = ArgumentParser(
            prog='s2busb.py',
            description='Convert Bash, PowerShell or similar languages to BadUSB script.',
            epilog='Copyright 2023 © B1TC0R3 - https://github.com/b1tc0r3')

    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')

    args = parser.parse_args()
    input_file  = args.input
    output_file = args.output
    output_dir  = os.path.dirname(output_file)

    command_regex = re.compile('^(' +\
    '((DEFAULT_?)?DELAY [0-9]+)|' +\
    '(DELAY [0-9]+)|' +\
    '(ALTCHAR .*)|' +\
    '(ALTSTRING .*)|' +\
    '(ALTCODE .*)|' +\
    '(STRING .*)|' +\
    '((ALT-)?GUI( .)?)|' +\
    '((CTRL-|ALT-|GUI-)?SHIFT( (DELETE|HOME|INSERT|PAGEUP|PAGEDOWN|WINDOWS|GUI|UPARROW|DOWNARROW|LEFTARROW|RIGHTARROW|TAB))?)|' +\
    '((CTRL-)?ALT( (END|ESC|ESCAPE|F[1-9][1-2]?|.|SPACE|TAB))?)|' +\
    '((CONTROL|CTRL)( (F[1-9][1-2]?|.|BREAK|PAUSE|ESCAPE|ESC))?)|' +\
    '((DOWN|UP|LEFT|RIGHT)(ARROW)?)|' +\
    '(BREAK|PAUSE|CAPSLOCK|DELETE|END|ESC|ESCAPE|HOME|INSERT|NUMLOCK|PAGEUP|PAGEDOWN|PRINTSCREEN|SCROLLLOCK|SPACE|TAB|FN|ENTER)|' +\
    '(REPEAT [0-9]+)|' +\
    ')$')

    if not os.path.isfile(input_file):
        print('Unable to read input file. Exiting')
        exit(-1)

    if output_dir:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(input_file,  'r') as fr_input_file, open(output_file, 'w') as fw_output_file:
        while True:
            line = fr_input_file.readline()
            if not line:
                break

            if line.lstrip().startswith('#'):
                line = line.lstrip()[1:]
                line = line.strip()

                if command_regex.match(line):
                    fw_output_file.write(line + '\n')

                else:
                    fw_output_file.write('REM ' + line + '\n')

                continue

            if line.isspace():
                fw_output_file.write('\n')
                continue

            fw_output_file.write('STRING ' + line + 'ENTER\n')


if __name__ == '__main__':
    main()
else:
    print(f's2busb.py is not a library file. Exiting.')
    exit(-1)
