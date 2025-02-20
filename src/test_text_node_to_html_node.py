import unittest

from htmlnode import LeafNode
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    leaf_node_ = LeafNode(tag="b", value="Bold Text")
    text_node_ = TextNode(text="Bold Text", text_type=TextType.BOLD)

    def test_bold_text_type(self):
        self.assertEqual(
            self.leaf_node_.tag, text_node_to_html_node(self.text_node_.tag)
        )
