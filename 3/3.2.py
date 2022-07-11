import cld3
import translate
from translate import Translator

a = input()


def translation(a):
    print(cld3.get_language(a)[0])

    text = Translator(to_lang='ru')
    translation = text.translate(a)
    print(translation)
    return a

translation(a)