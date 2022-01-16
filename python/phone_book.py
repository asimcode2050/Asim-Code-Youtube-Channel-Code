"""
Phone book lookup with a list and  a dictionary in Python
YouTube Channel: Asim Code
https://youtu.be/3Ma1pZEo3J8
Please Subscribe to Asim Code.
"""
def search_number(pbook,name):
    for n, number in pbook:
        if n == name:
            return number
    return None

phone_book = [("Mike Tyson", "555-555-5555"),
              ("Bill Gates", "111-555-5555"),
              ("John Doe","222-555-5555"),]
print(f"Bill Gates's phone number is : {search_number(phone_book,'Bill Gates')}")
 

phone_dict = {"Mike Tyson" : "555-555-5555",
              "Bill Gates" : "111-555-5555",
              "John Doe" : "222-555-5555" ,}
print(f"John Doe's phone number is : {phone_dict['John Doe']}")
