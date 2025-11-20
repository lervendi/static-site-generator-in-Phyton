from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if not old_nodes:
        return []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        else:
            parts = node.text.split(delimiter)

            if len(parts) % 2 == 0:
                raise ValueError(f"unpaired delimiter {delimiter}.")
            
            for i, part in enumerate(parts):
                if part == "":
                    continue
                if i % 2 == 0:
                    new_node = TextNode(TextType.TEXT, part)
                else:
                    new_node = TextNode(text_type, part)

                new_nodes.append(new_node)
    return new_nodes