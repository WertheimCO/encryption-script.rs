use rand::RngCore;
use rand::rngs::OsRng;
use sha2::{Sha256, Digest};
use aes::Aes256;
use block_modes::{BlockMode, Cbc};
use block_modes::block_padding::Pkcs7;

type Aes256Cbc = Cbc<Aes256, Pkcs7>;

fn main() {
    let plaintext = b"Hello, world!";

    // Generate a random 256-bit key
    let mut key = [0u8; 32];
    OsRng.fill_bytes(&mut key);

    // Generate a random 128-bit IV
    let mut iv = [0u8; 16];
    OsRng.fill_bytes(&mut iv);

    // Hash the key with SHA-256 to derive a 256-bit key for AES
    let mut hasher = Sha256::new();
    hasher.update(&key);
    let key_hash = hasher.finalize();

    // Encrypt the plaintext with AES-256 in CBC mode using the derived key and IV
    let cipher = Aes256Cbc::new_from_slices(&key_hash, &iv).unwrap();
    let ciphertext = cipher.encrypt_vec(plaintext);

    // Print the key, IV, and ciphertext in hexadecimal format
    println!("Key:     {:?}", hex::encode(&key));
    println!("IV:      {:?}", hex::encode(&iv));
    println!("Ciphertext: {:?}", hex::encode(&ciphertext));
}
