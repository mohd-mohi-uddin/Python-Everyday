>>> LIST COMPREHENSION:

we can use new_list = [new_item for item in my_list] to created a new list and add some functions to the old list.

like for example if u have like numbers = [1,2,3]

u want [2,4,6]
u can write:
new_list = [i*2 for i in numbers]

there is also

>> CONDITIONAL LIST COMPREHENSION:

the syntax for this is: 

new_list = [new_item for item in my_list if test]

here u can give a if conditition

>> split():

we can change sentence intolist of words.

"i love you" 
to
["i","love","you"]


>> DICTIONARY COMPREHENSION:

Dictionary comprehension is the dictionary version of a list comprehension. It lets you create a new dictionary in one line.

Syntax
new_dict = {
    key_expression: value_expression
    for item in iterable
}

or, when looping through another dictionary:

new_dict = {
    new_key: new_value
    for (key, value) in old_dict.items()
}