# Example
contacts = {'Jason': '555-5555', 'Carl': '555-4444'}

jason_phone = contacts['Jason']
carl_phone = contacts['Carl']

print ('Dial {} to call Jason.'.format(jason_phone))
print ('Dial {} to call Carl.'.format(carl_phone))

# Modify dict
contacts['Jason'] = '555-0000'
print ('Updated number. Dial {} to call Jason.'.format(jason_phone))

# Adding to dict
contacts['Tony'] = '555-7777'
print(contacts)
print(len(contacts))

# Deleting from dict
del contacts['Tony']
print(contacts)

#-----
#list inside dict:
contact_dict_list = {
    'Jason': ['555-5555', '555-6666'],
    'Tyler': '555-1234'
}

for number in contact_dict_list['Jason']:
    print('Phone number: {}'.format(number))

#check if key and/or value exists
if 'Jason' in contacts.keys():
    print("Jason's phone number(s) on file is:")
    print(contact_dict_list['Jason'])

if 'Troy' in contacts.keys():
    print("Jason's phone number is:")
    print(contact_dict_list['Troy'][0])

for contact in contacts:
    print('The number for {0} is {1}.'.format(contact, contacts[contact]))

# Loop through each value
for contact in contacts.values():
    print('The values are {}'.format(contact))

