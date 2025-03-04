from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    full_doc = markdown
    md_blocks = full_doc.split("\n\n")
    md_blocks = map(lambda item: item.strip(), md_blocks)
    md_blocks = list(filter(lambda item: False if item == "" else True, md_blocks))
    return md_blocks


def block_to_blocktype(block):
    if block[0] == "#":
        return BlockType.HEADING
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    if block[0] == ">":
        return BlockType.QUOTE
    if block[0] == "-":
        return BlockType.UNORDERED_LIST
    if block[0].isnumeric() and block[1] == "." and block[2] == " ":
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    tag = "div"
    children = []
    for block in blocks:
        children.append(create_parentnode(block))
    return ParentNode(tag, children)


# Helpter function to take block text and return a list of children html nodes
def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return children


# helper function to split unordered lists to children html nodes
def get_unordered_list_children(list_block):
    list_items = list_block.split("\n- ")
    children = []
    for item in list_items:
        children.append(ParentNode("li", text_to_children(item)))
    return children


# helper function to split ordered lists to children html nodes
def get_ordered_list_children(list_block):
    list_items = list_block.split("\n")
    children = []
    for item in list_items:
        children.append(ParentNode("li", text_to_children(item[3:])))
    return children


# Helper function to take children return their parent node of the respective type
def create_parentnode(block):
    block_type = block_to_blocktype(block)
    if block_type == BlockType.PARAGRAPH:
        tag = "p"
        children = text_to_children(block)
        return ParentNode(tag, children)
    if block_type == BlockType.HEADING:
        heading_num = len(block.split()[0])
        tag = f"h{heading_num}"
        text = block.strip("# ")
        children = text_to_children(text)
        return ParentNode(tag, children)
    if block_type == BlockType.UNORDERED_LIST:
        tag = "ul"
        children = get_unordered_list_children(block)
        return ParentNode(tag, children)
    if block_type == BlockType.ORDERED_LIST:
        tag = "ol"
        children = get_ordered_list_children(block)
        return ParentNode(tag, children)
    if block_type == BlockType.QUOTE:
        tag = "blockquote"
        text = block.strip("> ")
        children = text_to_children(text)
        return ParentNode(tag, children)
    if block_type == BlockType.CODE:
        tag = "code"
        text = block[3:-3]
        children = [text_node_to_html_node(TextNode(text, TextType.CODE))]
        return ParentNode(tag, children)
