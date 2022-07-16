import file
import sys


def pack():
    zip = open(sys.argv[1] + '.mvzip', 'w')
    for arg in sys.argv[2:]:
        zip.write(str(file.File(arg)))


if __name__ == '__main__':
    pack()
