import logging
logging.basicConfig(filename='data/log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        logging.debug('i is (%s), total is (%s)' % (i, total))
        total *= i
    logging.debug('Return value is %s' % (total))
    return total


factorial(5)
factorial(7)


logging.debug('End of program')
