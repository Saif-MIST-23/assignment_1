def view_contact(all_contact):

    if all_contact != []:
        for i in all_contact:
            print(f"\nname-{i['name']} || email-{i['email']} || phone-{i['phone']} || address-{i['address']}")
    else: print('your contact list is empty, add some first')
    
