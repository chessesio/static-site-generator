import unittest

from inline_markdown import (extract_markdown_image, extract_markdown_link,
                             extract_title, split_nodes_delimiter,
                             split_nodes_image, split_nodes_link,
                             text_to_textnodes)
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("This is text with a **bold** word", TextType.TEXT)
    node3 = TextNode(
        "This is text with an image of ![boot dev](https://www.boot.dev) and ![youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    node4 = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )

    def test_split_nodes_delimiter(self):
        self.assertEqual(
            "This is text with a ",
            split_nodes_delimiter([self.node1], "`", TextType.CODE)[0].text,
        )
        self.assertEqual(
            TextType.BOLD,
            split_nodes_delimiter([self.node2], "**", TextType.BOLD)[1].text_type,
        )

    def test_split_nodes_image(self):
        self.assertEqual(
            "This is text with an image of ", split_nodes_image([self.node3])[0].text
        )
        self.assertEqual(TextType.IMAGE, split_nodes_image([self.node3])[1].text_type)

    def test_split_nodes_links(self):
        self.assertEqual(
            "This is text with a link ", split_nodes_link([self.node4])[0].text
        )
        self.assertEqual(TextType.LINK, split_nodes_link([self.node4])[1].text_type)


class TestImageAndLinkExtractor(unittest.TestCase):
    def testImageExtraction(self):
        text_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            extract_markdown_image(text_image),
        )

    def testLinkExtraction(self):
        text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            extract_markdown_link(text_link),
        )


class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        input_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output_ = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(input_text), output_)


class TestExtactTitleSuccess(unittest.TestCase):
    def test_extract_title(self):
        markdown = """# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.
"""
        title = extract_title(markdown)
        print(f"title = {title}")
        self.assertEqual(title, "Tolkien Fan Club")


    def test_extract_title_exception(self):
        markdown = """
        # Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.
"""
        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
