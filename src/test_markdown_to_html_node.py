import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here
    
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = "# Heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Heading</h1></div>")

        md1 = """
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
###### Heading 5
###### Heading 6
"""
        node1 = markdown_to_html_node(md1)
        html1 = node1.to_html()
        self.assertEqual(
            html1,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h6>Heading 5</h6><h6>Heading 6</h6></div>",
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2 with **bold** text
- Item 3 with _italic_ text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2 with <b>bold</b> text</li><li>Item 3 with <i>italic</i> text</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item with `code`
3. Third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <code>code</code></li><li>Third item</li></ol></div>",
        )

    def test_blockquote(self):
        md = """
> This is a blockquote with **bold** text and _italic_ text.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is a blockquote with <b>bold</b> text and <i>italic</i> text.</p></blockquote></div>",
        )

    def test_mixed_content(self):
        md = """
# Heading
```
def hello():
    print("Hello, World!")
```     
> This is a blockquote.
- List item 1
- List item 2 with `inline code`
This is a **paragraph** with _italic_ text.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1><pre><code>def hello():\n    print(\"Hello, World!\")\n</code></pre><blockquote><p>This is a blockquote.</p></blockquote><ul><li>List item 1</li><li>List item 2 with <code>inline code</code></li></ul><p>This is a <b>paragraph</b> with <i>italic</i> text.</p></div>",
        )

    def test_empty_markdown(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")

if __name__ == "__main__":
    unittest.main()

                