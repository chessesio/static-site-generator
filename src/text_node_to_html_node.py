from htmlnode import LeafNode
from textnode import TextType

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
        return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
    if text_node.text_type is TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"url":text_node.url, "alt":text_node.text})
