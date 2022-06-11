import en_core_web_sm

# Load pre-trained english language model
nlp = en_core_web_sm.load()

# setting file extension
extension = 'pdf'

def create_tokenized_texts_list(extension):
    #Creating lists of names and tokenized information extracted
    resume_texts, resume_names = [], []
    # Loop over the resumes directory content
    for resume in list(filter(lambda x: extension in x, os.listdir(PROJECT_DIR + '/CV'))):
        if extension == 'pdf':
            resume_texts.append(nlp(extract_text_from_pdf(PROJECT_DIR + '/CV/' + resume)))
        elif 'doc' in extension:
            resume_texts.append(nlp(extract_text_from_word(PROJECT_DIR + '/CV/' + resume)))
        resume_names.append(resume.split('_')[0].capitalize())
    return resume_texts, resume_names