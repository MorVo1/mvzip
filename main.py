import files
import sys


def pack():
    zip = open(sys.argv[1] + '.mvzip', 'w')
    for file in sys.argv[2:]:
        zip.write(str(files.File(file)))


if __name__ == '__main__':
    pack()
