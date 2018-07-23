from googletrans import Translator

class Translate:

    @staticmethod
    def translate(text):
        translator = Translator()
        english = translator.translate(text,dest="en" , src='bg')
        return english