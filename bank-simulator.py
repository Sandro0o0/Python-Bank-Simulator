# TODO: შექმენი ცვლადი სადაც იქნება მომხმარებერლთა ინფორმაცია (dict)
#  name, lastname, age, id(ინდივიდუალური),role,balance,transactions,password

# < ============================================================ >

# TODO: VALIDATIONS:
# --- PASSWORD! უნდა ინახებოდეს ფაილში დაშიფრულად
# --- AGE RESTRICTION! - შეზღუდილი უნდა იყოს არასრულწნობნების რეგისტრაცია
# --- ID! - უნდა იყოს ყველა მომხმარებლისთვის ინდივიდუალური
# --- Role! - უნდა იყოს ერთი მთავარი ადმინი და სხვა ადმინების დამატება შესაძლებელი იქნება მხოლოდ დეველოპერის მიერ
# არ უნდა იყოს შესაძლებელი ბალანსზე არსებულ თანხაზე მეტის გამოტანა 


# < ============================================================ >

# TODO: შექმენი ფუნქცია რომელიც დაარეგისტრირებს users სისტემაში
# TODO: ფუნქცია რომელსაც გადაეცემა პარამეტრად დაშიფრული დიქტი(მომხმარებლის მონაცემები) 
# აბრუნებს მომხმარებლისთვის გასაგებ ინფორმაციას გასაშიფრი დაფა (Ascii)
#

import random as rd
import json

Users = []
current_user = None
ALL_ID = []
 


with open('./users.json', 'r') as file:
    Users = json.load(file) 



for user in Users:
    for key, val in user.items():
        if(key == 'id'):
        # print(val)
            converted_value = []
            for code in val.split('-'):
                converted_value.append(chr(int(code)))
            ALL_ID.append(''.join(converted_value))

print(ALL_ID)




def main_menu():
    print(
        f"""
    მოგესალმებით {current_user['name']}
    თქვენი ბალანსი: {current_user['balance']}
"""
    )
    pass



def main():
    # if(current_user  == None):
        # main_menu()
        # return
    print('____________________________________')
    print("""                 
|    რეგისტრაცია: register    |
|    შესვლა: login            |
    """)                        
    print('____________________________________')
    cmd_input = input('შეიყვანე ბრძანება:')
    if cmd_input == 'register':
        user_register()
    if cmd_input == 'login':
        user_login()

# ===================================გაანონიმურობა====================================

def anonymous_convert(user):
    keys = user.keys()
    val = []
    print(keys)
    for key,values in user.items():
        converted_value = []
        for letter in str(values) :
            converted_value.append(str(ord(letter)))
        val.append('-'.join(converted_value))
    result = zip(keys, val)
    return dict(result)

# ================================================================ >>>

def anonymous_reconvert(user):
    keys = user.keys()
    val = []
    for key, values in user.items():
        converted_value = []
        for code in values.split('-'):
            converted_value.append(chr(int(code)))
        val.append(''.join(converted_value))
    result = zip(keys, val)
    return dict(result)   


# ===================================გაანონიმურობა====================================

# ყველაფრის ფაილში LOG-ებად შენახვა ========

def save():
    with open('users.json', 'w') as log:
        json.dump(Users, log, indent=4)


# ყველაფრის ფაილში LOG-ებად შენახვა ========

#====================================ID გენერირება====================================
def generate_id():
    result = "".join([str(rd.randint(1,9)) for _ in range(9)])
    return result
#====================================ID გენერირება====================================

def email_exists(email):
    for user in Users:
        if anonymous_reconvert(user)['email'] == email:
            return True
    return False


def user_register ():
    user_name = input('Enter Your UserName:')
    user_email = input('Enter Your email:')
    
    # თუ ემაილი არსებობს 
    while email_exists(user_email):
        print('Email already exists!')
        user_email = input('Enter a different email: ')
        
    user_age = input('Enter Your Age:')
    user_password = input('Enter Your Password:')
    


    
    user_id = "".join([str(rd.randint(1,9)) for _ in range(9)]) # აგენერირებს რანდომ ID-ს მომხმარებლისთვის
    while user_id in ALL_ID : # თავიდან აგენერირებს მომხმარებლის ID იმ შემთხვევაში თუ ID უკვე არსებობს
        user_id = generate_id()


    new_user = {
        "name": user_name,
        "email": user_email,
        "user_age": user_age,
        "user_password":user_password,
        "balance": 0,
        "role": "user",
        "id": user_id   

    }
    
    
    converted_user = anonymous_convert(new_user)
    Users.append(converted_user)
    print('ანგარიში წარმატებით შეიქმნა✅')
    save()


def user_login():
    user_name = input('Enter your UserName: ')
    user_password = input('Enter Your Password')

    potencial_user ={
        "name": user_name,
        "password": user_password
    }
    result = anonymous_convert(potencial_user)
    for user in Users:
        if user["name"] == result["name"] and user["user_password"] == result['password']:
            current_user = anonymous_reconvert(user)
            print(f'მოგესალმებით: {potencial_user["name"]}')
            print(current_user)
        else:
            print("მომხმარებელი ან პაროლი არასწორია ❌")




if __name__ == "__main__":
    while(True):
        main()










# current_user = None
