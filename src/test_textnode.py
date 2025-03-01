import unittest

from textnode import LeafNode, TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_is_not(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNot(node, node2, "These nodes are not equal")


class TestTextNodeToHTML(unittest.TestCase):
    def test_bold_text_type(self):
        leaf_node_ = LeafNode(tag="b", value="Bold Text")
        text_node_ = TextNode(text="Bold Text", text_type=TextType.BOLD)
        self.assertEqual(leaf_node_.tag, text_node_to_html_node(text_node_).tag)


if __name__ == "__main__":
    unittest.main()
