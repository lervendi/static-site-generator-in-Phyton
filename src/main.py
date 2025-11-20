from copy_content import sync_static_public, copy_content
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    sync_static_public("static", "docs")
    generate_page("content/index.md", "template.html", "docs/index.html", basepath)
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()