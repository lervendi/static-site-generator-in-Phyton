import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

        node2 = HTMLNode(props={"href": "https://www.example.com"})
        expected2 = ' href="https://www.example.com"'
        self.assertEqual(node2.props_to_html(), expected2)

        node3 = HTMLNode()
        expected3 = ""
        self.assertEqual(node3.props_to_html(), expected3)

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "container"})
        expected = "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'container'})"
        self.assertIn(expected, repr(node))

    def test_leafnode_to_html(self):
        node = LeafNode("p", "Hello, world!") 
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>") 
        
        node2 = LeafNode("a", "OpenAI", props={"href": "https://www.openai.com"}) 
        self.assertEqual(node2.to_html(), '<a href="https://www.openai.com">OpenAI</a>') 
        

    def test_leafnode_to_html_no_value(self):
        node = LeafNode("p") 
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leafnode_to_html_no_tag(self):
        node = LeafNode(value="Sample text") 
        self.assertEqual(node.to_html(), "Sample text")

    def test_leafnode_to_html_no_props(self):
        node = LeafNode("p", "Hello", {}) 
        self.assertEqual(node.to_html(), "<p>Hello</p>")

        node2 = LeafNode("p", "Hello", None)
        self.assertEqual(node2.to_html(), "<p>Hello</p>")

    def test_leafnode_multiple_props(self):
        props = {
            "href": "https://www.example.com",
            "target": "_blank",
            "class": "link-class"
        }
        node = LeafNode("a", "Example", props)
        html = node.to_html()

        self.assertIn('href="https://www.example.com"', html)
        self.assertIn('target="_blank"', html)
        self.assertIn('class="link-class"', html)
        self.assertTrue(html.startswith("<a "))
        self.assertTrue(html.endswith("</a>"))

    def test_leafnode_different_tags(self):
        node_img = LeafNode("img", "Image", {"src": "image.png", "alt": "An image"})
        self.assertEqual(node_img.to_html(), '<img src="image.png" alt="An image">')

        node_div = LeafNode("div", "Content", {"class": "container"})
        self.assertEqual(node_div.to_html(), '<div class="container">Content</div>')

    def test_leafnode_any_attributes(self):
        props = {
            "data-id": "123",
            "aria-label": "label",
            "hidden": "true"
        }

        node = LeafNode("span", "Text", props)
        html = node.to_html()
        self.assertIn('data-id="123"', html)
        self.assertIn('aria-label="label"', html)
        self.assertIn('hidden="true"', html)
        self.assertTrue(html.startswith("<span "))
        self.assertTrue(html.endswith("</span>"))

    def test_leafnode_repr(self):
        node = LeafNode(tag="p", value="Hello", props={"class": "text"})
        expected = "HTMLNode(tag=p, value=Hello, children=None, props={'class': 'text'})"
        self.assertIn(expected, repr(node))

    def test_leafnode_no_children(self):
        node = LeafNode(tag="p", value="Hello", props={"class": "text"})
        self.assertIsNone(node.children)

if __name__ == "__main__":
    unittest.main()
    

