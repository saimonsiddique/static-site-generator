import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "abc.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"abc.com")
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD, "abc.com")
        node2 = TextNode("This is a text node", TextType.ITALIC,"xyz.com")
        self.assertNotEqual(node, node2)
    
    def test_eq_false_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node 2", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_text_node_to_htm_node(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node.text_node_to_htm_node().to_html(), "<b>This is a text node</b>")

if __name__ == "__main__":
    unittest.main()