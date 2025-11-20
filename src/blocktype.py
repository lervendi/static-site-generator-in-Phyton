from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return "code"

    if re.match(r"^#{1,6} ", block):
        return "heading"
    
    lines = block.split("\n")
    stripped = [l.strip() for l in lines if l.strip() != ""]

    # Quote
    if stripped and all(l.startswith("> ") for l in stripped):
        return "quote"

    # Ordered list: 1. , 2. , 3. ...
    ok = True
    for expected, line in enumerate(stripped, start=1):
        m = re.match(r"^(\d+)\. ", line)
        if not m or int(m.group(1)) != expected:
            ok = False
            break
    if ok and stripped:
        return "ordered_list"

    # Unordered list: - item / * item
    if stripped and all(l.startswith("- ") or l.startswith("* ") for l in stripped):
        return "unordered_list"

    # Otherwise = paragraph
    return "paragraph"
