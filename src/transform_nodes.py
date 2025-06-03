from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # takes a list of old nodes, a delimiter (beginning and end framing characters), and text type
    # returns a new list of nodes, splitting text up by type into nodes
    
    new_nodes = []
    for node in old_nodes:
        # iterate through old nodes list
        # for each node, determine if its text_type is TextType.TEXT
        if node.text_type != TextType.TEXT:
            # node's text_type is not TextType.TEXT:
            # add to the new_nodes list as is
            new_nodes.append(node)
        else:
            # node's text_type is TextType.TEXT:
            # node needs to be split if it contains the delimiter
            # check for unmatched delimiters and then splitting the text
            if node.text.count(delimiter) % 2 != 0:
                # uneven number of delimeters, effectively this is a syntax error
                raise Exception(f'No matching delimiter: {delimiter} in "{node.text}"')

            # split node string at the delimiters
            split_node_lst = node.text.split(delimiter)
            for i in range(len(split_node_lst)):
                #if split_node_lst[i] != "":
                    # skip null strs
                if (i % 2) == 0:
                    # every other str is the text_type associated with the delimiter
                    new_nodes.append(TextNode(split_node_lst[i], node.text_type))
                else:
                    new_nodes.append(TextNode(split_node_lst[i], text_type))
    return new_nodes
