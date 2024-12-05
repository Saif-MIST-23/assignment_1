from duplicate_numb import duplicate_numb

def add_contact(all_contact):

    name = input('your contact name: ')
    email = input('your contact email: ')
    phone = int(input('your contact phone number(no gap &vskip first number if it is 0): '))
    address = input('your contact address: ')
    
    contact = {
        'name':name,
        'email':email,
        'phone':phone,
        'address':address
    }

    duplicate_numb(contact,all_contact)

    