"""
Intentionally vulnerable code for SAST testing
"""
import os
import pickle
import subprocess

def unsafe_deserialize(data):
    return pickle.loads(data)


def get_user_data(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query

def read_file(filename):
    os.system("cat " + filename)

def run_command(cmd):
    subprocess.call(cmd, shell=True)

password = "admin123"
api_token = "secret_token_12345"

import hashlib
def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

def calculate(expression):
    return eval(expression)

def validate_user(user):
    assert user.is_admin, "Not an admin"

