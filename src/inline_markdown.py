import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_image(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_link(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_image(text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            split_text = text.split(f"![{image[0]}]({image[1]})")
            if len(split_text) != 2:
                raise ValueError("Invalid input")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = split_text[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_link(text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            split_text = text.split(f"[{image[0]}]({image[1]})")
            if len(split_text) != 2:
                raise ValueError("Invalid input")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.LINK, image[1]))
            text = split_text[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    delimiters = {
        "**": TextType.BOLD,
        "__": TextType.BOLD,
        "*": TextType.ITALIC,
        "_": TextType.ITALIC,
        "```": TextType.CODE,
        "``": TextType.CODE,
        "`": TextType.CODE,
    }
    text_nodes = [TextNode(text, TextType.TEXT)]
    for delimiter in delimiters:
        text_nodes = split_nodes_delimiter(text_nodes, delimiter, delimiters[delimiter])
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes
