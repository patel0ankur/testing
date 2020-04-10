import active_directory

ad_user = ['john', 'mike', 'chad', 'brad']

for username in ad_user:
    try:
        user = active_directory.find_user(username)
        print(user.cn + ':' + str(user.employeenumber) + ':' + str(user.DISPLAYname) + ':' + str(
            user.EmailAddress) + ':' + str(user.Useraccountcontrol))

        print(user.Useraccountcontrol)
        print(user.name)
        print(user.lastLogon)

    except:
        continue
