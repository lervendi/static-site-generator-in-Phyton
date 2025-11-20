import unittest
from split_nodes import split_nodes_image,split_nodes_link
from textnode import TextType,TextNode

class TestSplitNodes(unittest.TestCase):
    # split_nodes_image tests
    def test_image_middle(self):
        node = TextNode(TextType.TEXT, "text ![cat](https://imgur.com/cat.png) more text")
        expected = [
            TextNode(TextType.TEXT, "text "),
            TextNode(TextType.IMAGE, "cat", "https://imgur.com/cat.png"),
            TextNode(TextType.TEXT," more text")
        ]
        self.assertListEqual(expected, split_nodes_image([node]))

    def test_two_images_in_a_raw(self):
        node = TextNode(TextType.TEXT, "![a](https://a)![b](https://b)")
        expected = [
            TextNode(TextType.IMAGE, "a", "https://a"),
            TextNode(TextType.IMAGE, "b", "https://b")
        ]
        self.assertListEqual(expected, split_nodes_image([node]))

    def test_image_at_start(self):
        node = TextNode(TextType.TEXT, "![start](https://start) text")
        expected = [
            TextNode(TextType.IMAGE, "start", "https://start"),
            TextNode(TextType.TEXT, " text")
        ]
        self.assertListEqual(expected, split_nodes_image([node]))

    def test_image_at_end(self):
        node = TextNode(TextType.TEXT, "text ![end](https://end)")
        expected = [
            TextNode(TextType.TEXT, "text "),
            TextNode(TextType.IMAGE, "end", "https://end")
        ]
        self.assertListEqual(expected, split_nodes_image([node]))
    
    def test_no_alt(self):
        node = TextNode(TextType.TEXT, "![](https://noalt)")
        expected = [
            TextNode(TextType.IMAGE, "", "https://noalt")
        ]
        self.assertListEqual(expected, split_nodes_image([node]))

    def test_multiple_images(self):
        node = TextNode(TextType.TEXT, "![a](https://a) text ![b](https://b) more ![](https://c)")
        expected = [
            TextNode(TextType.IMAGE, "a", "https://a"),
            TextNode(TextType.TEXT, " text "),
            TextNode(TextType.IMAGE, "b", "https://b"),
            TextNode(TextType.TEXT, " more "),
            TextNode(TextType.IMAGE, "", "https://c")
        ]
        self.assertListEqual(expected, split_nodes_image([node]))

    def test_not_image_texttype(self):
        node = TextNode(TextType.LINK, "[not an image](https://link)")
        expected = [TextNode(TextType.LINK, "[not an image](https://link)")]
        self.assertListEqual(expected, split_nodes_image([node]))

    #split_nodes_link tests
    def test_single_link(self):
        node = TextNode(TextType.TEXT, "This is a [link](https://example.com).")
        expected = [
            TextNode(TextType.TEXT, "This is a "),
            TextNode(TextType.LINK, "link", "https://example.com"),
            TextNode(TextType.TEXT, ".")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_two_links(self):
        node = TextNode(TextType.TEXT, "[first](https://first) and [second](https://second)")
        expected = [
            TextNode(TextType.LINK, "first", "https://first"),
            TextNode(TextType.TEXT, " and "),
            TextNode(TextType.LINK, "second", "https://second")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_link_at_start(self):
        node = TextNode(TextType.TEXT, "[start](https://start) of the text")
        expected = [
            TextNode(TextType.LINK, "start", "https://start"),
            TextNode(TextType.TEXT, " of the text")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_link_at_end(self):
        node = TextNode(TextType.TEXT, "End with a [link](https://end)")
        expected = [
            TextNode(TextType.TEXT, "End with a "),
            TextNode(TextType.LINK, "link", "https://end")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_no_links(self):
        node = TextNode(TextType.TEXT, "This text has no links.")
        expected = [TextNode(TextType.TEXT, "This text has no links.")]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_image_link_mix(self):
        node = TextNode(TextType.TEXT, "![image](https://imgur.com/img)[link](https://example.com)")
        expected = [
            TextNode(TextType.IMAGE, "image", "https://imgur.com/img"),
            TextNode(TextType.LINK, "link", "https://example.com")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_no_anchor_text(self):
        node = TextNode(TextType.TEXT, "[](/empty)")
        expected = [
            TextNode(TextType.LINK, "", "/empty")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_multiple_links(self):
        node = TextNode(TextType.TEXT, "[one](https://one)[two](https://two)[three](https://three)")
        expected = [
            TextNode(TextType.LINK, "one", "https://one"),
            TextNode(TextType.LINK, "two", "https://two"),
            TextNode(TextType.LINK, "three", "https://three")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_only_image(self):
        node = TextNode(TextType.TEXT, "![onlyimage](https://onlyimage)")
        expected = [
            TextNode(TextType.IMAGE, "onlyimage", "https://onlyimage")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))

    def test_unicode(self):
        node = TextNode(TextType.TEXT, "Check this [链接](https://例子.公司)")
        expected = [
            TextNode(TextType.TEXT, "Check this "),
            TextNode(TextType.LINK, "链接", "https://例子.公司")
        ]
        self.assertListEqual(expected, split_nodes_link([node]))
        

