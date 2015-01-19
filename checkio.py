# coding=utf-8
import datetime


def median(_list):
    """
    >>> median([1, 2, 3, 4, 5])
    3
    >>> median([3, 1, 2, 5, 3])
    3
    >>> median([1, 300, 2, 200, 1])
    2
    >>> median([3, 6, 20, 99, 10, 15])
    12.5
    """
    _list = sorted(_list)
    l_list = len(_list)
    if l_list % 2:
        return _list[l_list / 2]

    return (_list[l_list / 2 - 1] + _list[l_list / 2]) / 2.0


def house_password(password):
    """
    >>> house_password('A1213pokl')
    False
    >>> house_password('bAse730onE')
    True
    >>> house_password('asasasasasasasaas')
    False
    >>> house_password('QWERTYqwerty')
    False
    >>> house_password('123456123456')
    False
    >>> house_password('QwErTy911poqqqq')
    True
    """
    if len(password) < 10:
        return False
    has_digit = False
    has_lower = False
    has_upper = False
    for letter in password:
        if letter.isdigit():
            has_digit = True
        elif letter.islower():
            has_lower = True
        elif letter.isupper():
            has_upper = True

    if has_digit and has_lower and has_upper:
        return True

    return False


def count_neighbours(matrix, y, x):
    """
    >>> count_neighbours(((1, 0, 0, 1, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0), (0, 0, 1, 0, 0)), 1, 2)
    3
    >>> count_neighbours(((1, 0, 0, 1, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0), (0, 0, 1, 0, 0)), 0, 0)
    1
    >>> count_neighbours(((1, 0, 1, 0, 1), (0, 1, 0, 1, 0), (1, 0, 1, 0, 1), (0, 1, 0, 1, 0), (1, 0, 1, 0, 1), (0,1,0,1,0)), 5, 4)
    2
    """
    l_x = len(matrix[0])
    l_y = len(matrix)
    n = 0
    if x > 0 and y > 0:
        n += matrix[y - 1][x - 1]
    if y > 0:
        n += matrix[y - 1][x]
    if x + 1 < l_x and y > 0:
        n += matrix[y - 1][x + 1]
    if x + 1 < l_x:
        n += matrix[y][x + 1]
    if x + 1 < l_x and y + 1 < l_y:
        n += matrix[y + 1][x + 1]
    if y + 1 < l_y:
        n += matrix[y + 1][x]
    if x > 0 and y + 1 < l_y:
        n += matrix[y + 1][x - 1]
    if x > 0:
        n += matrix[y][x - 1]
    return n


def most_popular(string):
    """
    >>> most_popular("Hello World!")
    'l'
    >>> most_popular("How do you do?")
    'o'
    >>> most_popular("One")
    'e'
    >>> most_popular("Oops!")
    'o'
    >>> most_popular("AAaooo!!!!")
    'a'
    >>> most_popular("abe")
    'a'
    >>> most_popular("Lorem ipsum dolor sit amet")
    'm'
    >>> most_popular("fsbd")
    'b'
    """
    string = string.lower()
    dictionary = {}
    for letter in string:
        if letter.isalpha():
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary.update({letter: 1})

    a = max(sorted(dictionary.items(), key=lambda y: y[0]), key=lambda x: x[1])
    return a[0]


def fizz_buzz(number):
    """
    >>> fizz_buzz(15)
    'Fizz Buzz'
    >>> fizz_buzz(6)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(7)
    '7'

    :param number:
    :return:
    """
    divisible_by_5 = False if number % 5 else True
    divisible_by_3 = False if number % 3 else True
    if divisible_by_3 and divisible_by_5:
        return 'Fizz Buzz'
    elif divisible_by_3:
        return 'Fizz'
    elif divisible_by_5:
        return 'Buzz'
    else:
        return '{0}'.format(number)


def index_power(array, index):
    """
    >>> index_power([1, 2, 3, 4], 2)
    9
    >>> index_power([1, 3, 10, 100], 3)
    1000000
    >>> index_power([0, 1], 0)
    1
    >>> index_power([1, 2], 3)
    -1

    :param data:
    :param index:
    :return:
    """
    if index >= len(array):
        return -1
    return array[index] ** index


