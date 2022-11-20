#Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

def linear_search_dictionary(dict , target):
    for key,value in dict.items():
        if value == target:
            print(f"Found  at key{key}")
            return key

        print("Target not in dictionary")
        return -1

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
