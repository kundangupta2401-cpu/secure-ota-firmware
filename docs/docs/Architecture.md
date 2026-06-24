# Secure OTA Architecture

## Workflow

Developer
    |
    v
Firmware Package
    |
    v
SHA256 Hash Generation
    |
    v
RSA Digital Signature
    |
    v
Firmware Storage
    |
    v
IoT Device
    |
    +--> Verify Signature
    |
    +--> Verify Hash
    |
    +--> Check Version
    |
    v
Install Firmware

## Components

1. Firmware Package
2. Signing Module
3. OTA Server
4. Cloud Storage
5. IoT Device Agent