def event_the_last(array):
    """
    >>> event_the_last([0, 1, 2, 3, 4, 5])
    30
    >>> event_the_last([1, 3, 5])
    30
    >>> event_the_last([6])
    36
    >>> event_the_last([])
    0

    :param array:
    :return:
    """
    if len(array) == 0:
        return 0
    # sum(array[0::2]) * array[-1]
    total = sum([x for i, x in enumerate(array) if not (i % 2)])
    return total * array[len(array) - 1]


def count_words(text, words):
    """
    >>> count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
    3
    >>> count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
    2
    >>> count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", {"sum", "hamlet", "infinity", "anything"})
    1
    """
    text = text.lower()
    # sum(w in text.lower() for w in words)
    return len([w for w in words if w.lower() in text])


def find_message(message):
    """
    >>> find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
    'HELLO'
    >>> find_message("hello world!")
    ''

    :param message:
    :return:
    """
    return ''.join(x for x in message if x.isupper())


def three_words(text):
    """
    >>> three_words("Hello World hello")
    True
    >>> three_words("He is 123 man")
    False
    >>> three_words("1 2 3 4")
    False
    >>> three_words("bla bla bla bla")
    True
    >>> three_words("Hi")
    False

    :param text:
    :return:
    """
    count = 0
    for word in text.split():
        if word[0].isalpha():
            count += 1
            if count == 3:
                break
        else:
            count = 0

    if count > 2:
        return True

    return False


def most_numbers(*args):
    """
    >>> most_numbers(1, 2, 3)
    2
    >>> most_numbers(5, -5)
    10
    >>> most_numbers(10.2, -2.2, 0, 1.1, 0.5)
    12.4
    >>> most_numbers()
    0

    :param args:
    :return:
    """
    if not len(args):
        return 0

    return max(args) - min(args)


def xo(field):
    """
    >>> xo(["X.O", "XX.", "XOO"])
    'X'
    >>> xo(["OO.", "XOX", "XOX"])
    'O'
    >>> xo(["OOX", "XXO", "OXX"])
    'D'
    >>> xo(["O.X", "XX.", "XOO"])
    'X'

    :param array: 
    :return:
    """
    empty = '.'
    for row in field:
        if row[0] == row[1] == row[2] and row[0] != empty:
            return row[0]

    for row in zip(*field):
        if row[0] == row[1] == row[2] and row[0] != empty:
            return row[0]

    d1 = field[0][0] == field[1][1] == field[2][2]
    d2 = field[2][0] == field[1][1] == field[0][2]
    if (d2 or d1) and field[0][0] != empty:
        return field[1][1]

    return 'D'


def number_in_word(number):
    """
    >>> number_in_word(10)
    'ten'
    >>> number_in_word(4)
    'four'
    >>> number_in_word(143)
    'one hundred forty three'
    >>> number_in_word(12)
    'twelve'
    >>> number_in_word(101)
    'one hundred one'
    >>> number_in_word(212)
    'two hundred twelve'
    >>> number_in_word(40)
    'forty'

    :param number:
    :return:
    """
    number = str(number)
    FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight",
                 "nine"]
    SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen", "nineteen"]
    OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                  "eighty", "ninety"]
    HUNDRED = "hundred"

    result = []
    if len(number) == 3:
        result.append('{0} {1}'.format(FIRST_TEN[int(number[0]) - 1], HUNDRED))
        number = number[1:]

    if len(number) == 2:
        if number[0] != '0':
            if int(number) < 20:
                result.append(SECOND_TEN[int(number[1])])
                number = number[1:]
            else:
                result.append(OTHER_TENS[int(number[0]) - 2])
        number = number[1:]

    if len(number) == 1 and number != '0':
        result.append(FIRST_TEN[int(number) - 1])
    return ' '.join(result)


