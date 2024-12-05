from save_contact import save_contact
def remove_contact(all_contact):

    if len(all_contact)>=1:

        n=0
        _contact_=input('write your contact to remove: ')

        while n < len(all_contact):

            index_value = all_contact[n]

            if index_value['phone'] == _contact_:
                all_contact.remove(all_contact[n])
                print('contact removed successfully')
                n+=1

            else: n+=1

        save_contact(all_contact)
        return all_contact

    else: print('your contact list is empty')

                     
        