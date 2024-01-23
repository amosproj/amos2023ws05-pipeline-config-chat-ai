import os
import fnmatch
import re

def extract_example_code(file_path):
    # Read the content of the Python file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define a regular expression pattern to match code blocks
    pattern = r'```python(.*?)```'

    # Use re.findall to find all code blocks in the content
    code_blocks = re.findall(pattern, content, re.DOTALL)

    return code_blocks

def save_example_code(input_directory, output_directory):
    for root, _, files in os.walk(input_directory):
        # Check if the folder name contains "spark"
        if "spark" in root.lower():
            for filename in files:
                if fnmatch.fnmatch(filename, '*.py'):
                    input_file_path = os.path.join(root, filename)

                    # Determine the relative path of the input file
                    relative_path = os.path.relpath(input_file_path, input_directory)

                    # Create the corresponding output directory structure
                    output_dir = os.path.join(output_directory, relative_path)
                    os.makedirs(output_dir, exist_ok=True)

                    print(f"Processing Python file: {input_file_path}")
                    code_blocks = extract_example_code(input_file_path)

                    for idx, code_block in enumerate(code_blocks, start=1):
                        example_filename = f"example_{idx}.py"
                        example_filepath = os.path.join(output_dir, example_filename)

                        # Save the example code as a separate .py file
                        with open(example_filepath, 'w', encoding='utf-8') as example_file:
                            example_file.write(code_block)

if __name__ == "__main__":
    # Specify the input and output directories
    input_root_directory = "/Users/obi/Desktop/AMOS_New/amos2023ws05-pipeline-config-chat-ai/src/RAG/pipelines"
    output_root_directory = "/Users/obi/Desktop/AMOS_New/amos2023ws05-pipeline-config-chat-ai/src/LeanRAG"

    # Call the function to save extracted example code with the same directory structure
    save_example_code(input_root_directory, output_root_directory)
