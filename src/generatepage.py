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

    with open(template_path, "r") as file:
        template_content = file.read()

    node = markdown_to_html_node(markdown_content)
    node_html_content = node.to_html()

    title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", node_html_content)

    directory = os.path.dirname(dest_path)

    os.makedirs(directory, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_content)

    

def generate_pages_recursive(from_path, template_path, to_path):
     
     for entry in os.listdir(from_path):
        source_path = os.path.join(from_path, entry)
        dest_path = os.path.join(to_path, entry)

        # If it's a file, process it
        if os.path.isfile(source_path):
            if source_path.endswith(".md"):  # Work only with markdown files
                dest_file_path = dest_path.replace(".md", ".html")
                generate_page(source_path, template_path, dest_file_path)
                print(f"File handled: {source_path} -> {dest_file_path}")

        # If it's a directory, create it in the destination and call recursively
        elif os.path.isdir(source_path):
            os.makedirs(dest_path, exist_ok=True)  # Ensure the directory exists in destination
            print(f"Processing directory: {source_path}")
            generate_pages_recursive(source_path, template_path, dest_path)


    


