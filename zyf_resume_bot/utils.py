
#def get_context_from_resume(file_path, query):
    #with open(file_path, 'r', encoding='utf-8') as f:
        #resume_text = f.read()
    #return resume_text[:2500]

import os

def get_context_from_resume(file_name, query):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)

    with open(file_path, 'r', encoding='utf-8') as f:
        resume_text = f.read()

    return resume_text[:2500]
