import os
import re

# Function to process and modify the content of a Markdown file
def modify_markdown_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    original_content = content  # Keep a copy of the original content for comparison

    # Replace client initialization to just client()
    # This regex handles multiline cases where the content inside parentheses is spread over multiple lines
    content = re.sub(r'client\s*=\s*OpenAI\s*\((.|\s)*?\)', 'client = OpenAI()', content)

    # Remove the 'import secret' and 'import os' lines
    content = re.sub(r'^\s*import secret\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*import os\s*$', '', content, flags=re.MULTILINE)

    # Replace model="gpt-3.5-turbo" or "GPT-3.5-turbo" with model="gpt-4o-mini"
    content = re.sub(r'model\s*=\s*"[Gg][Pp][Tt]-3\.5-turbo"', 'model="gpt-4o-mini"', content)

    # Replace any occurrence of 'gpt-3.5' or 'GPT-3.5' with 'gpt-4o-mini' even outside of the model context
    content = re.sub(r'[Gg][Pp][Tt]-3\.5', 'gpt-4o-mini', content)

    # Save the modified content back to the markdown file only if changes were made
    if content != original_content:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Modified: {file_path}")
    else:
        print(f"No changes needed: {file_path}")

# Function to process all markdown files in the ".guides/content" folder
def process_markdown_files():
    folder_path = ".guides/content/A-Simple-Chatbot-using-NLTK-545d"
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    
    for md_file in md_files:
        file_path = os.path.join(folder_path, md_file)
        print(f"Processing: {file_path}")
        modify_markdown_file(file_path)
    
    print("Finished modifying markdown files")

# Example usage
process_markdown_files()
