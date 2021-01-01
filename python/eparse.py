from flanker.addresslib import address
print(address.parse('email@hotmail.com'))
print(address.parse('@hotmail.com'))
#parse address list
print(address.parse_list(['email2@hotmail.com','email3@hotmail.com']))
#validate email address
print(address.validate_address('tom@jksjdlksjaaskl.com'))

