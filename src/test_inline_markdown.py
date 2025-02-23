import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a **bold** word", TextType.TEXT)
        # node3 = TextNode("This is text with an *italic* word", TextType.TEXT)

        self.assertEqual(
            "This is text with a ",
            split_nodes_delimiter([node1], "`", TextType.CODE)[0].text,
        )
        self.assertEqual(
            TextType.BOLD,
            split_nodes_delimiter([node2], "**", TextType.BOLD)[1].text_type,
        )


if __name__ == "__main__":
    unittest.main()
