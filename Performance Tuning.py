from timeit import Timer
import string


def soundex(source):
    code = string.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                            '91239129922455912623919292')
    if not source.isalpha():
        return 'Not a valid name'
    source = source.upper()
    digit = source[0] + source[1:].translate(code)
    # print digit
    codded_name = digit[0]
    for elem in digit[1:]:
        if elem is not '9':
            if elem is not codded_name[-1]:
                codded_name += elem

    codded_name += '000'
    return codded_name[:4]

if __name__ == '__main__':

    names = ('AkhileshSaipangallu', )
    for name in names:
        # print(soundex(name))
        statement = "soundex('%s')" % name
        t = Timer(statement, "from __main__ import soundex")
        print(t.repeat())

