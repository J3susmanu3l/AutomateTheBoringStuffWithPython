def method_1():
    all_guests = {'Alice': {'apples': 7, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

    def total_brought(guests, item):
        num_brought = 0
        for k, v in guests.items():
            num_brought = num_brought + v.get(item, 0)
        return num_brought

    print('Number of things being brought:')
    print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
    print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
    print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
    print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
    print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))

def method_2():
    # method 2
    all_guests = {'Alice': {'apples': 7, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}
    items_cuantity_pairs = {}

    for key, value in all_guests.items():
        for item, quantity in value.items():
            if item not in items_cuantity_pairs:
                items_cuantity_pairs[item] = quantity
            else:
                items_cuantity_pairs[item] += quantity
    
    for items, quantity in items_cuantity_pairs.items():
        print(' - ' + items + (20- len(items))*" " + str(quantity))




def unique_items_per_guest(guests):
    num_brought = {}
    for guest, item in guests.items():
        if guest not in num_brought:
            num_brought[guest] = item
        else:
            num_brought[guest] += item
    return num_brought

    # print('Number of things being brought:')
    # for key, value in unique_items_per_guest.items():
    #     print(' - ' + key + '         ' + str(value))

    



def main():
    # method_1()
    method_2()

if __name__ == "__main__":
    main()