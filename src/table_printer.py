TABLEDATA = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


"""
this is the expected output of any column. It needs to be rjustified.
  apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

"""

def printTable(list_var):
    lenth_list = []
    for list_row in list_var:
        for i in range(len(list_row)):
            if len(list_row[i]) > 0:
                lenth_list.append(len(list_row[i]))
    lenth_list.sort()
    num_to_justify = lenth_list[-1]
    print(lenth_list)


    for list_row in list_var:
        for i in range(len(list_row)):
            list_row[i] = list_row[i].rjust(num_to_justify)
        list_row = " ".join(list_row)
        print(list_row)
def main():
    printTable(TABLEDATA)








if __name__ == '__main__':
    main()