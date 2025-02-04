from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag: str = None, value: str = None):
    super().__init__()
    self.value = value
    self.tag = tag
  
  def to_html(self):
    if self.value is None:
      raise ValueError("All leaf nodes must have a value")
    elif self.tag is None:
      return self.value
    return f"<{self.tag}>{self.value}</{self.tag}>"