"""
Translator: create a dictionary file. Using this file you are able to translate words from one language to another.
"""
import sys


def translate(word, lang='en'):
    lang = lang if lang else 'en'
    with open('dictionary.txt', 'r') as data:
        if lang == 'en':
            _dict = {x.split(' ')[0].strip(): x.split(' ')[1].strip() for x in data.read().split('\n') if x != ''}
        elif lang == 'hu':
            _dict = {x.split(' ')[1].strip(): x.split(' ')[0].strip() for x in data.read().split('\n') if x != ''}
        else:
            return 'We only translate en -> hu or hu -> en'

        if (result := _dict.get(word)) is not None:
            return result
        else:
            print('we have detected a new word of the %s language!' % lang)
            print('enter y/yes/add to add it to the dictionary')
            add_new_word = input()
            if add_new_word.lower() not in ['y', 'yes', 'add']:
                print('okay, bye')
                sys.exit(0)
            else:
                print('enter the translation of the word (%s)' % word)
                translation = input()
                with open('dictionary.txt', 'a') as writer:
                    writer.write(word + ' ' + translation)
                print('done, new word added')


if __name__ == '__main__':
    print('Welcome to the Simple Dictionay')
    print('default language is en, type hu to change it')
    _lang = input()
    print('enter a word to translte')
    _word = input()
    print(translate(_word, _lang))
