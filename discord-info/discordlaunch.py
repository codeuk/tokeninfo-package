def help():
    print("""
	[+] Welcome to discordinfo | Tool for discord token information
                            < doop | github/7uk >       
			
	[+] General Commands:
	
	  [-] discordinfo.user()        |  Returns general user data
	  [-] discordinfo.payment()     |  Returns payment data

	[+] Specific Commands:
	
	  [-] discordinfo.username()    |  Returns accounts username
	  [-] discordinfo.phonenumber() |  Returns accounts phonenumber
	  [-] discordinfo.userid()      |  Returns accounts user ID
	  [-] discordinfo.avatar()      |  Returns accounts avatar	
	  [-] discordinfo.email()       |  Returns accounts email
	  [-] discordinfo.auth()        |  Returns accounts 2FA status
	  [-] discordinfo.flags()       |  Returns accounts flags
	  [-] discordinfo.language()    |  Returns accounts language	  
	  [-] discordinfo.verified()    |  Returns accounts email verification	  
	
	[INFO] Use commands within a file & with a token argument.
	[INFO] Example: discordinfo.email(token)
	""")
	
if __name__ == "__main__":
    help()