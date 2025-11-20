from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    nodes = [TextNode(TextType.TEXT, text)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = [n for n in nodes if not (n.text_type == TextType.TEXT and n.text == "")] 
    return nodes
