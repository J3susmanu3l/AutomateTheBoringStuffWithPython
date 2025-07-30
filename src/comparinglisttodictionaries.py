def dict_equality():
    spam = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
    ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
    print(spam == ham)
    print(list(spam.keys()) == list(ham.keys()))
    print(list(spam.values()) == list(ham.values()))
    print(list(spam.items()) == list(ham.items()))



def color_error():
    spam = {'name': 'Zophie', 'age': 7}
    spam['color'] = 'black'
    print(spam)
    spam['color'] = 'white'
    print(spam)





























def main():
    # dict_equality()
    color_error()














































if __name__ == '__main__':
    main()



