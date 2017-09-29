import os


def ls(path='.'):
    out = os.listdir(path)
    out = '\n'.join(out)
    print(out)


def cat(file_name):
    with open(file_name) as f:
        print(f.read())


def pwd():
    print(os.getcwd())


def cd(path):
    os.chdir(path)


def rm(*args):
    if len(args) == 0:
        args = args[0].split()

    for path in args:
        try:
            os.remove(path)
        except OSError:
            if '-r' in args:
                os.rmdir(path)
            else:
                raise OSError(path + 'is a directory')


def mkdir(path):
    os.mkdir(path)


def mv(old_path, new_path):
    os.rename(old_path, new_path)
