from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # lists used to collect loop outputs
    initial = []
    delimited = []
    new_nodes = []

    # loop through old_nodes to get a node to parse
    for node in old_nodes:
        # split text attribute into list to get single word for inspection
        text = node.text.split()
        # loop through each word and inspect for delimiter
        for index in range(len(text)):
            # check for leading delimiter
            if text[index][: len(delimiter)] == delimiter:
                # append leader to the delimiter bucket
                delimited.append(text[index].strip(f"{delimiter}"))
                # initialize new TextNode for text preceding delimited text and add it to the new_nodes list
                if len(initial) > 0:
                    # append empty string to add space at the end when joining
                    initial.append("")
                    new_nodes.append(TextNode(" ".join(initial), TextType.TEXT))
                if text[index][-len(delimiter) :] == delimiter:
                    new_nodes.append(
                        TextNode(text[index].strip(f"{delimiter}"), text_type)
                    )
                    new_nodes.append(
                        TextNode(" " + " ".join(text[index + 1 :]), TextType.TEXT)
                    )
                    return new_nodes
                else:
                    remainder = text[index + 1 :]
                    for index in range(len(remainder)):
                        if remainder[index][-len(delimiter) :] == delimiter:
                            delimited.append(remainder[index].strip(f"{delimiter}"))
                            new_nodes.append(TextNode(" ".join(delimited), text_type))
                            new_nodes.append(
                                TextNode(
                                    " " + " ".join(remainder[index + 1 :]),
                                    TextType.TEXT,
                                )
                            )
                            return new_nodes
                        else:
                            delimited.append(remainder[index])

            else:
                initial.append(text[index])

        if len(new_nodes) > 0:
            return new_nodes

    return old_nodes
