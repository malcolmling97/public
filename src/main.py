import os
import shutil

from copystatic import copy_directory_recursive
from generatepage import generate_page
from generatepage import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():


    if os.path.exists(dir_path_public):
        print(f"found {dir_path_public} directory, deleting")
        shutil.rmtree(dir_path_public)
    
    os.mkdir(dir_path_public)
    copy_directory_recursive(dir_path_static, dir_path_public)
    print("completed copy recursion")
    
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)



main()