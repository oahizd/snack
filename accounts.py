import snaker
# 1.确定在文件里存储的账号信息的结构

# 2.把账号数据读入内存，为了方便使用，可改成list
accounts = {
    # "alex": ["alex", "abc123!", "1"],
}

def create_account():
    f = open("accounts.db", "a")
    flag = str(input("是否需要创建新账号（要的输1，否则输其他任意字符）："))
    if flag == "1":
        account = str(input("请创建一个账号名："))
        email = str(input("请添加一个邮箱："))
        default_status = 0
        if len(account) >= 3 and len(email) >= 6:
            f.write(f"\n{account},{email},{default_status}")
            f.close()
    else:
        f.close()

def log_in_account():
    f = open("accounts.db", "r")
    for line in f:
        line = line.split(",")
        accounts[line[0]] = line
    print(accounts)
    # 3.创建一个loop，要求用户输入账号信息，去判断即可
    count = 0
    while True:
        user = input("Username:").strip()
        if user not in accounts:
            print("该用户未注册...")
            continue
        elif accounts[user][2] == "1\n": #此账号已锁定
            print("此账户已锁定，请联系管理员")
            continue

        while count < 3:         #控制密码
            find1 = "@"
            find2 = "com"
            if find1 in accounts[user][1] and find2 in accounts[user][1]:
                print(f"Welcome {user} 登陆成功")
                return 0
            else:
                print("Wrong email address format, please change")
                em = input("Email:").strip()  # 去账号dict里去判断password对不对
                f = open("accounts.db", "r")
                content = f.read()
                f.close()
                t = content.replace(accounts[user][1], em)
                with open("accounts.db", "w") as f2:
                    f2.write(t)
                f2.close()
                if find1 in em and find2 in em:
                    return 0
            count += 1

        if count == 3:
            print(f"输错了{count}次邮箱，需要锁定账号{user}")
            # 1.先改在内存中dictionary账号信息的用户状态
            # 2.把dictionary里的数据按原account.db数据格式，并且存回文件
            accounts[user][2] = "1"
            f2 = open("accounts.db", "w")
            for user,val in accounts.items():
                line = ",".join(val) + "\n"        # 把列表转成字符
                f2.write(line)
            f2.close()
            return 0

# def score_append():
#     user = input("Username:").strip()
#     f = open("accounts.db", "r")
#     content = f.read()
#     f.close()
#     t = content.replace(accounts[user][3], str(snaker.score))
#     with open("accounts.db", "w") as f2:
#         f2.write(t)
#     f2.close()

if __name__ == '__main__':
    create_account()
    log_in_account()
    snaker.main()
    # score_append()
