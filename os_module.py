import os
from datetime import datetime

# print(dir(os)) # print alle methods, etc from os
# print(os.listdir('C:/_LocalGit'))
# print(os.getcwd())
os.chdir('C:/_LocalGit/')
# os.makedirs('TEST/SUBTEST')
# os.rmdir('TEST/SUBTEST')
# os.removedirs('TEST/')
# os.mkdir('Test/')
os.chdir(os.path.join(os.getcwd(), 'Test'))
print(os.listdir(os.getcwd()))
# os.rename('newfile.txt', 'renamed.txt')
print(os.listdir(os.getcwd()))
time = datetime.fromtimestamp(os.stat('renamed.txt').st_mtime)


def list_dirs_files():
    for dirpath, dirnames, filenames in os.walk('D:/Intel'):
        print('Current Path:', dirpath)
        print('Directories:', dirnames)
        print('Files:', filenames, '\n')



file_path = os.path.join(os.environ.get('HOMEDRIVE'), 'test.txt')

path = 'C:/User/Path/test.txt'
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))
print(os.path.exists(path))
print(os.path.isdir(path), os.path.isfile(path))
print(os.path.splitext(path),'dd')

print(dir(datetime))