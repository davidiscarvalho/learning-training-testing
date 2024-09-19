email = input("enter your email: ")
index = email.index("@")
username = email[:index]
domain = email[index+1:]

print(f"username: {username} - domain: {domain}")