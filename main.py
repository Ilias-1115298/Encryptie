from cryptography.fernet import Fernet
from sleutelbeheer import sleutel_laden

key = sleutel_laden()

f = Fernet(key)

message = "Dit is geheim"

versleuteld = f.encrypt(message.encode())
print(versleuteld)

ontsleuteld = f.decrypt(versleuteld)
print(ontsleuteld.decode())