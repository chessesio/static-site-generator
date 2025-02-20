import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_not_eq(self):
        node = HTMLNode("<p>", "A HTML node test")
        node2 = HTMLNode("<a>", "Another HTML node test")
        self.assertNotEqual(node, node2)

    def test_is(self):
        node = HTMLNode("<p>", "A HTML node test")
        node2 = node
        self.assertIs(node, node2)

    def test_false(self):
        node = HTMLNode("<body>", "A HTML node test")
        node2 = HTMLNode("<body>", "Another HTML node test")
        self.assertTrue(node.tag == node2.tag, "Nodes have the same tag")

    def test_LeafNode(self):
        node = LeafNode(value="Hello World!", tag="h1", props={"font-family": "Arial"})
        self.assertEqual(node.to_html(), "<h1 font-family=Arial>Hello World!</h1>")


class TestParentNode(unittest.TestCase):
    node = ParentNode(
        tag="p",
        children=[
            LeafNode(tag="b", value="Bold text"),
            LeafNode(tag=None, value="Normal text"),
            LeafNode(tag="i", value="italic text"),
            LeafNode(tag=None, value="Normal text"),
        ],
        props={"font-family": "Arial"},
    )

    def test_output(self):
        self.assertEqual(self.node.to_html(), '<p font-family=Arial><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')


if __name__ == "__main__":
    unittest.main()
