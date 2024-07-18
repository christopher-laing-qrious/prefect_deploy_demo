#!/usr/bin/env python

import keyring, getpass


def get_or_set_secret(account_name, user_name, reset=False, prefix='cjl_utils.'):
    """
    Get the password for the username out of the keyring.  If the password
    isn't found in the keyring, ask for it from the command line.
    """
    account_name = prefix + account_name
    password = None

    if not reset:
        password = keyring.get_password(account_name, user_name)

    if not password or reset:
        print("Configuring utility. Enter secret: ")
        password = getpass.getpass()
        keyring.set_password(account_name, user_name, password)

    return password


if __name__ == "__main__":
    password = get_or_set_secret('prefect_test', 'ansible_vault_password')
    print(password)



