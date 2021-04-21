import re

message = 'Call me 786-720-1111, or at 786-777-6565'

phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

match_object = phone_number_regex.search(message)

print(match_object.group(1))


batRegex = re.compile(r'Bat(man|copter|mobile|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
