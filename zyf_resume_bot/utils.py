
def get_context_from_resume(file_path, query):
    with open(file_path, 'r', encoding='utf-8') as f:
        resume_text = f.read()
    return resume_text[:2500]
