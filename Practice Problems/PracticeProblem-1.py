'''
Password Strength Checker Instructions:

Write a program that checks if a password is strong based on the following criteria:

1. The password must be at least 8 characters long.
2. It must contain at least one uppercase letter.
3. It must contain at least one lowercase letter.
4. It must contain at least one digit.
5. It must contain at least one special character (e.g., !@#$%^&*()-_+=).

If all the conditions are met, print or return "Strong password".
If any condition is not met, print or return "Weak password".

Bonus:
- Allow the user to enter a password again until a strong one is given.
'''



def check_password(input):
    # Set password checking variables to False
    password_length = False
    password_uppercase = False
    password_lowercase = False
    password_digit = False
    password_specialchar = False
    
    password_strength = []
    specialchar = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", "¬", "±", "§", "©", "®", "™", "†", "‡", "¶", "•", "∆", "∑", "≠", "≥", "≤", "≈", "×", "÷", "€", "£", "¥", "¢", "₹", "↔", "↑", "↓", "←", "→", "∞", "♥", "♠", "♣", "♦", "♪", "♫", "°", "∩", "∪", "≡", "∈", "∉", "√", "∇", "∂", "∀", "∃"]

    while len(password_strength) > 5:
        if len(input) >= 8:
            password_length = True
            password_strength.append(1)
        else:
            password_length = False
        
        if specialchar in input == True:
            password_specialchar = True
            password_strength.append(1)
        else:
            password_specialchar = False