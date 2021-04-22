def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be of length 1')

    if (width < 2) or (height < 2):
        raise Exception(
            '"width" and "height" must be greater than or equal to two')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


box_print('*', 15, 5)
box_print('O', 5, 16)
box_print('OW', 5, 16)
