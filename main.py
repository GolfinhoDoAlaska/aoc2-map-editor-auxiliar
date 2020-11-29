import os
import glob

print(os.listdir('.'))


count = 0

files = [f for f in glob.iglob('*', recursive=True) if f[0].isnumeric()]

while 1 == 1:
    for file_name in files:
        print(file_name)
        with open(file_name, "r") as f:
            c = f.read()
            f.close()
            if c == ";" or c == " " or c == "":
                if os.path.isfile(file_name):
                    os.remove(file_name)

        if os.path.isfile(str(count)):
            pass
        else:
            os.rename(file_name, str(count))
        
        count += 1