def boolean(x, y, operation):
    """
    >>> boolean(1, 0, "conjunction")
    0
    >>> boolean(0, 1, "exclusive")
    1
    >>> boolean(0, 0, "equivalence")
    1

    :param x:
    :param y:
    :param operation:
    :return:
    """
    """
    if operation == "conjunction":
        return x & y
    if operation == "disjunction":
        return x | y
    if operation == "implication":
        return (1 ^ x) | y
    if operation == "exclusive":
        return x ^ y
    if operation == "equivalence":
        return x ^ y ^ 1
    """
    if operation == 'conjunction' and (x != 1 or y != 1):
        return 0
    elif operation == 'exclusive' and ((x == 1 and y == 1) or (x == 0 and y == 0)):
        return 0
    elif operation == 'equivalence' and ((x != 1 or y != 1) and (x != 0 or y != 0)):
        return 0
    elif operation == 'implication' and (x == 1 and y == 0):
        return 0
    elif operation == 'disjunction' and (x == 0 and y == 0):
        return 0
    return 1


def left_join(strings):
    """
    >>> left_join(("left", "right", "left", "stop"))
    'left,left,left,stop'
    >>> left_join(("bright aright", "ok"))
    'bleft aleft,ok'
    >>> left_join(("brightness wright",))
    'bleftness wleft'
    >>> left_join(("enough", "jokes"))
    'enough,jokes'

    :param strings:
    :return:
    """
    return ','.join(strings).replace('right', 'left')


def digits_multiplication(number):
    """
    >>> digits_multiplication(123405)
    120
    >>> digits_multiplication(999)
    729
    >>> digits_multiplication(1000)
    1
    >>> digits_multiplication(1111)
    1

    :param number:
    :return:
    """
    number = str(number).replace('0', '1')
    multiplication = 1
    for x in number:
        multiplication *= int(x)
    return multiplication


def count_inversion(sequence):
    """
    >>> count_inversion((1, 2, 5, 3, 4, 7, 6))
    3
    >>> count_inversion((0, 1, 2, 3))
    0

    :param sequence:
    :return:
    """
    n = 0
    sequence = list(sequence)
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                n += 1
                sequence[j], sequence[i] = sequence[i], sequence[j]
    return n


def end_of_other(words):
    """
    >>> end_of_other({"hello", "lo", "he"})
    True
    >>> end_of_other({"hello", "la", "hellow", "cow"})
    False
    >>> end_of_other({"walk", "duckwalk"})
    True
    >>> end_of_other({"one"})
    False
    >>> end_of_other({"helicopter", "li", "he"})
    False

    :param words:
    :return:
    """
    for word_one in words:
        for word_two in words:
            if word_one != word_two and word_one.endswith(word_two):
                return True
    return False


def days_diff(date_one, date_two):
    """
    >>> days_diff((1982, 4, 19), (1982, 4, 22))
    3
    >>> days_diff((2014, 1, 1), (2014, 8, 27))
    238
    >>> days_diff((2014, 8, 27), (2014, 1, 1))
    238

    :param date_one:
    :param date_two:
    :return:
    """
    # abs((datetime.date(*date_one) - datetime.date(*date_two)).days)
    days = (datetime.date(*date_one) - datetime.date(*date_two)).days
    if days < 0:
        days *= -1
    return days


def binary_count(number):
    """
    >>> binary_count(4)
    1
    >>> binary_count(15)
    4
    >>> binary_count(1)
    1
    >>> binary_count(1022)
    9

    :param number:
    :return:
    """
    return str(bin(number)).count('1')


def to_int(string, system):
    """
    >>> to_int("AF", 16)
    175
    >>> to_int("101", 2)
    5
    >>> to_int("101", 5)
    26
    >>> to_int("Z", 36)
    35
    >>> to_int("AB", 10)
    -1

    :param string:
    :param system:
    :return:
    """
    try:
        return int(string, system)
    except ValueError:
        return -1


def common_words(words_one, words_two):
    """
    >>> common_words("hello,world", "hello,earth")
    'hello'
    >>> common_words("one,two,three", "four,five,six")
    ''
    >>> common_words("one,two,three", "four,five,one,two,six,three")
    'one,three,two'

    :param words_one:
    :param words_two:
    :return:
    """
    words = set(words_one.split(',')).intersection(set(words_two.split(',')))
    return ','.join(sorted(words))


def abs_sort(array):
    """
    >>> abs_sort((-20, -5, 10, 15))
    [-5, 10, 15, -20]
    >>> abs_sort((1, 2, 3, 0))
    [0, 1, 2, 3]
    >>> abs_sort((-1, -2, -3, 0))
    [0, -1, -2, -3]

    :param array:
    :return:
    """
    return sorted(array, key=lambda x: abs(x))