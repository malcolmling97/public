import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    list_of_lines = markdown.split("\n")
    for line in list_of_lines:
        if line.startswith("# "):
            new_line = line.replace("#","").strip()
            return (new_line)
    
    raise Exception("no h1 header found")

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown_content = file.read()
    # print(markdown_content)

    with open(template_path, "r") as file:
        template_content = file.read()
    # print(html_content)

    node = markdown_to_html_node(markdown_content)
    node_html_content = node.to_html()

    # print(node_html_content)
    # print("extractign title")
    title = extract_title(markdown_content)
    # print(title)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", node_html_content)

    # print(template_content)

    directory = os.path.dirname(dest_path)

    os.makedirs(directory, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_content)

    


    







# test_generate_page = generate_page("./content/index.md", "./template.html","./public/index.html")





