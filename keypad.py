from mutagen.id3 import ID3, TKEY
import sys, os, glob

# KeyPad py3.6, adds leading 0s to key tags
# By _rouge
############################################
# Heavily inpired by Carlos Lanenga

def main(dir):
    os.chdir(dir)
    mp3s = []
    mp3s.extend(glob.glob("*.mp3"))
    if not mp3s:
        return 1
    
    for file in mp3s:
        print(file)

        try:
            tag = ID3(file)
        except:
            print('!-no tag \n')
            continue

        if tag == {}:
            print('!-empty tag \n')
            continue

        try:
            key = tag["TKEY"].text[0]
            print("--currently",key)
        except:
            print('!-no key \n')
            continue

        key_number = key[:-1]
        key_letter = key[-1:]

        try:
            num = int(key_number)
        except ValueError:
            print("!-key number isn't a number :O \n")
            continue
        
        if num < 10 and len(key_number) < 2:
            new_key = "0"+key_number+key_letter
            print('--new value is:',new_key,"\n")
            tag.add(TKEY(encoding=3, text=new_key))
            tag.save()
        
        else:
            print('--no change in tag \n')
            continue
    return 0

def climb(dir):
    res = []
    for root, sub, files in os.walk(dir):
            if len(files) != 0:
                res.append(root)
    print("One more dir done")
    return res
 
if __name__ == "__main__":
    dirs = []
    walk = False
    if len(sys.argv) >= 2:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == '-W' or sys.argv[i] == "--walk":
                walk = True
            else:
                dirs.append(sys.argv[i])
    else:
        print("You could use sys.argv","heres a normal input, use commas as delimiters (space after)","but you don't get to use walk mode -W/--walk",sep="\n")
        inp = input().split(", ")
        dirs.extend(inp)

    if walk:
        print("Walking mode enabled see ya in a bit")
        for dir in dirs:
            subs = climb(dir)
        dirs.extend(subs)
        print(dirs)
    
    for dir in dirs:
        print(dir)
        if not os.path.isdir(dir):
            print("you fucked up")
            sys.exit(2)
        else:
            retValue = main(dir)
            if not retValue == 0:
                if retValue == 1:
                    print('oops')
                    continue
                else:
                    sys.exit(retValue)