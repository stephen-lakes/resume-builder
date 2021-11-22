def clean_input(input_str:str, cap=False):
    if cap:
        return ' '.join([word.capitalize().strip() for word in input_str.split()])
    return ' '.join([word.strip() for word in input_str.split()])

def clean_location_field(input_str:str):
    return ','.join([ch.strip().capitalize() for ch in input_str.split(",")])

