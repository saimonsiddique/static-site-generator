from textnode import TextNode, TextType

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

if __name__ == "__main__":
  node = TextNode("This is text with a **bolded** word and **another**", TextType.TEXT)
  new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
  print(new_nodes)