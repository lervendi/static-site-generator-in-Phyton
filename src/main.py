from copy_content import sync_static_public, copy_content
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
def main():

    sync_static_public("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")

    generate_pages_recursive("content", "template.html", "public")
main()