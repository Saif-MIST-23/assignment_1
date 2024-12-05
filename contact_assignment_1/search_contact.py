def search_contact(all_contact):

    if len(all_contact)>=1:

        n=0
        _contact_=input('write the contact number to search and see the details: ')

        while n < len(all_contact):

            index_value = all_contact[n]

            if index_value['phone'] == _contact_:
                print(f"name-{index_value['name']}||email-{index_value['email']}||phone-{index_value['phone']}||address-{index_value['address']}")
                n+=1
            else: n+=1
    else: print('no match with your list')
    