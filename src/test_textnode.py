import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_same_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "url.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "url.com")
        self.assertEqual(node1, node2)
    
    def test_not_eq_dif_style(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_dif_text(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is also a text node", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_eq_dif_url(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT, "url.com")
        self.assertNotEqual(node1, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        # def more tests for converting text nodes to leaf nodes
        # final lesson of section 2

if __name__ == "__main__":
    unittest.main()