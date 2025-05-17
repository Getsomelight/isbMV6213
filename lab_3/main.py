from RSA import *
from tripleDES import *
from file import *


def generate_keys(
    size: int, private_key_path: str, public_key_path: str, encrypted_key_path: str
) -> None:
    """
    Generate symmetric key by 3DEC, and private and public keys by RSA
    Save private and public keys, encrypt public key with symmetric key and save it
    """
    symmetric_key = generate_3des_key(size)
    private_key, public_key = generate_rsa_key()
    serialize_keys(private_key, public_key, private_key_path, public_key_path)
    encrypted_symmetric_key = encrypt_rsa(public_key, symmetric_key)
    save_binary_file(encrypted_key_path, encrypted_symmetric_key)


def encrypt_text(
    private_key_path: str,
    encrypted_key_path: str,
    text_to_encrypt_path: str,
    result_path: str,
) -> None:
    """
    Encrypting text file by using symmetric key
    """
    private_key_pem = open_binary_file(private_key_path)
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    encrypted_symmetric_key = open_binary_file(encrypted_key_path)
    symmetric_key = decrypt_rsa(private_key, encrypted_symmetric_key)
    text = open_file(text_to_encrypt_path)
    encrypted_text = encrypt_3des(text, symmetric_key)
    save_binary_file(result_path, encrypted_text)


def decrypt_text(
    private_key_path: str,
    encrypted_key_path: str,
    text_to_decrypt_path: str,
    result_path: str,
) -> None:
    """
    Decrypting text file by using symmetric key
    """
    private_key_pem = open_binary_file(private_key_path)
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    encrypted_symmetric_key = open_binary_file(encrypted_key_path)
    symmetric_key = decrypt_rsa(private_key, encrypted_symmetric_key)
    encrypted_text = open_binary_file(text_to_decrypt_path)
    decrypted_text = decrypt_3des(encrypted_text, symmetric_key)
    save_file(result_path, decrypted_text)


def main():
    """
    Provides operations to create keys, encode and decode text
    """
    args = parse()
    paths = open_json_file("settings.json")
    match (args.generation, args.encryption, args.decryption):
        case (size, False, False):
            size = args.generation
            generate_keys(
                size,
                paths["private_key"],
                paths["public_key"],
                paths["symmetric_key"],
            )
        case (None, True, False):
            encrypt_text(
                paths["private_key"],
                paths["symmetric_key"],
                paths["file"],
                paths["encrypted_file"],
            )
        case (None, False, True):
            decrypt_text(
                paths["private_key"],
                paths["symmetric_key"],
                paths["encrypted_file"],
                paths["decrypted_file"],
            )


if __name__ == "__main__":
    main()
