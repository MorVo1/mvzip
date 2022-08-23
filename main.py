import file
import sys


def pack():
    zip = open(sys.argv[1] + '.mvzip', 'w')
    for arg in sys.argv[2:]:
        zip.write(str(file.File(arg)))
        zip.write('\n')
    
def unpack():
    zip = open(sys.argv[1])
    f = zip.readlines()
    for line in f:
        c = open(line.split(';')[0], 'w')
        c.write(''.join(line.split(';')[1:]).replace('\\n','\n'))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        unpack()
        sys.exit()
    pack()
    sys.exit()

