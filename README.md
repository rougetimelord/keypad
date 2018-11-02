# Key Pad

~~Pioneer is always right.~~
This tool adds a leading zero to your MiK key tags, so that the sorting on XDJs/CDJs actually makes sense.

## How to use

- use python **3.4+**
- run: `pip install -r requirements.txt`
- run: `python keypad.py {OPTIONS} {PATH}....` or don't use sys.argv whatever
  - Multiple paths are allowed, just use double quotes if the path has a space in it
- on windows you can optionally run: `./keypad {OPTIONS} {PATH}....` instead
  - Considerably faster than running the python version
    - On Linux/OSX you can build your own executable with `pyinstaller --onefile keypad.py` or use VScode tasks
      - If you build an executable it would be cool if you submitted a PR with it, only builds in python 3.6 (pending updates to [PyInstaller](https://github.com/pyinstaller/pyinstaller))

Options:

- `--walk/-W` enables walking mode, walks through all sub directories of supplied paths
- `--comment/-C` enables comment mode, the script will zero pad keys that are stored in the comment field
- `-XC` enables exclusive comment mode, only comment fields will be processed
- `-l={LANGUAGE CODE}` will change what comment language will be checked, default is 'eng' for English. [Here's a list of ISO 639.2 language codes](https://www.loc.gov/standards/iso639-2/php/code_list.php "ISO 639.2 reference")

Binary signed with the key listed on my [keybase](https://keybase.io/r0uge) with the fingerprint of `F9FE 1C8E D139 E706 F2DC C318 F8B0 FBCA 606A DF14`