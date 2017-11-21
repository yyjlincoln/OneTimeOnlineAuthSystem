import requests
Final={}
def get():
    #GET http://localhost:80/auth 参数:key=您的序列号/密码 类型:str
    #这里用KEY这个变量代替
    KEY=str(input('输入你要验证的序列号/密码/... >'))
    Content=requests.get('http://localhost:80/auth',{'key':KEY})._content.decode()
    print('服务器已返回数据,开始分析')
    Data=Content.split('\n')
    Final={}
    if len(Data)>=2:
        if Data[0]=='{' and Data[-1]=='}':
            for x in Data:
                if x!='{' and x!='}':
                    y=x.split('=')
                    if len(y)==2:
                        Final[y[0]]=y[1]
    if Final['Succeed'] == 'true': 
        print('验证成功,剩余验证次数:'+Final['Remaining']+' 已使用'+Final['Used']+'次.')
    elif Final['Succeed']=='used':
        print('该验证码已过期')
    elif Final['Succeed']=='false':
        print('验证失败(不匹配)')
    else:
        print('无法验证.RAW Messages:')
        print(Final)
print('验证开始.')
get()
print('验证结束.')
#可以删除下面的内容
from time import sleep
sleep(5)
