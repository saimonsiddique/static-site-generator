def markdown_to_blocks(markdown):
    blocks = []
    bullets_points = []
    for line in markdown.split('\n'):
        line = line.strip()
        if line.startswith('#'):
            blocks.append(f'# {line[1:].strip()}')
        elif line.startswith('*'):
            bullets_points.append(f'* {line[1:].strip()}')
        else:
            blocks.append(line)

    if bullets_points:
        blocks.append('\n'.join(bullets_points))
    return list(filter(None, blocks))

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return 'heading'
    if block.startswith('```') and block.endswith('```'):
        return 'code'
    if all(line.startswith('>') for line in block.split('\n')):
        return 'quote'
    if all(line.startswith(('* ', '- ')) for line in block.split('\n') if line):
        return 'unordered_list'
    if all(str(i+1) + '. ' in line for i, line in enumerate(block.split('\n')) if line):
        return 'ordered_list'
    return 'paragraph'


if __name__ == '__main__':
    text = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item
    """
    print(markdown_to_blocks(text))