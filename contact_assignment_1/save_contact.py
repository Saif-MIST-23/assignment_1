def save_contact(all_contact):
    with open ("all_contact.csv","w") as ac:
        for i in all_contact:
            line=f"{i['name']},{i['email']},{i['phone']},{i['address']}\n"
            ac.write(line)
            