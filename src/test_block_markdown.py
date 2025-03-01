import unittest

from block_markdown import BlockTypes, block_to_blocktype, markdown_to_blocks


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
        print(f"------\n{blocks}\n--------")
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
            BlockTypes.HEADING,
            BlockTypes.PARAGRAPH,
            BlockTypes.UNORDERED_LIST,
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
            BlockTypes.HEADING,
            BlockTypes.PARAGRAPH,
            BlockTypes.ORDERED_LIST,
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


if __name__ == "__main__":
    unittest.main()
