import re

# retunrs the dictionary
# returns {key: value}


def generatingDictionary():
    dictionary = {}
    with open('list.txt') as f:
        words = f.readlines()
        # n time complexity (n would be the number of words)
        for word in words:
            dictionary[word[:-1]] = word[:-1]
    return dictionary

# returns the filtered suggestions on the basis of entered string and dictionary
# params string
# params dictionary
# returns suggestions


def filterSearchedValues(string, dictionary):
    suggestions = list(
        filter(lambda x: (re.findall((r'{}'.format(string)), x)), dictionary))

    # prints suggested values.
    print("Results: ")
    print('No Result Found' if suggestions == [] else suggestions)


# It formats the entered key
# params key
# returns filtered values
def formatSearchedQuery(key):
    string = ''
    for i in range(len(key)):  # n time complexity (n would be the length of entered string)
        string += key[i] + '+'
    string = string[:-1]
    return filterSearchedValues(string, generatingDictionary())


key = input("Enter something to search :- ")
formatSearchedQuery(key)
