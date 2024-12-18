from googletrans import Translator

def text_translation(text : str, lan : str):
    t_translator = Translator()
    result = t_translator.translate(text=text, dest=lan)
    
    return result.text