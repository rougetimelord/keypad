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
        print('try getting some music')
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
            print("--currently "+key)
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
            print('--new value is: '+new_key)
            tag.add(TKEY(encoding=3, text=new_key))
            tag.save()
        
        else:
            continue
    return 0
 
if __name__ == "__main__":
    dirs = []
    if len(sys.argv) >= 2:
        for i in range(1, len(sys.argv)):
            dirs.append(sys.argv[i])
    else:
        print("You could use sys.argv, but heres a normal input, use commas as delimiters (no space before or after)")
        inp = input().split(",")
        dirs.extend(inp)
    
    for dir in dirs:
        if not os.path.isdir(dir):
            print("you fucked up")
            sys.exit(2)
        else:
            retValue = main(dir)
            if not retValue == 0:
                sys.exit(retValue)