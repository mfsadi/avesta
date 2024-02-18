def persian_character_normalizer(input_string):
    translation_mapping = str.maketrans(
        {'آ': 'ا', 'ک': 'ک', 'ي': 'ی', '٥': '5', '\u200c': ' ', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5',
         '۶': '6', '۷': '7', '۸': '8', '۹': '9', '۰': '0'})
    result_string = input_string.translate(translation_mapping)
    return result_string
