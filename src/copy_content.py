import os
import shutil

def sync_static_public(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir, ignore_errors=True)
        os.makedirs(dest_dir)

    else:
        os.makedirs(dest_dir)

    copy_content(src_dir, dest_dir)


def copy_content(src_dir, dest_dir):

    items = os.listdir(src_dir)

    for item in items:
        full_src_path = os.path.join(src_dir, item)
        full_dest_path = os.path.join(dest_dir, item)

        if os.path.isdir(full_src_path):
            os.mkdir(full_dest_path)
            copy_content(full_src_path, full_dest_path)
            print(f"Directory copied: {full_src_path} to {full_dest_path}")
        else:
            shutil.copy(full_src_path, full_dest_path)
            print(f"File copied: {full_src_path} to {full_dest_path}")

if __name__ == "__main__":
    sync_static_public("static", "public")
            
        


    

    

