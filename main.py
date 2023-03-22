from mimetypes import guess_type
from fileinput import FileInput
from os import listdir, rename
from os.path import basename, dirname, isdir, join
from shutil import copytree
import easygui

root_path = easygui.diropenbox()

old = basename(root_path)
new = input('New name: ')

def files_rewrite(path: str, old_name: str, new_name: str) -> None:
    mime, _ = guess_type(path)
    if mime == "text/plain":
        with FileInput(path, inplace=True, encoding='utf-8') as file:
            for line in file:
                print(line.replace(old_name, new_name), end='')

def files_rename(base_path: str, old_name: str, new_name: str) -> None:
    files = listdir(base_path)

    for file in files:
        path = join(base_path, file)
        new_path = path.replace(old_name, new_name)

        if new_path != path:
            rename(path, new_path)

        if isdir(new_path):
            files_rename(new_path, old_name, new_name)

        else:
            files_rewrite(new_path, old_name, new_name)


copytree(join(dirname(root_path), old), join(dirname(root_path), new))
files_rename(join(dirname(root_path), new), old, new)