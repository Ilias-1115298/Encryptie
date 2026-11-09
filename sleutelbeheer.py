from cryptography.fernet import Fernet
from pathlib import Path

sleutel_bestand = Path(__file__).parent / "secret.key"

def sleutel_laden():
    if sleutel_bestand.exists():
        return sleutel_bestand.read_bytes()

    key = Fernet.generate_key()
    sleutel_bestand.write_bytes(key)
    return key