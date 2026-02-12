import os
import pickle

def unsafe_deserialize(data):
    return pickle.loads(data)

def sql_injection_example(user_input):

    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    return query

def command_injection(filename):
    os.system("cat " + filename)

