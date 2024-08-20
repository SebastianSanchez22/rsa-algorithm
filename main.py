import secrets
import sympy

def generate_prime(bits=1024):
    """Generates a large prime number."""
    while True:
        num = secrets.randbits(bits)
        if sympy.isprime(num):
            return num

def calculate_n(p, q):
    """Calculates n as the product of two primes p and q."""
    return p * q

def calculate_phi(p, q):
    """Calculates the Euler's totient function using LCM."""
    return lcm(p - 1, q - 1)

def lcm(a, b):
    """Calculates the Least Common Multiple (LCM) of a and b."""
    return abs(a * b) // gcd(a, b)

def gcd(a, b):
    """Calculates the Greatest Common Divisor (GCD) of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def generate_e(phi):
    """Generates the public exponent e."""
    e = secrets.randbelow(phi - 1) + 1
    while gcd(e, phi) != 1:
        e = secrets.randbelow(phi - 1) + 1
    return e

def modinv(a, m):
    """Calculates the modular inverse of a under modulo m."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keys(bits=1024):
    """Generates the public and private keys."""
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = calculate_n(p, q)
    phi = calculate_phi(p, q)
    e = generate_e(phi)
    d = modinv(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    """Encrypts a plaintext message using the public key."""
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    """Decrypts a ciphertext message using the private key."""
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Example usage
def rsa_example():
    public_key, private_key = generate_keys()
    print("Public key:", public_key)
    print("Private key:", private_key)

    message = "Hello"
    print("Original message:", message)

    encrypted_msg = encrypt(public_key, message)
    print("Encrypted message:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted message:", decrypted_msg)

rsa_example()
