import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self):
        markdown = "# My Title"
        title = extract_title(markdown)
        self.assertEqual(title, "My Title")

    def test_title_not_on_first_line(self):
        markdown = """
some text
# Actual Title
more text
"""
        title = extract_title(markdown)
        self.assertEqual(title, "Actual Title")

    def test_extra_spaces(self):
        markdown = "   #   Spaced Title   "
        title = extract_title(markdown)
        self.assertEqual(title, "Spaced Title")

    def test_no_title(self):
        markdown = """
some text
more text
"""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_not_a_title(self):
        markdown = "## Subtitle"
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()
    