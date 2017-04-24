import sys
import os

removefiles_suffix = set(
    ['db', 'pdb', 'obj', 'log',  'sdf', 'idb', 'pch'])

removedirs_prefix = set(
    ['x64', 'x86', '.vs', 'obj', 'Debug', 'Release', 'build'])


def rmdir(path):
    if os.path.isfile(path):
        os.remove(path)
        print('del', path)
        return
    for sub in os.listdir(path):
        now = os.path.join(path, sub)
        rmdir(now)
    print('rm', path)
    os.rmdir(path)


def ask(s):
    return True

    print('will remove', s, '(y/s)')
    if input()[0] == 'y':
        return True
    return False


def processPath(path: str):
    if os.path.isdir(path):
        print('work on', path)
        root, now = os.path.split(path)
        if now == '':
            return
        for prefix in removedirs_prefix:
            if now == prefix:
                if ask(now):
                    rmdir(path)
                return
        for sub in os.listdir(path):
            processPath(os.path.join(path, sub))
    elif os.path.isfile(path):
        root, now = os.path.split(path)
        if len(now) > 2 and now[-2:] in removefiles_suffix:
            if ask(now):
                os.remove(path)
                print('del', path)
            return
        if len(now) > 3 and now[-3:] in removefiles_suffix:
            if ask(now):
                os.remove(path)
                print('del', path)
            return



if __name__ == '__main__':
    paths = []
    if len(os.sys.argv) == 1:
        paths.append(os.getcwd())
    else:
        for i in os.sys.argv[1:]:
            paths.append(i)
    for path in paths:
        processPath(path)
