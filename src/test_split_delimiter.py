import unittest

from textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter

class Test_split_delimiter(unittest.TestCase):
    def test_no_splits(self):
        node = TextNode(TextType.TEXT, "plain")
        expected = [TextNode(TextType.TEXT, "plain")]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.BOLD), expected)

    def test_single_formatted_block(self):
        node = TextNode(TextType.TEXT, "A 'x' B")
        expected = [
            TextNode(TextType.TEXT, "A "),
            TextNode(TextType.CODE, "x"),
            TextNode(TextType.TEXT, " B")
        ]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE),
                          expected
        )

    def test_multi_formatted_block(self):
        node = TextNode(TextType.TEXT, "this is 'multi' formatted 'block'")
        expected = [
            TextNode(TextType.TEXT, "this is "),
            TextNode(TextType.CODE, "multi"),
            TextNode(TextType.TEXT, " formatted "),
            TextNode(TextType.CODE, "block")
        ]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE),
                         expected
        )

    def test_unpaired_delimiter(self):
        node = TextNode(TextType.TEXT, "bad 'x")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "'", TextType.CODE)

    def test_empty_string(self):
        node = TextNode(TextType.TEXT, "")
        expected = []
        self.assertEqual(
            split_nodes_delimiter([node], "'", TextType.CODE),
            expected
        )

    def test_delimiter_first(self):
        node = TextNode(TextType.TEXT, "'x'")
        expected = [TextNode(TextType.CODE, "x")]
        self.assertEqual(
            split_nodes_delimiter([node], "'", TextType.CODE),
            expected
        )

    def test_two_formatted_in_a_raw(self):
        node = TextNode(TextType.TEXT, "'a''b'")
        expected = [
            TextNode(TextType.CODE, "a"),
            TextNode(TextType.CODE, "b")
        ]
        self.assertEqual(
            split_nodes_delimiter([node], "'", TextType.CODE),
            expected
        )

    def test_space(self):
        node = TextNode(TextType.TEXT, "' '")
        expected = [TextNode(TextType.CODE, " ")]
        self.assertEqual(
            split_nodes_delimiter([node], "'", TextType.CODE),
            expected
        )

    def test_non_text_node(self):
        node = TextNode(TextType.CODE, "print(1)")
        expected = [TextNode(TextType.CODE, "print(1)")]
        self.assertEqual(
            split_nodes_delimiter([node], "'", TextType.CODE),
            expected
        )

    def test_different_nodes(self):
        node = [
            TextNode(TextType.TEXT, "a 'i' b"),
            TextNode(TextType.CODE, "print(1)"),
            TextNode(TextType.TEXT, "j")
        ]
        expected = [
            TextNode(TextType.TEXT, "a "),
            TextNode(TextType.CODE, "i"),
            TextNode(TextType.TEXT, " b"),
            TextNode(TextType.CODE, "print(1)"),
            TextNode(TextType.TEXT, "j")
        ]
        self.assertEqual(
            split_nodes_delimiter(node, "'", TextType.CODE),
            expected
        )

    def test_two_different_delimiters(self):
        node = TextNode(TextType.TEXT, "foo 'x **not bold**' and **yes**")

        step1 = split_nodes_delimiter([node], "'", TextType.CODE)
        step2 = split_nodes_delimiter(step1, "**", TextType.BOLD)

        expected = [
            TextNode(TextType.TEXT, "foo "),
            TextNode(TextType.CODE, "x **not bold**"),
            TextNode(TextType.TEXT, " and "),
            TextNode(TextType.BOLD, "yes")
        ]

        self.assertEqual(step2, expected)



if __name__ == "__main__":
    unittest.main()

