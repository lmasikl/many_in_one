# coding=utf-8
import os
import sys
import re

__author__ = 'maxim'
__project__ = 'many_in_one'
__version__ = '0.0.1'

EXCLUDE_DIRS = ['.idea', '.git', 'migrations', 'vendor', 'env']

EXCLUDE_FILES = []

FILE_TYPES = r'^.*\.(py|coffee)$'

LOG = False


def log(message):
    if LOG:
        print(message)


def collect(_path):
    """
    Collect many files in one.

    :param _path:
    :return:

    >>> collect('.')
    >>> 'source_code.txt' in os.listdir('.')
    True
    >>> os.remove('source_code.txt')
    """
    with open('source_code.txt', 'w+') as output_file:
        for _dir, dirs, files in os.walk(_path):
            if True in map(lambda x: x in _dir, EXCLUDE_DIRS):
                log('Dir {0} was excluded.'.format(_dir))
                continue

            for file_name in files:
                if file_name in EXCLUDE_FILES or not re.match(FILE_TYPES, file_name):
                    log('File {0} was excluded.'.format(file_name))
                    continue

                file_name = os.path.join(_dir, file_name)
                with open(file_name) as input_file:
                    output_file.write('{file}\n'.format(file=file_name))
                    output_file.write('=' * 120)
                    output_file.write('\n')
                    output_file.write(input_file.read())
                    output_file.write('\n\n\n')

                log('File {0} was read.'.format(file_name))


if __name__ == '__main__':
    _path = '.'
    EXIT = True

    if len(sys.argv) == 2:
        EXIT = False
        _path = sys.argv[1]

    if '-v' in sys.argv:
        EXIT =False
        import doctest
        doctest.testmod()

    if not EXIT:
        collect(_path)
    else:
        print('Nothing done')
