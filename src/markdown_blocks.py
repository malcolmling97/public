def markdown_to_blocks(markdown):
    markdown_split = markdown.split("\n\n")
    final_list = []
    for i in markdown_split:
        if i.strip():
            final_list.append(i.strip())

    return final_list



    
