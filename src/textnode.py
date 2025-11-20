from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


def text_node_to_html_node(text_node):
    if not hasattr(text_node, "text_type"):
        raise TypeError("text_node_to_html_node expects a TextNode-like object")

    # пустая строка безопаснее, чем None, для не-void тегов
    txt = "" if text_node.text is None else text_node.text

    tt = text_node.text_type
    if tt == TextType.TEXT:
        return LeafNode(value=txt)

    if tt == TextType.BOLD:
        return LeafNode(tag="b", value=txt)

    if tt == TextType.ITALIC:
        return LeafNode(tag="i", value=txt)

    if tt == TextType.CODE:
        return LeafNode(tag="code", value=txt)

    if tt == TextType.LINK:
        if not text_node.url:
            raise ValueError("Link TextNode must have a URL")
        return LeafNode(tag="a", value=txt, props={"href": text_node.url})

    if tt == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Image TextNode must have a URL")
        # value НЕ передаём — img это void-тег
        alt = txt if txt is not None else ""
        return LeafNode(tag="img", props={"src": text_node.url, "alt": alt})

    raise ValueError(f"Unsupported TextType: {tt}")


class TextNode:
    def __init__(self, text_type=TextType.TEXT, text="", url=None):
        self.text_type = text_type
        self.text = text
        self.url = url

    def __eq__(self, other: "TextNode") -> bool:
        return (
            isinstance(other, TextNode) and
            self.text_type == other.text_type and
            self.text == other.text and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"
