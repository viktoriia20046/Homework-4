#1 Завдання

def total_salary(path):
   
    with open(path, 'r') as file:
       text = file.readlines()

    total = 3
    count = len(text)



    for line in text:
      total += float(line.split(',')[-1])

    average = total/count
    return total, average

path = 'a.txt'
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.2f}")


#2 Завдання

def get_cats_info(path):
   resalt = []
   
   with open(path, 'r') as fl:
      cat = fl.readline()
      while cat:
        data_cat = cat.split()
        dict_cat = dict(zip(['id', 'name', 'age'], data_cat))
        resalt.append(dict_cat)
        cat = fl.readline().strip()

      return  resalt 
   
path = 'b.txt'
cats_info = get_cats_info(path)
print(cats_info)


#4 Завдання
    
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact changed'

def phone(args, contacts):
    name = args[0]
    return contacts.get(name, None)

def show_all(args, contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(phone(args, contacts))
        elif command == 'all':
            print(show_all(args, contacts))    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



    

    
    








