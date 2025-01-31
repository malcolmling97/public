import os
import shutil

def copy_directory_recursive(src_path, dest_path):
    
    # Checks if directory exists
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for filename in os.listdir(src_path):
        from_path = os.path.join(src_path,filename)
        to_path = os.path.join(dest_path, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path,to_path)
        else:
            copy_directory_recursive(from_path,to_path)
