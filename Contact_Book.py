################################################################################
##      Fundamental Operations
################################################################################

##      The dictionary
contact_book = {}

##      Methods to request info

def get_fname():
    fname = input('Enter contact first name: ').strip()
    while not fname:
        fname = input('First name cannot be empty. Please enter a valid first name: ').strip()
    return fname

def get_lname():
    lname = input('Enter contact last name: ').strip()
    while not lname:
        lname = input('Last name cannot be empty. Please enter a valid last name: ').strip()
    return lname

def get_number():
    number = input('Enter contact phone number (digits only): ').strip()
    while not number.isdigit():
        number = input('Invalid phone number. Please enter digits only: ').strip()
    return number

def get_email():
    email = input('Enter contact email: ').strip()
    while '@' not in email or '.' not in email:
        email = input('Invalid email address. Please enter a valid email: ').strip()
    return email

##       Printers

def print_dict(dict):
    for key in dict.keys():
        print(f'{key}: {dict[key]}')

def print_contact_book(dict):
    for key in dict.keys():
        print(f'Entry: {key}')
        print_dict(dict[key])
        print(' ')

##      Create dictionary out of values

def make_dict(fname, lname, number, email):
    return {
        "First name": fname,
        "Last name": lname,
        "Phone number": number,
        "Email address": email
    }

##      Search and return contact book of results

def contact_search(query):
    search_results = {}
    results_qty = 0
    query = query.lower()
    for key, nested_dict in contact_book.items():
        if any(query in value.lower() for value in nested_dict.values()):
            results_qty += 1
            search_results[results_qty] = nested_dict
    if not search_results:
        print('\n...No results found...\n')
        return None
    else:
        print(f'\n< Found {results_qty} result(s) >\n')
        return search_results

def search_and_select_contact():
    query = input('Enter search query: ').strip()
    if not query:
        print('\n...Invalid search query...\n')
        return None

    results = contact_search(query)

    if not results:
        return None

    print_contact_book(results)

    try:
        selection = input('Enter contact number: ').strip()
        if not selection.isdigit():
            raise ValueError
        selected_contact = results.get(int(selection))
        if selected_contact:
            return selected_contact
        else:
            print('\n...Invalid selection...\n')
            return None
    except ValueError:
        print('\n...Invalid input, please enter a number...\n')
        return None

################################################################################
##      1. Create contact
################################################################################

def create_contact():
    print('\n< Create new contact >')

    fname = get_fname()
    lname = get_lname()
    number = get_number()
    email = get_email()

    name = f'{fname} {lname}'
    dict = make_dict(fname, lname, number, email)

    if name not in contact_book:
        contact_book[name] = dict
        print('\n< Contact created successfully! >\n')
        print_dict(dict)
    else:
        print('\n...Contact already exists...\n')
        print('Existing contact:')
        print_dict(contact_book[name])

        print('\nNew contact:')
        print_dict(dict)

        print('\nWould you like to update the existing contact?\n1 = yes\nAny key = no\n')
        choice = input().strip()

        if choice == '1':
            contact_book[name] = dict
            print('\n< Success! Contact updated. >\n')
        else:
            print('\n...Returning to main menu...\n')

################################################################################
##      2. Search contact
################################################################################

def search_contact():
    query = input('\n< Search for a contact >\nEnter search query: ').strip()
    results = contact_search(query)
    if results:
        print_contact_book(results)

################################################################################
##      3. Update contact
################################################################################

def modify_contact(old_key, updated_contact):
    if old_key in contact_book:
        del contact_book[old_key]
    new_key = f"{updated_contact['First name']} {updated_contact['Last name']}"
    contact_book[new_key] = updated_contact

def update_contact():
    print('\n< Search for a contact >\n<   Update a contact   >\n')

    results = search_and_select_contact()
    if not results:
        return

    print('\n< Current contact details: >\n')
    print_dict(results)

    tmp_contact = results.copy()

    options = {
        '1': lambda: tmp_contact.update({'First name': get_fname()}),
        '2': lambda: tmp_contact.update({'Last name': get_lname()}),
        '3': lambda: tmp_contact.update({'Phone number': get_number()}),
        '4': lambda: tmp_contact.update({'Email address': get_email()}),
        '5': lambda: print('...Success!...\n'),
        '6': lambda: print('...Returning to main menu...\n')
    }

    while True:
        print('''
        < 1 > Edit First name
        < 2 > Edit Last name
        < 3 > Edit Phone number
        < 4 > Edit Email address
        < 5 > Commit Editing
        < 6 > Cancel Editing
        ''')

        selection = input().strip()
        if selection in options:
            options[selection]()
            if selection == '5':
                old_key = f"{results['First name']} {results['Last name']}"
                modify_contact(old_key, tmp_contact)
                break
            elif selection == '6':
                break
        else:
            print('\n...Invalid selection...\n')

################################################################################
##      4. View all contacts
################################################################################

def view_all_contacts():
    if contact_book:
        print('\n< Current contact book entries >\n')
        print_contact_book(contact_book)
    else:
        print('\n...No contacts to display...\n')

################################################################################
##      5. Delete contact
################################################################################

def delete_contact():
    print('\n< Search for a contact >\n<   delete a contact   >\n')

    results = search_and_select_contact()
    if isinstance(results, dict):
        name = f"{results['First name']} {results['Last name']}"
        del contact_book[name]
        print('\n< Success! Contact deleted. >\n')
    else:
        print('\n...Invalid selection...\n')

################################################################################
##      Front end
################################################################################

def main_menu():
    options = {
        '1': create_contact,
        '2': search_contact,
        '3': update_contact,
        '4': view_all_contacts,
        '5': delete_contact,
        '6': lambda: print('...Thank you for using the contact book app...\n')
    }

    while True:
        print('''
        Please make a selection from the following:
        < 1 > Create a new contact
        < 2 > Search for a contact
        < 3 > Update an existing contact
        < 4 > View all contacts
        < 5 > Delete a contact
        < 6 > Exit contact app
        ''')
        selection = input().strip()
        if selection in options:
            options[selection]()
            if selection == '6':
                break
        else:
            print('\n...Invalid selection...\n')

################################################################################
##      Initialize front end
################################################################################

print('''
##############################################
##                                          ##
##                < Welcome >               ##
##                                          ##
##                  (>'-')>                 ##
##                                          ##
##          Contact book application        ##
##        Premium contact storage and       ##
##       management at your fingertips      ##
##                                          ##
##############################################''')

main_menu()
