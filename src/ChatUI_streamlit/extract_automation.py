#%%
import os
import re 


#%%
def extract_and_save_docstrings(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                docstrings = re.findall(r'""".*?"""', content, re.DOTALL)
                extracted_text = '\n'.join(docstrings)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(extracted_text)
#%%
extract_and_save_docstrings('/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/RAG/pipelines')
# %%
