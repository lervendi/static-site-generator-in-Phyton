import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line
    
    - This is a list
    - with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_single_block(self):
              md = "just a single paragraph"
              expected = ["just a single paragraph"]
              self.assertEqual(expected, markdown_to_blocks(md))

        def test_extra_empty_block(self):
              md = """! Heading


              Paragraph
              """
              blocks = markdown_to_blocks(md)
              self.assertEqual(blocks,
                               [
                                     "! Heading",
                                     "Paragraph"  
                               ])
        
        def test_spaces_at_the_edges(self):
              md = """   # Heading  
              
                Text with spaces.    
              """
              blocks = markdown_to_blocks(md)
              self.assertEqual(blocks, [
                    "# Heading",
                    "Text with spaces."
              ])

        def test_emptiness(self):
              md = ""
              blocks = markdown_to_blocks(md)
              self.assertEqual(blocks, [])

if __name__ == "__main__":
      unittest.main()

