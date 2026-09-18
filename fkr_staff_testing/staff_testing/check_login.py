def check_login(accounts, username, password):
    for account in accounts:
        if account['login'] == username and account['password'] == password:
            return True
    else:
        return False