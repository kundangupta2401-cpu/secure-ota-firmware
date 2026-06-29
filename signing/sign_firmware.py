from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Load Private Key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

# Read Firmware
with open("../firmware/firmware_v1.bin", "rb") as firmware:
    firmware_data = firmware.read()

# Sign Firmware
signature = private_key.sign(
    firmware_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Save Signature
with open("../firmware/signature.sig", "wb") as sig_file:
    sig_file.write(signature)

print("Firmware Signed Successfully!")
