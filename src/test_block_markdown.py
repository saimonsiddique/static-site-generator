import unittest
from block_mardown import (
  markdown_to_blocks,
  block_to_block_type  
)

class TestMarkdownToBlocks(unittest.TestCase):
  def text_markdown_to_blocks(self):
    text = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item
    """
    self.assertListEqual(
      [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
      ],
      markdown_to_blocks(text)
    )
  
  def test_block_to_block_type(self):
    self.assertEqual('heading', block_to_block_type('# This is a heading'))
    self.assertEqual('paragraph', block_to_block_type('This is a paragraph'))
    self.assertEqual('code', block_to_block_type('```This is a code block```'))
    self.assertEqual('quote', block_to_block_type('> This is a quote'))
    self.assertEqual('unordered_list', block_to_block_type('* This is a list item\n* This is another list item'))
    self.assertEqual('ordered_list', block_to_block_type('1. This is a list item\n2. This is another list item'))
    self.assertEqual('paragraph', block_to_block_type('This is a paragraph\n\nThis is another paragraph'))

    block = "# heading"
    self.assertEqual(block_to_block_type(block), 'heading')
    block = "```\ncode\n```"
    self.assertEqual(block_to_block_type(block), 'code')
    block = "> quote\n> more quote"
    self.assertEqual(block_to_block_type(block), 'quote')
    block = "* list\n* items"
    self.assertEqual(block_to_block_type(block), 'unordered_list')
    block = "1. list\n2. items"
    self.assertEqual(block_to_block_type(block), 'ordered_list')
    block = "paragraph"
    self.assertEqual(block_to_block_type(block), 'paragraph')