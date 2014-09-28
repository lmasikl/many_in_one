# coding=utf-8
"""
Collect many files in one.
"""
import os
import sys
import re

__author__ = 'maxim'
__project__ = 'many_in_one'

EXCLUDE_DIRS = ['.idea', '.git', 'migrations', 'vendor']

EXCLUDE_FILES = []

FILE_TYPES = r'^.*\.(py|coffee)$'

LOG = True


def log(message):
    if LOG:
        print(message)


def collect(_path):
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
                    output_file.write('*{file}*\n\n'.format(file=file_name))
                    output_file.write(input_file.read())
                    output_file.write('\n\n')
                    output_file.write('=' * 120)
                    output_file.write('\n\n')

                log('File {0} was read.'.format(file_name))


def main():
    if len(sys.argv) < 2:
        _path = '.'
    else:
        _path = sys.argv[1]

    collect(_path)


if __name__ == '__main__':
    main()