import numpy as np

def professional_matrix_crypto():
    print("="*40)
    print(" PASSWORD ENCRYPTION SYSTEM (LINEAR ALGEBRA)")
    print("="*40)

    # Key Matrix
    K = np.array([[3, 3], 
                  [2, 5]])

    det = int(np.linalg.det(K))

    print(f"[*] Key Matrix (K):\n{K}")
    print(f"[*] Determinant of K: {det}")

    if det == 0:
        print("[!] Error: Key matrix is singular (not invertible).")
        return

    # Input
    password = input("\n[>] Enter password to encrypt: ")

    if len(password) % 2 != 0:
        password += " "

    # Encryption
    ascii_values = [ord(char) for char in password]
    P = np.array(ascii_values).reshape(-1, 2).T
    C = np.dot(K, P)

    print("\n--- ENCRYPTION PHASE ---")
    print(f"Original Text: '{password}'")
    print(f"Ciphertext Matrix (C = K*P):\n{C}")

    # 🔥 Ask user for decryption
    choice = input("\nDo you want to decrypt the password? (yes/no): ").lower()

    if choice == "yes":
        print("\n--- DECRYPTION PHASE ---")

        K_inv = np.linalg.inv(K)
        P_decrypted = np.dot(K_inv, C)

        plain_values = np.round(P_decrypted).T.flatten().astype(int)
        decrypted_text = "".join([chr(val) for val in plain_values])

        print(f"Inverse Key Matrix (K⁻¹):\n{K_inv}")
        print(f"Decrypted ASCII: {plain_values}")
        print(f"Final Decrypted Password: {decrypted_text.strip()}")

    else:
        print("\n[!] Decryption skipped.")

    print("="*40)


if __name__ == "__main__":
    professional_matrix_crypto()