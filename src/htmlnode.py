class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_self(self):
        raise NotImplementedError()

    def props_to_html(self):
        props_string = ""
        if self.props == None:
            return ""
        for prop in self.props:
            props_string += f" {prop}={self.props[prop]}"
        return props_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value=value, tag=tag, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value is required")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Attribute 'tag' is required")
        if self.children == None:
            raise ValueError("Attribute 'children' is required")
        # for every child in self.children, concatenate its html
        children_html = ""
        for child in self.children:
            children_html = children_html + child.to_html()
        if self.props == None:
            return f"<{self.tag}>{children_html}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
