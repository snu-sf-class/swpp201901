def create_users(N):
    #ls = [("debt_admin", "debt_adminpasswd")]
    ls = []
    for i in range(1, N):
        ls.append(("test{0}".format(i), "test{0}passwd".format(i)))
    return ls
