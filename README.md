# encryption-script.rs
encryption script in Rust that uses the RustCrypto library for cryptographic operations

This script generates a random 256-bit key and a random 128-bit initialization vector (IV) using the OsRng provided by the rand library. It then hashes the key using the SHA-256 algorithm to derive a 256-bit key that can be used with the AES-256 encryption algorithm. The script encrypts a plaintext message ("Hello, world!") using AES-256 in CBC mode with the derived key and IV, and prints the key, IV, and ciphertext in hexadecimal format.



