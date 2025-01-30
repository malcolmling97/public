block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    markdown_split = markdown.split("\n\n")
    final_list = []
    for i in markdown_split:
        if i.strip():
            final_list.append(i.strip())

    return final_list

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph



    

# test_string = "  hello world   \n     \n\n  hello   \nworld  \n  "
# markdown_string = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

# print(markdown_to_blocks(test_string))
# print(markdown_to_blocks(markdown_string))

# markdown_block_1 = "# This is a heading"
# markdown_block_2 = "* This is a heading"
# markdown_block_3 = " This is a heading"

# print(block_to_block_type(markdown_block_1))
# print(block_to_block_type(markdown_block_2))
# print(block_to_block_type(markdown_block_3))



