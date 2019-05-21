initial_text = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.[28][29]

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[30]

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[31] and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation.

Python was conceived in the late 1980s[32] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL)[33], capable of exception handling and interfacing with the Amoeba operating system.[7] Its implementation began in December 1989.[34] Van Rossum's long influence on Python is reflected in the title given to him by the Python community: Benevolent Dictator For Life (BDFL) – a post from which he gave himself permanent vacation on July 12, 2018.[35]"""

# task 1
# знайти кількість букв в тексті в розрізі: всього, верхній регістр, нижній регістр; результат записати до dict з ключами total, upper, lower.

import string

common_letters = 0
upper_letters = 0
lower_letters = 0

for i in initial_text:
    if i in string.ascii_letters:
        common_letters += 1
    if i in string.ascii_uppercase:
        upper_letters += 1
    if i in string.ascii_lowercase:
        lower_letters += 1

print(common_letters)
print(upper_letters)
print(lower_letters)

# знайти кількість по кожній букві в тексті; результат записати в list , де кожний елемент - це tuple(letter, count)
import string
import copy

initial_text = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.[28][29]
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[30]
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[31] and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation.
Python was conceived in the late 1980s[32] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL)[33], capable of exception handling and interfacing with the Amoeba operating system.[7] Its implementation began in December 1989.[34] Van Rossum's long influence on Python is reflected in the title given to him by the Python community: Benevolent Dictator For Life (BDFL) – a post from which he gave himself permanent vacation on July 12, 2018.[35]"""

result = dict()
ascii_l = string.ascii_lowercase
ascii_u = string.ascii_uppercase

# task 1. Знайти кількість букв в тексті в розрізі: всього, верхній регістр, нижній регістр; результат записати до dict з ключами total, upper, lower
temp2 = {
    'upper': 0,
    'lower': 0,
    'total': 0
}
for letter in initial_text:
    if letter in string.ascii_uppercase:
        temp2['upper'] += 1
    elif letter in string.ascii_lowercase:
        temp2['lower'] += 1
temp2['total'] = temp2['upper'] + temp2['lower']
result[1] = temp2

# task 2. Знайти кількість по кожній букві в тексті; результат записати в list, де кожний елемент - це tuple(letter, count)
temp2 = []
for i in range(len(ascii_l)):
    temp2.append((ascii_l[i], initial_text.count(ascii_l[i]) + initial_text.count(ascii_u[i])))
result[2] = temp2

# task 3. Сформувати list на основі list з п.2, в якому елементи відсортовані по кількості букв (від найменшої до найбільшої кількості)
temp3 = copy.deepcopy(temp2)
for i in range(len(temp3)):
    key, val = temp3[i]
    temp3[i] = (val, key)
temp3.sort()
for i in range(len(temp3)):
    key, val = temp3[i]
    temp3[i] = (val, key)
result[3] = temp3

# (????) task 4. Знайти загальну кількість слів в тексті, результат записати як int
temp4 = ''
for letter in initial_text:
    if letter not in string.ascii_letters + '0123456789':
        temp4 += ' '
    else:
        temp4 += letter
result[4] = len(temp4.split())

# task 5. Знайти кількість чисел в тексті, результат записати як int
temp5 = ''
for letter in initial_text:
    if letter not in '0123456789':
        temp5 += ' '
    else:
        temp5 += letter
result[5] = len(temp5.split())

# (???) task 6. Створити dict, де ключ - це довжина слова, а значення - це кількість слів з такою довжиною
# 1986s - только слово или только число или слово/число?,  s - слово или ничего?,  [32] -  число/слово или только число?
temp6 = dict()
for word in temp4.split():
    word_length = len(list(word))
    temp6[word_length] = temp6.setdefault(word_length, 0) + 1
result[6] = temp6

# task 7. Знайти відсоток речень, в яких зустрічається слово Python; результат записати як float (на 100 не множимо)
# "...permanent vacation on July 12, 2018.[35]", [35] - не считаю отдельным предложением?
temp7 = initial_text.split('.')
i = 0
for sentence in temp7:
    if 'python' in sentence.lower():
        i += 1
result[7] = i / (len(temp7) - 1)

# task 8. Знайти кількість спеціальних символів в тексті; результат записати до dict, де ключ - це спеціальний символ, а значення - кількість;
temp8 = {}
for symb in initial_text:
    if symb not in string.ascii_letters + '0123456789':
        temp8[symb] = temp8.setdefault(symb, 0) + 1
result[8] = temp8

# task 9. Створити list, в якому речення відсортовані по кількості букв в верхньому регістрі;


for key in result.keys():
    print(key, ':', result[key])
