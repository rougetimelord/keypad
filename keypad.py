import mutagen
import sys, os, glob, re
keyRe = re.compile('(?<![0-9])[1-9][a-bA-B]')
# KeyPad py3.6, adds leading 0s to key tags
# By _rouge
############################################
# Heavily inpired by Carlos Lanenga

def key_chng(dir, comm, lang):
    os.chdir(dir)
    files = []
    files.extend(glob.glob('*.mp3'))
    files.extend(glob.glob('*.aiff'))
    if not files:
        return 1
    
    for file in files:
        print(file)

        try:
            tag = mutagen.File(file)
        except:
            print('!-no tag \n')
            continue

        if tag == {}:
            print('!-empty tag \n')
            continue

        if comm == '1' or comm == 'x':
            try:
                frame = 'COMM::' + lang
                comment = tag[frame]
                for i in range(len(comment.text)):
                    text = comment.text[i]
                    match = keyRe.search(text)
                    if match:
                        new_comm = text[0:match.start()] + '0' + match[0].upper() + text[match.end():]
                        tag[frame].text[i] = new_comm
                        tag.save()
                        print('--new comment is:', new_comm)
                    else:
                        print("!-comment didn't include key that needed fixing")
                if comm == 'x':
                    print('\n')
                    continue
            except:
                print('!-no comment')
                if comm == 'x':
                    print('\n')
                    continue

        
        try:
            key = tag['TKEY'].text[0]
            print('--currently',key)
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
            print('--new value is:',new_key,'\n')
            tag['TKEY'].text[0] = new_key
            tag.save()
        
        else:
            print('--no change in tag \n')
            continue
    return 0

def climb(dir):
    res = []
    print('Walk progress: \n')
    for root, sub, files in os.walk(dir):
            if len(files) != 0:
                res.append(root)
                print('*',end='')
    return res

def main():
    print('', '#### Keypad.py ####','     by _rouge     ', 'fixing tags since 2018', '-'*22, '', sep='\n')
    dirs = []
    walk = False
    comm = '0'
    lang = 'eng'
    if len(sys.argv) >= 2:
        for i in range(1, len(sys.argv)):
            if sys.argv[i].lower() == '-w' or sys.argv[i].lower() == '--walk':
                print('Walking mode enabled')
                walk = True
            elif sys.argv[i].lower() == '-c' or sys.argv[i].lower() == '--comment':
                print('Comment mode enabled')
                comm = '1'
            elif sys.argv[i].lower() == '-xc':
                print('Exclusive comment mode enabled')
                comm = 'x'
            elif sys.argv[i].lower()[0:3] == '-l=' and len(sys.argv[i]) == 6:
                lang = sys.argv[i].lower()[-3:]
            else:
                dirs.append(sys.argv[i])
    else:
        print("You could use sys.argv","heres a normal input, use commas as delimiters (space after)","but you don't get to use cool extras",sep="\n")
        inp = input().split(", ")
        dirs.extend(inp)

    if walk:
        for name in dirs:
            subs = climb(name)
        dirs.extend(subs)

    print('\n','-'*22 ,'\n')
    
    for name in dirs:
        if not os.path.isdir(name):
            print("That's not a directory")
            sys.exit(2)
        else:
            retValue = key_chng(name, comm, lang)
            if not retValue == 0:
                if retValue == 1:
                    continue
                else:
                    sys.exit(retValue)
 
if __name__ == "__main__":
    main()