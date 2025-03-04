import unittest

from block_markdown import BlockType, block_to_blocktype, markdown_to_blocks, markdown_to_html_node


class TestMarkdownToBlocks(unittest.TestCase):
    def testmarkdowntoblocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )

    def test_block_to_unordered_list(self):
        markdown = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

        - This is the first list item in a list block
        - This is a list item
        - This is another list item
        """
        block_types = [
            BlockType.HEADING,
            BlockType.PARAGRAPH,
            BlockType.UNORDERED_LIST,
        ]

        self.assertEqual(
            block_types,
            list(
                map(
                    lambda block: block_to_blocktype(block),
                    markdown_to_blocks(markdown),
                )
            ),
        )

    def test_block_to_odered_list(self):
        markdown = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

        1. This is the first list item in a list block
        2. This is a list item
        3. This is another list item
        """
        block_types = [
            BlockType.HEADING,
            BlockType.PARAGRAPH,
            BlockType.ORDERED_LIST,
        ]

        self.assertEqual(
            block_types,
            list(
                map(
                    lambda block: block_to_blocktype(block),
                    markdown_to_blocks(markdown),
                )
            ),
        )

    def test_md_to_html(self):
        md = """
        This is **bolded** paragraph text in a p tag here

        This is another paragraph with _italic_ text and `code` here

        """
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")

if __name__ == "__main__":
    unittest.main()
