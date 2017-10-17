import json

def get_account(name):
    with open(f'{name}.acc') as account_file:
        return json.loads(account_file.read())

def save_account(account):
    name = account['name']
    with open(f'{name}.acc', 'w') as account_file:
        account_file.write(json.dumps(account))

    print('Account "{name}" saved.')


def create_account(name, password):
    account = {
        'name': name,
        'password': password,
        'balance': 0,
    }

    print('Account "{name}" created.')

    save_account(account)

def

