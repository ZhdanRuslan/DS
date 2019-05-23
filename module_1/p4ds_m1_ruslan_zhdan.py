import string
import copy

initial_text = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.[28][29]

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[30]

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[31] and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation.

Python was conceived in the late 1980s[32] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL)[33], capable of exception handling and interfacing with the Amoeba operating system.[7] Its implementation began in December 1989.[34] Van Rossum's long influence on Python is reflected in the title given to him by the Python community: Benevolent Dictator For Life (BDFL) – a post from which he gave himself permanent vacation on July 12, 2018.[35]"""

result = dict()
ascii_lower = string.ascii_lowercase
ascii_upper = string.ascii_uppercase
ascii_letters = string.ascii_letters

# task 1. Знайти кількість букв в тексті в розрізі: всього, верхній регістр, нижній регістр; результат записати до dict з ключами total, upper, lower
temp2 = {
    'upper': 0,
    'lower': 0,
    'total': 0
}
for letter in initial_text:
    if letter in ascii_upper:
        temp2['upper'] += 1
    elif letter in ascii_lower:
        temp2['lower'] += 1
temp2['total'] = temp2['upper'] + temp2['lower']
result[1] = temp2


# task 2. Знайти кількість по кожній букві в тексті; результат записати в list, де кожний елемент - це tuple(letter, count)
temp2 = []
for upper_number in range(len(ascii_lower)):
    temp2.append((ascii_lower[upper_number], initial_text.count(ascii_lower[upper_number]
                                                                ) + initial_text.count(ascii_upper[upper_number])))
result[2] = temp2


# init dict keys
tmp2 = dict()
for key in ascii_lower:
    tmp2[key] = 0
for val in initial_text.lower():
    if val in tmp2:
        tmp2[val] += 1
print(tmp2)
r_list = []

for i in tmp2.items():
    r_list.append(i)
    # print('\'' + str(i) + '\''+ str(tmp2[i]))
    # r_list.append(str(i) + str(tmp2[i]))
print(r_list)

# task 3. Сформувати list на основі list з п.2, в якому елементи відсортовані по кількості букв (від найменшої до найбільшої кількості)
temp3 = copy.deepcopy(temp2)
for upper_number in range(len(temp3)):
    key, val = temp3[upper_number]
    temp3[upper_number] = (val, key)
temp3.sort()
for upper_number in range(len(temp3)):
    key, val = temp3[upper_number]
    temp3[upper_number] = (val, key)
result[3] = temp3


# (????) task 4. Знайти загальну кількість слів в тексті, результат записати як int
temp4 = ''
for letter in initial_text:
    if letter not in ascii_letters + string.digits:
        temp4 += ' '
    else:
        temp4 += letter
result[4] = len(temp4.split())


# task 5. Знайти кількість чисел в тексті, результат записати як int
temp5 = ''
for letter in initial_text:
    if not letter.isdigit():
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
temp7.pop()
upper_number = 0
for sentence in temp7:
    if 'python' in sentence.lower():
        upper_number += 1
result[7] = upper_number / len(temp7)


# task 8. Знайти кількість спеціальних символів в тексті; результат записати до dict, де ключ - це спеціальний символ, а значення - кількість;
temp8 = {}
for symb in initial_text:
    if symb not in ascii_letters + '0123456789':
        temp8[symb] = temp8.setdefault(symb, 0) + 1
result[8] = temp8


# task 9. Створити list, в якому речення відсортовані по кількості букв в верхньому регістрі;
temp9 = list()
# make list of tuple (upper_number, sentence)
for sentence in temp7:
    upper_number = 0
    for letter in sentence:
        if letter in ascii_upper:
            upper_number += 1
    temp9.append((upper_number, sentence))
temp9.sort()
# make list оf sentence
res = list()
for _, sentence in temp9:
    res.append(sentence)
result[9] = res


# task 10. Знайти букву, яка зустрічається найчастіше і найрідше; результат записати як tuple(max, min);
# make dict, where key - letter, value - number
temp10 = dict()
for letter in initial_text.lower():
    if letter in ascii_letters:
        temp10[letter] = temp10.setdefault(letter, 0) + 1
min_number, max_number = min(temp10.values()), max(temp10.values())
min_letter, max_letter = '', ''
for key, val in temp10.items():
    if val == min_number:
        min_letter = key
    if val == max_number:
        max_letter = key
result[10] = (max_letter, min_letter)


# task 11. Знайти всі числа та записати їх до list, відсортувавши від найбільного до найменшого;
temp11 = temp5.split()
for i, elem in enumerate(temp11):
    temp11[i] = int(elem)
temp11.sort()
result[11] = temp11


# task 12. Знайти мінімальне і максимальне число; результат записати як tuple(min, max);
result[12] = (min(temp11), max(temp11))


# task 13. Знайти абзац, в якому Python зустрічається найчастіше; результат записати як str.
temp13 = initial_text.lower().split('\n')
max_python_str = ''
for sentence in temp13:
    num = sentence.count('python')
    if num > len(max_python_str):
        max_python_str = sentence
result[13] = max_python_str


# task 14. Cтворити dict, де ключ - це слово, а значення - кількість разів, з якою слово зустрічається в тексті;



# task 15. Знайти слово, яке зустрічається найчастіше і найрідше; результат записати як tuple(tuple(word, count), tuple(word, count)).

for key in result.keys():
    print(key, ':', result[key])



