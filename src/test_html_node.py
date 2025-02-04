import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestHTMLNode(unittest.TestCase):

  def test_initialization(self):
    node = HTMLNode(tag='div', value='Hello, World!')
    self.assertEqual(node.tag, 'div')
    self.assertEqual(node.value, 'Hello, World!')

  def test_props_to_html(self):
    node = HTMLNode(tag='a', value='Click me!', props={'href': 'https://www.boot.dev'})
    self.assertEqual(node.props_to_html(), 'href="https://www.boot.dev"')

  def test_leaf_node_initialization(self):
    node = LeafNode(value='Hello, World!')
    self.assertEqual(node.value, 'Hello, World!')

  def test_leaf_node_to_html(self):
    node = LeafNode(value='Hello, World!', tag='h1')
    self.assertEqual(node.to_html(), '<h1>Hello, World!</h1>')

  def test_parent_node_initialization(self):
    node = ParentNode(tag='div', children=[LeafNode(tag='span', value='Child')])
    self.assertEqual(node.tag, 'div')
    self.assertEqual(len(node.children), 1)
    self.assertEqual(node.children[0].tag, 'span')
    self.assertEqual(node.children[0].value, 'Child')

  def test_parent_node_to_html(self):
    node = ParentNode(
      tag='div',
      children=[
        LeafNode(tag='span', value='Child 1'),
        LeafNode(tag='span', value='Child 2')
      ]
    )
    self.assertEqual(node.to_html(), '<div><span>Child 1</span><span>Child 2</span></div>')

if __name__ == '__main__':
  unittest.main()