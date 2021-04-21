import shelve
import os

print(os.getcwd())
shlef_file = shelve.open('mydata')
shlef_file['cats'] = ['zophie', 'pooka', 'simon', 'cleo']
shlef_file.close()

shlef_file = shelve.open('mydata')
print(shlef_file['cats'])
