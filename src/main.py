import os
import shutil
import sys

from copystatic import copy_files
from generate_html import generate_pages_recursive

path_static = "./static"
path_public = "./docs"
path_template = "./template.html"
path_content = "./content"
default_basepath = "/"


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'

    print("Deleting public directory... ")
    if os.path.exists(path_public):
        shutil.rmtree(path_public)

    print("Copying static files to public directory... ")
    copy_files(path_static, path_public)

    print("Generating pages... ")
    generate_pages_recursive(path_content, path_template, path_public, basepath)


main()
