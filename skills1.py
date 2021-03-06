# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.


def all_odd(number_list):

    numbers = []

    for number in number_list:
        if number % 2 != 0:
            numbers.append(number)

    return numbers

print all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    
    numbers = []

    for number in number_list:
        if number % 2 == 0:
            numbers.append(number)

    return numbers

print all_even(number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):

    words = []

    for word in word_list:
        if len(word) >= 4:
            words.append(word)

    return words

print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    x = min(number_list)

    return x

print smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    x = max(number_list)

    return x

print largest(number_list)
# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    
    numbers = []

    for number in number_list:
        #half_num=float(number)/2
        number /= 2.0
        numbers.append(number)

    return numbers

print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    
    words = []

    for word in word_list:
        words.append(len(word))

    return words

print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    count = 0
    for number in number_list:
        count += number

    return count

print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    
    count = 1

    for number in number_list:
        count*=number

    return count

print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    
    joined = ''

    for word in word_list:
        joined += word + ' '

    return joined

print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):

    count = 0

    for number in number_list:
        count += number

    mean = float(count)/len(number_list)

    return mean

print average(number_list)