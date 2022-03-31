from os import listdir
from os.path import isfile, join

mypath = '/SmallLCLData' # change path if necessary
mac = 'MAC002163'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
write_filename = mypath + "/" + mac + ".csv"
writer = open(write_filename, "w")
writer.write('LCLid,stdorToU,DateTime,KWH/hh (per half hour)\n')
for file in onlyfiles:
    print(file)
    filename = mypath + "/" + file
    openedfile = open(filename, 'r')
    lines = openedfile.readlines()
    for line in lines:
        if mac in line:
            writer.write(line)