import mutagen
import sys, os, glob, re

keyRe = re.compile("(?<![A-z0-9])[1-9][a-bA-B](?![A-z])")

# KeyPad py3.x, adds leading 0s to key tags
# By _r0uge
# Built in python 3.7.0, support not included
# Tested on py3.6.7 and py3.7.0 x64
############################################
# Heavily inspired by Carlos Lanenga


def keyChange(dir, comm, lang):
    """Changes all the keys of files in a directory.
    
    First it globs all audio files in the usual formats (check the types list)
    into one giant list then it runs the key and/or comment fields through a
    regex (check keyRe) and replaces them with the fixed key.
    
    Arguments:
        dir {str} -- Path of the folder to change.
        comm {str} -- Either 0, 1 or x, determines whether the files' comments
                    are checked.
        lang {str} -- The ISO639.2 language code for comments.
    
    Returns:
        int -- 0 for success, 1 for failure
    """

    os.chdir(dir)
    files = []
    types = ["mp3", "aiff", "mp4", "ogg", "m4a", "flac"]
    for type in types:
        files.extend(glob.glob("*." + type))
    if not files:
        return 1

    # Searches all the files for key/comment tags
    for file in files:
        print(file)

        try:
            tag = mutagen.File(file)
        except:
            print("!-no tag \n")
            continue

        if tag == {}:
            print("!-empty tag \n")
            continue

        # This code handles searching comments, if exclusive comment mode
        # is on then it skips the key.
        if comm == "1" or comm == "x":
            try:
                frame = "COMM::" + lang
                comment = tag[frame]
                for i in range(len(comment.text)):
                    text = comment.text[i]
                    match = keyRe.search(text)
                    if match:
                        new_comm = (
                            text[0 : match.start()]
                            + "0"
                            + match[0].upper()
                            + text[match.end() :]
                        )
                        tag[frame].text[i] = new_comm
                        tag.save()
                        print("--new comment is:", new_comm)
                    else:
                        print("!-comment didn't include key that needed fixing")
            except:
                print("!-no comment")
            if comm == "x":
                print("\n")
                continue

        # This block handles the key field
        try:
            key = tag["TKEY"].text[0]
            print("--currently", key)
        except:
            print("!-no key \n")
            continue

        key_match = keyRe.search(key)
        if key_match:
            new_key = "0" + key_match[0].upper()
            print("--new value is:", new_key, "\n")
            tag["TKEY"].text[0] = new_key
            tag.save()

        else:
            print("--no change in tag \n")
            continue
    return 0


def climb(dir):
    """Gets all sub directories of the inputted directory. Only gets called
    with the -w option enabled.
    
    Arguments:
        dir {str} -- The root directory.
    
    Returns:
        [list] -- All sub directories of the root.
    """

    res = []
    print("Walk progress: \n")
    for root, sub, files in os.walk(dir):
        if not len(files) == 0:
            res.append(root)
            print("*", end="")
    return res


def main():
    """Runs everything else
    """

    print(
        "",
        "######### Keypad.py ##########",
        '   by _r0uge',
        "     fixing tags since 2018",
        "-" * 22,
        sep="\n",
    )
    dirs = []
    walk = False
    comm = "0"
    lang = "eng"
    if len(sys.argv) >= 2:
        for i in sys.argv:
            if i.lower() == "-w" or i.lower() == "--walk":
                print("Walking mode enabled")
                walk = True
            elif i.lower() == "-c" or i.lower() == "--comment":
                print("Comment mode enabled")
                comm = "1"
            elif i.lower() == "-xc":
                print("Exclusive comment mode enabled")
                comm = "x"
            elif i.lower()[0:3] == "-l=" and len(i) == 6:
                lang = i.lower()[-3:]
            elif (
                i.lower() == "-h" or i.lower() == "--h" or i.lower() == "-help"
            ):
                print(
                    "keypad.py is a tool to zero pad MiK results",
                    "use -w or --walk to go through all sub folders",
                    "use -c or --comment to fix tags that are stored in comments",
                    "use -xc to only fix comments",
                    "use -l=[ISO-639.2 Code] if your comment isn't in english",
                    "remember to put quotes around paths that have spaces in them",
                    sep="\n",
                )
                sys.exit(0)
            elif not i == sys.argv[0]:
                dirs.append(i)
    else:
        print(
            "You could use sys.argv",
            "heres a normal input, use commas as delimiters (space after)",
            "but you don't get to use cool extras",
            sep="\n",
        )
        try:
            inp = input().split(", ")
        except KeyboardInterrupt:
            sys.exit(1)
        dirs.extend(inp)

    if walk:
        for name in dirs:
            subs = climb(name)
        dirs.extend(subs)

    print("\n", "-" * 22, "\n")

    for name in dirs:
        if not os.path.isdir(name):
            print("%s: that's not a directory" % name)
            sys.exit(1)
        else:
            retValue = keyChange(name, comm, lang)
            if not retValue == 0:
                if retValue == 1:
                    continue
                else:
                    sys.exit(retValue)


if __name__ == "__main__":
    main()
