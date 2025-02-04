from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
  def __init__(self, tag: str, children: list = [], props: dict = None):
    super().__init__(tag=tag, props=props)
    self.children = children
    self.tag = tag
    self.props = props
  

  def to_html(self):
    if self.tag is None:
      raise ValueError("All parent nodes must have a tag")
    elif len(self.children) == 0:
      raise ValueError("All parent nodes must have children")
    else:
      children = "".join([child.to_html() for child in self.children])
      return f"<{self.tag}>{children}</{self.tag}>"



if __name__ == "__main__":
  node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
  )

  print(node.to_html())