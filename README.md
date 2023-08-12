# s2busb

## Notice

This script is tailored towards the Flipper Zero and only supports **Rubber Ducky script version 1.0**!

## Usage

The script takes an input file and writes the contents to an output file.
Any commands that are specific to Rubber Ducky script (e.g. `SHIFT DELETE`, `PRINTSCREEN`) can be specified in the source script through a comment.

```bash
./s2busb.py -i bash_script.sh -o rubber_script.txt
./s2busb.py --input bash_script.sh --output rubber_script.txt
```

## Additional Resource

- [Rubber Ducky Scripting Language v1.0 - web.archive.org](https://web.archive.org/web/20220816200129/http://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript)
- [BadUSB Documentation - docs.flipper.net](https://docs.flipper.net/bad-usb)
