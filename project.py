"""
STATUS: Working

OVERVIEW: Make a template project

IMPROVEMENTS:
    - How database making is managed
"""

# @ Imports
import pathlib
import argparse

# * Defining

parser = argparse.ArgumentParser(description='Make a project from a template.')

parser.add_argument('project_name', type=str,
                    help='stores name of the project')

parser.add_argument('--database', '-d', action='store_const',
                    const=True, default=False, help='is a database required')

args = parser.parse_args()

projectDirectory = pathlib.Path.cwd() / args.project_name
if args.database:
    projectDirectory = projectDirectory / 'Database'

projectDirectory.mkdir(parents=True, exist_ok=False)

files = {
    'main.py':
    '''
"""
STATUS:
OVERVIEW:
IMPROVEMENTS:
Workings:
"""

# @ Imports

# * Defining

# ? Implementation
if __name__ == "__main__":
   print("Hello world!")

''',
    'README.md':
    '''# PROJECT NAME

[DESCRIPTION]

## USES

## EXTRA

## DOCS
'''
}

if args.database:
    projectDirectory = projectDirectory.parent

for file, template in files.items():
    fpath = projectDirectory / file
    with fpath.open(mode='w') as dir:
        dir.write(template)

# ? Implementation
if __name__ == "__main__":
    print('Project: ', projectDirectory, 'successfully made!')
