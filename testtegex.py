import re
# - - 比如你妈啊
#   - @今天调教bot了吗 你们啥时候过来啊.jpg
# - - @今天调教bot了吗 你们啥时候过来啊.jpg
#   - pn是个给
regex = r'@\S* |[\[\]]'

test_str='@兜风是薇尔莉特的老板  [dsfa] 请自闭'

print(re.split(regex, test_str))

print(''.join(list(filter(lambda x:x!='',re.split(regex, test_str)))))