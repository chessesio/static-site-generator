import os
import shutil

from copystatic import copy_files
from generate_html import generate_pages_recursive, generate_html

path_static = "./static"
path_public = "./public"
path_template = "./template.html"
path_content = "./content"


def main():
    print("Deleting public directory... ")
    if os.path.exists(path_public):
        shutil.rmtree(path_public)

    print("Copying static files to public directory... ")
    copy_files(path_static, path_public)

    print("Generating pages... ")
    #generate_html(
        #os.path.join(path_content, "index.md"),
        #path_template,
        #os.path.join(path_public, "index.html"),
    #)
    generate_pages_recursive(path_content, path_template, path_public)


main()
