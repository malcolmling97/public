import os
import shutil

from copystatic import copy_directory_recursive
from generatepage import generate_page

dir_path_static = "./static"
dir_path_public = "./public"

dir_path_index_md = "./content/index.md"
dir_path_template_html = "./template.html"
dir_path_index_html = "./public/index.html"

def main():


    if os.path.exists(dir_path_public):
        print(f"found {dir_path_public} directory, deleting")
        shutil.rmtree(dir_path_public)
    
    os.mkdir(dir_path_public)
    copy_directory_recursive(dir_path_static, dir_path_public)
    print("completed copy recursion")

    generate_page("./content/index.md", "./template.html","./public/index.html")



main()