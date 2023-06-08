<!-- In python, for loop and else loop can be used together -->


<!-- In Python, the else clause in a for loop can be used to execute a block of code when the loop completes normally (i.e., without encountering a break statement). It is not related to the else statement used in conditional statements like if or while.

In the context of a for loop, the else clause is optional and provides a way to define code that should be executed if the loop completes all iterations without encountering a break statement. The code within the else block is executed after the loop finishes iterating over all the items in the sequence.

Here's an example to illustrate the usage of the else clause with a for loop: -->


my_list = [1, 2, 3, 4, 5]

for item in my_list:
    if item == 0:
        break
    print(item)
else:
    print("Loop completed without encountering a break statement.")



# List, set requires declaration
# Dictionary, set has different ways of iteration
Ex.    for base_word, words in occurrences.items(): ==> dictionary

Ex2. for triplet in occurrences: ==> set


triplet[2].extend([word2]) will make triplet[2] a list.

# In Python, the extend() method is used to append multiple elements from an iterable (such as a list) to the end of an existing list.

# If triplet[2] is initially an empty list, then extend([word2]) will add word2 as the first element in the list. 
# If triplet[2] already contains elements, extend([word2]) will append word2 to the existing list.

# For example, if triplet[2] initially contains ['existing_word'] and you execute triplet[2].extend(['new_word']), the resulting value of triplet[2] will be ['existing_word', 'new_word'].

# When adding element to a tuple, '(new_element, )' syntax is required, in order to indicate that it's a single element tuple