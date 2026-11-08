from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

message = "Dit is geheim"

versleuteld = f.encrypt(message.encode())
print(versleuteld)

ontsleuteld = f.decrypt(versleuteld.decode())
print(ontsleuteld)