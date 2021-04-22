import traceback

try:
    raise Exception('this is an error message')
except:
    errorFile = open('data/error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')
