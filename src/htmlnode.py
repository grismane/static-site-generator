class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # tag == None       renders as raw text
        self.value = value          # value == None     assume has children
        self.children = children    # children == None  assume has a value
        self.props = props          # props == None     no attributes

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        # return a string that represents the HTML attributes of the node
        if self.props == None:
            return ""
        props_str = ''
        for i in self.props:
            props_str += f' {i}="{self.props[i]}"'
        return props_str
    
    def __eq__(self, node):
        if not isinstance(node, HTMLNode):
            return False
        # Check if one has children and the other doesn't
        if (self.children is None) != (node.children is None):
            return False
        return (self.tag == node.tag) and (self.value == node.value) and (self.children == node.children) and (self.props == node.props)
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        # render leaf node as an HTML string (return a str)
        
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        elif self.tag == "img":
            return f'<img src="{self.props["src"]}" alt="{self.value}" />'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    # tag and children args are not optional
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode requires a tag")
        elif self.children == None:
            raise ValueError("ParentNode requires child node(s)")
        else:
            big_str = ""
            for child in self.children:
                big_str += child.to_html()
            if self.tag == "img":
                return f'<img src="{self.props["src"]}" alt="{big_str}" />'
            else:
                return f'<{self.tag}{self.props_to_html()}>{big_str}</{self.tag}>'