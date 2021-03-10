## CSV to JSON Converter


Will start with the most atmoic function. The `create_dict(keys, field_value)` function recieves two arguments. The first one `key` is a list, each item of this list will be the dictionary key inside the previous key, the value is what will be placed as the last key value. For example if I want one level dictionary:

``
create_dict(['OneLevel'], 'A')
``

will return
``
{'OneLevel': 'A'}
``

and 

``
create_dict(['OneLevel', 'TwoLevels'], 'A')
``

will return 

``
{'OneLevel': {'TwoLevels': 'A'}}
``

The next level is the `update_dict(d_, keys, field_value)` function that takes in a dictionary, list of keys and value, all three arguments are mandatory. The function will update the dictionary that was given according to the keys.
If for example I have the following dictionary `my_dict = {'LevelOne':{'LevelTwo':'A'}}` and I want to add the `{'LevelTwoOne':'B'}` inside `LevelOne` key I can use the function as follows:

``
update_dict(my_dict, ['LevelOne','LevelTwoOne'], 'B')
``

my new updated dictionary will be `{'LevelOne':{'LevelTwo':'A','LevelTwoOne':'B'}}`

next there is the `write_line(headers, values)` function. It takes in two lists. Headers and values. In order to create a nested dict use comma between each key, ie. `LevelOne.LevelTwo` will be come a two nested dictionaries, `LevelTwo` inside `LevelOne`. Can also use squrare brackets `[i]` for creating a list where `i` is the index. Values can be anything (lists, dict, string). Length of headers and values must be the same. 

Example:

``
write_line(['LevelOne[0].LevelThree','SecondKey.SecondKeyTwo', 'LevelOne[1].LevelTwo'], ['A','B','C'])
``

will return the following:

``
{'LevelOne': [{'LevelThree': 'A'}, {'LevelTwo': 'C'}],
 'SecondKey': {'SecondKeyTwo': 'B'}}
``
