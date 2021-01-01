def passwd_dict(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#','\n')):
                user_rec = line.split(':')
                users[user_rec[0]] = int(user_rec[2])
    return users

result = passwd_dict('/etc/passwd')

for key in result.keys():
    print(key,result[key])
