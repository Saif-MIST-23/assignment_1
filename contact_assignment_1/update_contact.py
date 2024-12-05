from save_contact import save_contact
def update_contact(all_contact):

    if len(all_contact)>=1:

        n=0
        _contact_=int(input('write your previous contact number to update: '))

        while n < len(all_contact):

            index_value = all_contact[n]

            if index_value['phone'] == _contact_:

                while True:
                    print('''
                          update ---
                                1. name
                                2. email
                                3. phone
                                4. address
                                5. exit
                          ''')
                    menu_select=input('choose option to update:')

                    if menu_select=='1':
                        index_value['name']=input('write your updated contact name: ')
                        print(f"updated contact name: {index_value['name']}, added successfully")
                    
                    elif menu_select=='2':
                        index_value['email']=input('write your updated contact email: ')
                        print(f"updated contact email: {index_value['email']}, added successfully")
                    
                    elif menu_select=='3':
                        index_value['phone']=int(input('write your updated contact phone: '))
                        print(f"updated contact phone: {index_value['phone']}, added successfully")
                    
                    elif menu_select=='4':
                        index_value['address']=input('write your updated contact address: ')
                        print(f"updated contact address: {index_value['address']}, added successfully")
                    
                    elif menu_select=='5':
                        print('all update is completed')
                        break
                n+=1
            else: n+=1
        else: print('no contact is in your list')

        save_contact(all_contact)

        return all_contact




                                      
