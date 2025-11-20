import unittest

from markdown_utils import extract_markdown_images, extract_markdown_links

class TestMardownUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], 
            matches
        )

    def test_empty_img(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_link_not_an_image(self):
        matches = extract_markdown_links(
            "This is text with an ![not an image](https://i.imgur.com/zjjcJKZ.png) and a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")], 
            matches
        )

    def test_image_not_a_link(self):
        matches = extract_markdown_images(
            "This is text with an ![an image](https://i.imgur.com/zjjcJKZ.png) and a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("an image", "https://i.imgur.com/zjjcJKZ.png")], 
            matches
        )
    
    def test_no_matches(self):
        matches_img = extract_markdown_images(
            "This is text with no images."
        )
        matches_link = extract_markdown_links(
            "This is text with no links."
        )
        self.assertListEqual([], matches_img)
        self.assertListEqual([], matches_link)

    def test_punctuation(self):
        matches = extract_markdown_links(
            "Check this out: [example](https://example.com). It's great!"
        )
        self.assertListEqual(
            [("example", "https://example.com")], 
            matches
        )

    def test_dofferent_URL_formats(self):
        matches = extract_markdown_links(
            "Links: ![a](http://x/a) and ![b](https://x/b) and [c](mailto:user@example.com)"
        )
        self.assertListEqual(
            [("c", "mailto:user@example.com")],
            matches
        )

    def test_broken_markdown(self):
        matches_img = extract_markdown_images(
            "![broken(https://x.png]"
        )
        matches_link = extract_markdown_links(
            "Broken link [link text](missing-end"
        )
        self.assertListEqual([], matches_img)
        self.assertListEqual([], matches_link)

    if __name__ == "__main__":
        unittest.main()