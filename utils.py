def input_processor(input_string:str, cap=False) -> str:
    if cap:
        return input_string.strip().capitalize()
    return input_string.strip()

def capitalize_sentence(sentence:str) -> str:
    return ' '.join([word.capitalize() for word in sentence.split()])
    

def clean_input(text):
    pass

