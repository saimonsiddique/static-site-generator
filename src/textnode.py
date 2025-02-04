from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    NORMAL = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINKS = 5
    IMAGES = 6


class TextNode:
    def __init__(self, text, text_type, url):
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
            case TextType.NORMAL:
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
