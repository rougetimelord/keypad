from mutagen.id3 import ID3, TKEY
import sys, os, glob

# KeyPad py3.6, adds leading 0s to key tags
# By _rouge
############################################
# Heavily inpired by Carlos Lanenga

def main():
    count = 0
    dir =''
    if len(sys.argv) == 2:
        dir = sys.argv[1]
    else:
        print("You could use sys.argv, but heres a normal input")
        dir = input()
    
    if not os.path.isdir(dir):
        print("you fucked up")
        sys.exit(2)

    os.chdir(dir)
    mp3s = []
    files_types = ("*.mp3", "*.MP3", "*.Mp3", "*.mP3")
    for mp3_file in files_types:
        mp3s.extend(glob.glob(mp3_file))
    if not mp3s:
        print('try getting some music')
        sys.exit(1)
    
    for file in mp3s:
        count += 1
        print(file+" #"+str(count))

        try:
            tag = ID3(file)
        except:
            print(' no tag \n')
            continue

        if tag == {}:
            print(' empty tag \n')
            continue

        try:
            key = tag["TKEY"].text[0]
            print(" currently "+key)
        except:
            print(' no key \n')
            continue

        key_number = key[:-1]
        key_letter = key[-1:]

        try:
            num = int(key_number)
        except ValueError:
            print("key number isn't a number :O \n")
            continue
        
        if num < 10 and len(key_number) < 2:
            new_key = "0"+key_number+key_letter
            print(' new value is: '+new_key)
            tag.add(TKEY(encoding=3, text=new_key))
            tag.save()
        
        else:
            continue
 
if __name__ == "__main__":
    main()