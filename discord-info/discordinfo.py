#tokeninfo python module ~ github.com/7uk

#tokeninfo is a tool created for simply looking up discord account data with the use of an account token.

import requests
import json

cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}

def help():
    return """
	[+] Welcome to tokeninfo | Tool for discord token information
                            < doop | github/7uk >       
			
	[+] General Commands:
	
	  [-] tokeninfo.user()        |  Returns general user data
	  [-] tokeninfo.payment()     |  Returns payment data

	[+] Specific Commands:
	
	  [-] tokeninfo.username()    |  Returns accounts username
	  [-] tokeninfo.phonenumber() |  Returns accounts phonenumber
	  [-] tokeninfo.userid()      |  Returns accounts user ID
	  [-] tokeninfo.avatar()      |  Returns accounts avatar	
	  [-] tokeninfo.email()       |  Returns accounts email
	  [-] tokeninfo.auth()        |  Returns accounts 2FA status
	  [-] tokeninfo.flags()       |  Returns accounts flags
	  [-] tokeninfo.language()    |  Returns accounts language	  
	  [-] tokeninfo.verified()    |  Returns accounts email verification	  
	
	[INFO] Use commands within a file & with a token argument.
	[INFO] Example: tokeninfo.email(token)
	"""


def user(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
		
        return user_name, user_id, avatar_id, avatar_url, phone_number, email, mfa_enabled, flags, locale, verified

    else:
        return 'tokeninfo ERROR: Improper token passed.'
		
def payment(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    billing_info = []
    for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
        y = x['billing_address']
        name = y['name']
        address_1 = y['line_1']
        address_2 = y['line_2']
        city = y['city']
        postal_code = y['postal_code']
        state = y['state']
        country = y['country']

        if x['type'] == 1:
            cc_brand = x['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = x['last_4']
            cc_month = str(x['expires_month'])
            cc_year = str(x['expires_year'])
                        
            data = {
                'Payment Type': 'Credit Card',
                'Valid': not x['invalid'],
                'CC Holder Name': name,
                'CC Brand': cc_brand.title(),
                'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                'Address 1': address_1,
                'Address 2': address_2 if address_2 else '',
                'City': city,
                'Postal Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default Payment Method': x['default']
            }
            billing_info.append(data)
        elif x['type'] == 2:
            data = {
                'Payment Type': 'PayPal',
                'Valid': not x['invalid'],
                'PayPal Name': name,
                'PayPal Email': x['email'],
                'Address 1': address_1,
                'Address 2': address_2 if address_2 else '',
                'City': city,
                'Postal Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default Payment Method': x['default']
            }

            billing_info.append(data)
            return billinginfo
			
def username(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        return user_name
    else:
        return 'tokeninfo ERROR: Improper token passed.'

def userid(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        user_id = res_json['id']
        return user_id
    else:
        return 'tokeninfo ERROR: Improper token passed.'
		
def avatar(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        return avatar_url
    else:
        return 'tokeninfo ERROR: Improper token passed.'

def phonenumber(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        phone_number = res_json['phone']
        return phone_number
    else:
        return 'tokeninfo ERROR: Improper token passed.'

def email(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        email = res_json['email']
        return email
    else:
        return 'tokeninfo ERROR: Improper token passed.'

def auth(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        mfa_enabled = res_json['mfa_enabled']
        return mfa_enabled
    else:
        return 'tokeninfo ERROR: Improper token passed.'

def flags(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        flags = res_json['flags']
        return flags
    else:
        return 'tokeninfo ERROR: Improper token passed.'

def language(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        locale = res_json['locale']
        return locale
    else:
        return 'tokeninfo ERROR: Improper token passed.'

def emailverified(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
	
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
	
    if res.status_code == 200:
        res_json = res.json()
        verified = res_json['verified']
        return verified
    else:
        return 'tokeninfo ERROR: Improper token passed.'

if __name__ == "__main__":
    print(help())
