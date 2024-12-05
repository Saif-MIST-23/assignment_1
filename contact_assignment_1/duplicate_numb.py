from save_contact import save_contact

def duplicate_numb(contact,all_contact):

    unic=[]
    n=0

    while n<len(all_contact):
        if contact['phone']!=all_contact[n]['phone']:
            unic.append(all_contact[n])
            n+=1
        else: n+=1

    if len(unic)==len(all_contact):
        all_contact.append(contact)
        save_contact(all_contact)
        print('contact added successfully')
    else: print('this contact already exists')


