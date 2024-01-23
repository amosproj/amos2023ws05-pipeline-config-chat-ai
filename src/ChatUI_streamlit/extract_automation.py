#%%
import os
import re


#%%
def extract_triple_quoted_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return re.findall(r'\"\"\"(.*?)\"\"\"', content, re.DOTALL)
#%%
def search_directory(directory, output_file):
    extracted_texts = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                extracted_text = extract_triple_quoted_text(file_path)
                for text in extracted_text:
                    extracted_texts += text

    with open(output_file, 'w') as file:
        file.write(extracted_texts)
#%% 
search_directory('/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/RAG/pipelines', 'extracted_data.py')
# %%
