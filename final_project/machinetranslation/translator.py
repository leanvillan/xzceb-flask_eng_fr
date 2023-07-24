from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """Translates English text to French using MyMemoryTranslator.
    Args: english_text (str): The English text to be translated.
    Returns: str: The translated French text."""
    translator = MyMemoryTranslator(source='en-GB', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text

def frenchToEnglish(french_text):
    """Translates French text to English using MyMemoryTranslator.
    Args: french_text (str): The French text to be translated.
    Returns: str: The translated English text."""
    translator = MyMemoryTranslator(source='fr-FR', target='en-GB')
    english_text = translator.translate(french_text)
    return english_text
