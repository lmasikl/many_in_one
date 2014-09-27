# -*- coding:utf-8 -*-
"""
Collect many files in dir on one file.
"""
import os

__author__ = 'maxim'
__project__ = 'many_in_one'


def collect():
    with open('output.md', 'w+') as output_file:
        for _dir, dirs, files in os.walk('.'):
            if './.idea' in _dir or './.git' in _dir:
                continue

            for ignore in ['.gitignore', 'output.md', '__init__.py']:
                if ignore in files:
                    files.pop(files.index(ignore))

            for file_name in files:
                with open(os.path.join(_dir, file_name)) as input_file:
                    output_file.write('*{file}*\n\n'.format(file=file_name))
                    # output_file.write('```python\n\n')
                    output_file.write(input_file.read())
                    # output_file.write('\n\n```')
                    output_file.write('\n\n')

                print('File {0} was read.'.format(os.path.join(_dir, file_name)))



if __name__ == '__main__':
    collect()