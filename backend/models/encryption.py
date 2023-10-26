


# from argon2 import PasswordHasher


# def hash_password(password):
#     ph = PasswordHasher()
#     hashed_password = ph.hash(password)
#     return hashed_password

# def check_password(input_password, stored_hashed_password):
#     ph = PasswordHasher()
#     try:
#         return ph.verify(stored_hashed_password, input_password)
#     except Exception:
#         return False