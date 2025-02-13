from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, compare_text_node):
        return (self.text == compare_text_node.text and 
                self.text_type == compare_text_node.text_type and 
                self.url == compare_text_node.url
              )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_htm_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(value=self.text)
            case TextType.BOLD:
                return LeafNode(tag='b', value=self.text)
            case TextType.ITALIC:
                return LeafNode(tag='i', value=self.text)
            case TextType.CODE:
                return LeafNode(tag='code', value=self.text)
            case TextType.LINKS:
                return LeafNode(tag='a', value=self.text, props={'href': self.url})
            case TextType.IMAGES:
                return LeafNode(tag='img', props={'src': self.url})
            case _:
                raise ValueError("Invalid text type")
