from textnode import TextNode, TextType
from markdown_utils import extract_markdown_images, extract_markdown_links
import re

def split_nodes_image(old_nodes):
    new_nodes = []
    if not old_nodes:
        return []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        pairs = extract_markdown_images(node.text)
        if not pairs:
            new_nodes.append(node)
            continue
        working = node.text

        for alt,url in pairs:
            left,working = working.split(f"![{alt}]({url})", 1)
            if left:
                new_nodes.append(TextNode(TextType.TEXT,left))
            new_nodes.append(TextNode(TextType.IMAGE,alt,url))
        if working:
            new_nodes.append(TextNode(TextType.TEXT,working))
        
    return new_nodes

        

def split_nodes_link(old_nodes):
    new_nodes = []
    if not old_nodes:
        return []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        image_split = split_nodes_image([node])

        for part in image_split:
            if part.text_type == TextType.IMAGE:
                new_nodes.append(part)
                continue

            pairs = extract_markdown_links(part.text)
            if not pairs:
                new_nodes.append(part)
                continue

            working = part.text
                    
            for anchor,url in pairs:
                left,working = working.split(f"[{anchor}]({url})", 1)
                if left:
                    new_nodes.append(TextNode(TextType.TEXT,left))
                new_nodes.append(TextNode(TextType.LINK,anchor,url))

            if working:
                new_nodes.append(TextNode(TextType.TEXT,working))
        
    return new_nodes

