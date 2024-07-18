#!/usr/bin/env python
import os, getpass

def get_action_string(str_to_encrypt, var_name):
    action_string = f"ansible-vault encrypt_string '{str_to_encrypt}' --name {var_name}"
    return action_string


def get_password():
    password = getpass.getpass(prompt="Enter secret: ")
    return password


def run():
    variable_name = input("Enter variable name: ")
    password = get_password()
    for string, var in [(password, variable_name)]:
        action_string = get_action_string(string, var)
        os.system(action_string)


if __name__ == "__main__":
    run()
