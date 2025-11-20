import unittest
from textnode import TextNode,TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):
    def test_all_kindes_of_markdowns(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode(TextType.TEXT, "This is "),
            TextNode(TextType.BOLD, "text"),
            TextNode(TextType.TEXT," with an "),
            TextNode(TextType.ITALIC, "italic"),
            TextNode(TextType.TEXT, " word and a "),
            TextNode(TextType.CODE, "code block"),
            TextNode(TextType.TEXT, " and an "),
            TextNode(TextType.IMAGE, "obi wan image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(TextType.TEXT, " and a "),
            TextNode(TextType.LINK, "link", "https://boot.dev"),
            ]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_empty_string(self):
        text = ""
        expected = []
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_no_markdown(self):
        text = "This is a simple text without any markdown."
        expected = [TextNode(TextType.TEXT, text)]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_unpaired_delimiter(self):
        text = "This is **bold text with no ending delimiter."
        with self.assertRaises(ValueError):
            text_to_textnodes(text)
    
    def test_consecutive_markdowns(self):
        text = "**Bold**_Italic_`Code`"
        expected = [
            TextNode(TextType.BOLD, "Bold"),
            TextNode(TextType.ITALIC, "Italic"),
            TextNode(TextType.CODE, "Code"),
        ]
        self.assertListEqual(text_to_textnodes(text), expected)

if __name__ == "__main__":
    unittest.main()