# Key Pad

~~Pioneer is always right.~~
This tool adds a leading zero to your MiK key tags, so that the sorting on XDJs/CDJs actually makes sense.


### How do I use this?!
- use python **3.4+**
- run: `pip install mutagen` or `sudo apt-get install python-mutagen python3-mutagen`
- run: `python keypad.py {--walk/-W} {PATH}....` or don't use sys.argv whatever
    - Multiple paths are allowed, just use double quotes if the path has a space in it
    - `--walk/-W` enables walking mode which walks through all sub directories of supplied paths