import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_same_ref(self):
        # tag, value, children, props
        nodechild = HTMLNode(tag="a", value="This is a link to google", props={"href": "https://www.google.com"})
        node1 = HTMLNode(children=nodechild)
        node2 = HTMLNode(children=nodechild)
        self.assertEqual(node1, node2)
    
    def test_eq(self):
        # tag, value, children, props
        node1 = HTMLNode(tag="a", value="This is a link to google", props={"href": "https://www.google.com"})
        node2 = HTMLNode(tag="a", value="This is a link to google", props={"href": "https://www.google.com"})
        self.assertEqual(node1, node2)

    def test_not_eq_child_no_child(self):
        nodechild = HTMLNode(tag="a", value="This is a link to google", props={"href": "https://www.google.com"})
        node1 = HTMLNode(children=nodechild)
        node2 = HTMLNode()
        # different children
        self.assertNotEqual(node1, node2)

    def test_not_eq_diff_child(self):
        nodechild = HTMLNode(tag="h1", value="This is a child node")
        node1 = HTMLNode(children=nodechild)
        node2 = HTMLNode()
        # different children
        self.assertNotEqual(node1, node2)

    def test_not_eq_diff_tag(self):
        node1 = HTMLNode(tag="h1", value="This is a test heading")
        node2 = HTMLNode(tag="h2", value="This is a test heading")
        # different tag
        self.assertNotEqual(node1, node2)

    def test_not_eq2(self):
        node1 = HTMLNode(tag="h1", value="This is a test heading")
        node2 = HTMLNode(tag="h1", value="This is also a test heading")
        # different value
        self.assertNotEqual(node1, node2)

    def test_not_eq3(self):
        node1 = HTMLNode(tag="a", value="This is a link to google", props={"href": "https://www.google.com"})
        node2 = HTMLNode(tag="a", value="This is a link to google", props={"href": "https://www.google.ca"})
        # different props
        self.assertNotEqual(node1, node2)

class TestLeafNode(unittest.TestCase):    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Google", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Google</a>')
    
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "Image", props={"src": "url/of/image.jpg"})
        self.assertEqual(node.to_html(), '<img src="url/of/image.jpg" alt="Image" />')
    
    def test_leaf_to_html_code(self):
        node = LeafNode("code", "Hello, world!")
        self.assertEqual(node.to_html(), "<code>Hello, world!</code>")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span></div>")
    
    def test_to_html_with_mixed_children(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node1 = ParentNode("span", [grandchild_node])
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span><span>child2</span></div>")

    def test_to_html_no_tag_value_err(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        # Use assertRaises to check if calling to_html() raises a ValueError
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        # Optionally, you can check the content of the error message
        self.assertEqual(str(cm.exception), "ParentNode requires a tag")

    def test_to_html_no_child_value_err(self):
        parent_node = ParentNode("span", None)
        # Use assertRaises to check if calling to_html() raises a ValueError
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        # Optionally, you can check the content of the error message
        self.assertEqual(str(cm.exception), "ParentNode requires child node(s)")
        

if __name__ == "__main__":
    unittest.main()