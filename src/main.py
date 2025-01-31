import os
import shutil

from copystatic import copy_directory_recursive

dir_path_static = "./static"
dir_path_public = "./public"

def main():


    if os.path.exists(dir_path_public):
        print(f"found {dir_path_public} directory, deleting")
        shutil.rmtree(dir_path_public)
    
    os.mkdir(dir_path_public)
    copy_directory_recursive(dir_path_static, dir_path_public)
    print("completed copy recursion")

    pass




main()