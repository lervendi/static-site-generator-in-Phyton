from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    
    node = markdown_to_html_node(markdown)
    html_node = node.to_html()
    title = extract_title(markdown)

    new_template = template.replace("{{ Title }}", title)
    new_template1 = new_template.replace("{{ Content }}", html_node)

    new_template1 = new_template1.replace('href="/', f'href="{basepath}')
    new_template1 = new_template1.replace('src="/', f'src="{basepath}')


    folder = os.path.dirname(dest_path)
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_template1)
    




    