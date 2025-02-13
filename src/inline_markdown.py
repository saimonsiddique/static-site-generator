from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_node_list = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
       new_node_list.append(node)
       continue
    else:
      split_nodes = []
      split_text_sections = node.text.split(delimiter)
      if len(split_text_sections) % 2 == 0:
        raise ValueError("invalid markdown, formatted section not closed")
      for i, text in enumerate(split_text_sections):
        if text == "":
          continue
        if i % 2 == 0:
          split_nodes.append(TextNode(text, TextType.TEXT))
        else:
          split_nodes.append(TextNode(text, text_type))
    new_node_list.extend(split_nodes)
  return new_node_list

def extract_markdown_images(text):
  return re.findall(r'!\[([^\]]*)\]\(([^\)]*)\)', text)

def extract_markdown_links(text):
  return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

if __name__ == "__main__":
  node = TextNode("This is text with a **bolded** word and **another**", TextType.TEXT)
  new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
  print(new_nodes)

  text1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
  print(extract_markdown_links(text1))
  # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

  text2 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
  print(extract_markdown_images(text2))
  # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]