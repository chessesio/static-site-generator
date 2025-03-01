from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type is TextType.TEXT:
        return LeafNode(value=text_node.text)
    if text_node.text_type is TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type is TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type is TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type is TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type is TextType.IMAGE:
        return LeafNode(
            tag="img", value="", props={"url": text_node.url, "alt": text_node.text}
        )
