import cld3
import translate
from translate import Translator

a = input()


def translation(a):
    text = Translator(to_lang='ru')
    translation = text.translate(a)
    print(translation)
    return a

translation(a)