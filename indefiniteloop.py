def checkout():
    total = 0
    count = 0
    moreItems = True
    while (moreItems):
        price = float(input("Enter price of item (0 when done):"))
        if price > 0:
            count += 1
            total += price
            print(('Subtotal: $ {:.2f}').format(total))
        elif price < 0:
            print('The item price cannot be negative')
        else :
            moreItems = False
    average = total / count
    print(('Total items: {}').format(count))
    print(('Total ${}').format(total))
    print(('Average price per item: ${:.2f}').format(average))

checkout()