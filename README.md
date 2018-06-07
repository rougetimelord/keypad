# Key Pad

~~Pioneer is always right.~~
This tool adds a leading zero to your MiK key tags, so that the sorting on XDJs/CDJs actually makes sense.


### How do I use this?!
- use python **3.4+**
- run: `pip install mutagen` or `sudo apt-get install python-mutagen python3-mutagen`
- run: `python keypad.py {OPTIONS} {PATH}....` or don't use sys.argv whatever
    - Multiple paths are allowed, just use double quotes if the path has a space in it

Options:

- `--walk/-W` enables walking mode, walks through all sub directories of supplied paths
- `--comment/-C` enables comment mode, the script will zero pad keys that are stored in the comment field
- `-XC` enables exclusive comment mode, only comment fields will be processed
- `-l={LANGUAGE CODE}` will change what comment language will be checked, default is 'eng' for English