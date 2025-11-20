import unittest


from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_noteq_url(self):
        node = TextNode("OpenAI", TextType.LINK, url="https://www.openai.com")
        node2 = TextNode("OpenAI", TextType.LINK, url="https://www.example.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode(TextType.TEXT, "This is a text node")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_basic(self):
        tn = TextNode(TextType.TEXT, "hello")
        assert text_node_to_html_node(tn).to_html() == "hello"

    def test_bold(self):
        tn = TextNode(TextType.BOLD, "x")
        assert text_node_to_html_node(tn).to_html() == "<b>x</b>"

    def test_link_ok(self):
        tn = TextNode(TextType.LINK, "site", "https://ex.com")
        assert text_node_to_html_node(tn).to_html() == '<a href="https://ex.com">site</a>'

    def test_link_no_url(self):
        tn = TextNode("site", TextType.LINK, None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn)

    def test_img_ok(self):
        tn = TextNode(TextType.IMAGE, "logo", "/logo.png")
        assert text_node_to_html_node(tn).to_html() == '<img src="/logo.png" alt="logo">'

    def test_img_empty_alt(self):
        tn = TextNode(TextType.IMAGE, None, "/logo.png")
        assert text_node_to_html_node(tn).to_html() == '<img src="/logo.png" alt="">'


if __name__ == "__main__":
    unittest.main()