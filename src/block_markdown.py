from enum import Enum

from inline_markdown import text_to_textnodes


class BlockTypes(Enum):
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
        return BlockTypes.HEADING
    if block[:3] == "```" and block[-3:] == "```":
        return BlockTypes.CODE
    if block[0] == ">":
        return BlockTypes.QUOTE
    if block[0] == "-":
        return BlockTypes.UNORDERED_LIST
    if block[0].isnumeric() and block[1] == "." and block[2] == " ":
        return BlockTypes.ORDERED_LIST

    return BlockTypes.PARAGRAPH
