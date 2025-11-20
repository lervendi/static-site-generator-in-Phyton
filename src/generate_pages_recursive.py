import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    names_list = os.listdir(dir_path_content)
    for name in names_list:
        src_path = os.path.join(dir_path_content, name)
        dest_path = os.path.join(dest_dir_path, name)
        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_path)
        elif name.endswith(".md"):
            dest_path1 = dest_path[:-3] + ".html"
            generate_page(src_path, template_path, dest_path1)
