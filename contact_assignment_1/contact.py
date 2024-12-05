from add_contact import add_contact
from view_contacts import view_contact
from update_contact import update_contact
from remove_contact import remove_contact
from search_contact import search_contact

all_contact=[]

while True:

    print('''
          0. Exit
          1. Add contact
          2. View contact
          3. Update contact
          4. Reomove contact
          5. Search contact
''')
    
    menu_select = input('select option from menu: ')

    if menu_select=='0':
        print('thanks for choosing our contacts')
        break
    elif menu_select=='1':
        add_contact(all_contact)
    elif menu_select=='2':
        view_contact(all_contact)
    elif menu_select=='3':
        update_contact(all_contact)
    elif menu_select=='4':
        remove_contact(all_contact)
    elif menu_select=='5':
        search_contact(all_contact)
    else: print('invalid option is choosen, try again')
