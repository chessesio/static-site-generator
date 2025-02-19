import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()
