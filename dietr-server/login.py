import hashlib

def handleLogin(postvars, response):
    import mysqldietr

    mysqldietr.cur.execute("SELECT * FROM accounts WHERE email LIKE '" + postvars["email"] + "'")
    # SELECT * FROM items WHERE items.xml LIKE '%123456%'

    #hashlib.sha512(b"Nobody inspects the spammish repetition").hexdigest()

    return ["text/plain", "0"]
    #also returns session

# login possible response:
# 0 - fail, unknown error
# 1 - success
# 2 - fail, username not exist
# 3 - fail, password wrong