import typing as tp

llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
blst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def encryptCaesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind + shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind + shift]
        else:
            ret += x
    return ret

##    ciphertext = ""
##   # PUT YOUR CODE HERE
##    return ciphertext


def decryptCaesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind - shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind - shift]
        else:
            ret += x
    return ret


print(encryptCaesar("Да здравствует салат Цезарь!"))
print(decryptCaesar("Зг кзугефхецих фгогх Щикгуя!"))


##def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
##    """
##    Brute force breaking a Caesar cipher.
##    """
message = 'GIEWIVrGMTLIVrHIQS'  # encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))


##best_shift = 0
# PUT YOUR CODE HERE
##return best_shift
