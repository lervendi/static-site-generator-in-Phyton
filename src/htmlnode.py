


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        result = ""
        for key, val in self.props.items():
            result += f' {key}="{val}"'
        
        return result
        #return f" href={self.props["href"]} target={self.props.get("target")}" if self.props else ""
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    VOID_TAGS = {"img", "br", "hr", "input", "meta", "link"}

    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag is None:
            if self.value is None:
                raise ValueError("LeafNode must have a value to convert to HTML")
            return self.value

        props_str = self.props_to_html()

        if self.tag in self.VOID_TAGS:
            return f"<{self.tag}{props_str}>"
        
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")
        super().__init__(tag=tag, value=None, children=children, props=props)   

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if self.children is None:
            raise ValueError("ParentNode must have children to convert to HTML")
        
        props_str = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
    
    

