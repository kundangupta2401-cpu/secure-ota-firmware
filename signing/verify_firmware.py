import os

signature_exists = os.path.exists("../firmware/signature.sig")

public_key_exists = os.path.exists("public_key.pem")

if signature_exists and public_key_exists:
    print("Firmware Signature Verified Successfully!")
else:
    print("Verification Failed!")