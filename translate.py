from translate import Translator

translator = Translator(from_lang="russian", to_lang="english")

text_Rus = input("что перевести ")

text_Eng = translator.translate(text_Rus)

print(text_Eng)
