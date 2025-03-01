from inline_markdown import text_to_textnodes


def markdown_to_blocks(markdown):
    full_doc = markdown
    md_blocks = full_doc.split("\n\n")
    md_blocks = map(lambda item: item.strip(), md_blocks)
    md_blocks = list(filter(lambda item: False if item == "" else True, md_blocks))
    return md_blocks


markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

markdown_to_blocks(markdown)
