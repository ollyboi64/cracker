import itertools
import hashlib

def brute_force_password_cracker(target_hash, max_length=4):

    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    for length in range(1, max_length + 1):
        # Generate all combinations of the specified length
        for guess in itertools.product(charset, repeat=length):
            # Join the tuple of characters into a string
            password_guess = ''.join(guess)
            # Calculate the MD5 hash of the guessed password
            hashed_guess = hashlib.md5(password_guess.encode()).hexdigest()
            # Check if the generated hash matches the target hash
            if hashed_guess == target_hash:
                print(f"Password found: {password_guess}")
                return password_guess
    
    print("Password not found.")
    return None

# Example usage:
# Replace '5f4dcc3b5aa765d61d8327deb882cf99' with your target MD5 hash.
target_hash = '5f4dcc3b5aa765d61d8327deb882cf99'  # This is the MD5 for 'password'
brute_force_password_cracker(target_hash)