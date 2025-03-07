import os

from block_markdown import markdown_to_html_node
from inline_markdown import extract_title
from pathlib import Path


def generate_pages_recursive(dir_path_content, template_path, dir_destination_path, basepath):
    for path in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, path)
        destination_path = os.path.join(dir_destination_path, path)
        if os.path.isfile(from_path):
            destination_path = Path(destination_path).with_suffix(".html")
            generate_page(from_path, template_path, destination_path, basepath)
        else:
            print(from_path)
            generate_pages_recursive(from_path, template_path, destination_path, basepath)


def generate_page(from_path, template_path, destination_path, basepath):
    print(
        f"Generating page from {from_path} to {destination_path} using {template_path}"
    )
    md_text = get_text(from_path)
    html_template = get_text(template_path)

    html_title = extract_title(md_text)
    html_text = markdown_to_html_node(md_text).to_html()
    html_template = html_template.replace("{{ Title }}", html_title)
    html_template = html_template.replace("{{ Content }}", html_text)

    destination_dir_path = os.path.dirname(destination_path)

    if destination_dir_path != "":
        os.makedirs(destination_dir_path, exist_ok=True)
    to_file = open(destination_path, "w")
    to_file.write(html_template)


def get_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
