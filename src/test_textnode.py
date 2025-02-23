import unittest

from textnode import TextNode, TextType, split_nodes_delimiter

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

    def test_split_nodes_delimiter(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a **bold** word", TextType.TEXT)
        #node3 = TextNode("This is text with an *italic* word", TextType.TEXT)

        self.assertEqual("This is text with a ", split_nodes_delimiter([node1], "`", TextType.CODE)[0].text)
        self.assertEqual(TextType.BOLD, split_nodes_delimiter([node2], "**", TextType.BOLD)[1].text_type)


if __name__ == "__main__":
    unittest.main()
