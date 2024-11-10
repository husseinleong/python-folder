
email = input('Enter your email: ')

index = email.index("@")
# husseinleong@gmail.com
username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")