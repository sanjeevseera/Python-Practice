import os

print(os.getcwd())
print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))
print(os.path.isfile("os_module.py"))
print(os.listdir())
os.chdir("D:/My Data/Python/workspace/Practice_exercise/src/python-basic/Part1/")
print(os.getcwd())
os.chdir("D:/My Data/Python/workspace/Practice_exercise/src/python-basic/")
if 'temp' in os.listdir() and os.path.isdir('temp'):
    os.rmdir('temp')
    # os.removedirs(<dir>)  remove all directories within a directory
    print('rmdir')
else:
    os.mkdir('temp')
    # os.makedirs(/<dir>/<dir>/<dir>) create with parent directory
    print('mkdir')

print(os.listdir())