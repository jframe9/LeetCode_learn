

'''
        929. 独特的电子邮件地址
        好好地审题最重要！！！！！
'''

def numUniqueEmails(emails):
    result_list = []
    for item in emails:
        if "@" not in item:
            return 0
        if "@" in item:
            mail_list = item.split('@')
            if '.' in mail_list[0]:
                res_point = mail_list[0].replace('.', '')
                print(res_point)
                if '+' in res_point:
                    res_plus = res_point.split('+')
                    result_list.append(res_plus[0] + "@" + mail_list[1])
                else:
                    result_list.append(res_point + "@" + mail_list[1])
            else:
                if '+' in mail_list[0]:
                    res_plus = mail_list[0].split('+')
                    result_list.append(res_plus[0] + "@" + mail_list[1])
                else:
                    result_list.append(mail_list[0] + "@" + mail_list[1])
    return list(set(result_list))
    # seen = set()
    # for email in emails:
    #     local, domain = email.split('@')
    #     if '+' in local:
    #         local = local[:local.index('+')]
    #     seen.add(local.replace('.', '') + '@' + domain)
    # return seen




res = numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(res)
