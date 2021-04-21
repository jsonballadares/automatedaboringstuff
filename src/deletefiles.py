import os

os.chdir('/Users/jasonballadares/repos/automatedaboringstuff/')

print(os.listdir())

for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print(filename)
