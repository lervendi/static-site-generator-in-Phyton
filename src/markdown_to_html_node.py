from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode, HTMLNode, LeafNode
from text_to_textnodes import text_to_textnodes
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        blocktype = block_to_block_type(block)

        if blocktype == "quote":
            text = ""
            block1 = block.split("\n")
            for b in block1:
                b = b.strip()
                if b.startswith("> "):
                    b = b[2:]

                if not b or b == ">":
                    continue
                text += b + " "
            text = text.strip()

            children = text_to_children(text)
            html_node = ParentNode(tag="blockquote", children=children)
            html_nodes.append(html_node)

        elif blocktype == "paragraph":
            lines = block.split("\n")
            text = " ".join(l.strip() for l in lines if l.strip() != "")
            children = text_to_children(text)
            html_node = ParentNode(tag="p", children=children)
            html_nodes.append(html_node)



        elif blocktype == "unordered_list":
            block1 = block.split("\n")
            html_node = ParentNode(tag="ul", children=[])
            for b in block1:
                b = b.strip()
                if b.startswith("- ") or b.startswith("* "):
                    b = b[2:]
                if b == "":
                    continue
                children = text_to_children(b)
                li_node = ParentNode(tag="li", children=children) 
                html_node.children.append(li_node)
            html_nodes.append(html_node)
                
        elif blocktype == "ordered_list":
            block1 = block.split("\n")
            html_node = ParentNode(tag="ol", children=[])
            for b in block1:
                b = b.strip()
                match = re.match(r"^\d+\. ", b)
                if match:
                    b = b[len(match.group(0)):]
                if b == "":
                    continue
                children = text_to_children(b)
                li_node = ParentNode(tag="li",children=children)
                html_node.children.append(li_node)
            html_nodes.append(html_node)

        elif blocktype == "code":
            block1 = block.split("\n")
            block1 = block1[1:-1]
            text = ""
            for b in block1:
                text += b
                text += "\n"
            code_node = LeafNode(tag="code", value=text)
            html_node = ParentNode(tag="pre", children=[code_node])
            html_nodes.append(html_node)
        
        elif blocktype == "heading":
            lines = block.split("\n")
            for line in lines:
                match = re.match(r"^(#{1,6}) (.*)", line)
                if match:
                    level = len(match.group(1))
                    text = match.group(2)
                    children = text_to_children(text)
                    tag = f"h{level}"
                    html_node = ParentNode(tag=tag, children=children)
                    html_nodes.append(html_node)

    return ParentNode(tag="div", children=html_nodes)

        


def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for textnode in text_nodes:
        children.append(text_node_to_html_node(textnode))

    return children