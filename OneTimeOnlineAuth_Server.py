#Import Keys
with open('key') as f:
    x=f.read()
x=x.split('\n')
y={}
for z in x:
    if z!='':
        y[z.split(',')[0]]=[int(z.split(',')[1]),int(z.split(',')[2])]
#Keys={'123':[5,5],'456':[5,5]}
Keys=y
print(Keys)
Feedback={}
from flask import Flask
from flask import request
app=Flask(__name__)
@app.route('/auth',methods=['GET','POST'])
def main():
    Feedback.clear()
    AuthDetails=dict(request.args)
    if 'key' in AuthDetails:
        Key=AuthDetails['key'][0]
        print('Authing Key '+Key)
        if Key in Keys:
            if len(Keys[Key])>=2:
                if Keys[Key][1]>0:
                    Keys[Key][1]=Keys[Key][1]-1
                    Keys[Key][0]=Keys[Key][0]+1
                    Feedback['Succeed']='true'
                    Feedback['Remaining']=Keys[Key][1]
                    Feedback['Used']=Keys[Key][0]
                    data=''
                    for x in Keys:
                        data=data+'\n'+str(x)
                        for y in Keys[x]:
                            data=data+','+str(y)
                    with open('key','w') as f:
                        f.write(data)
                else:
                    Feedback['Succeed']='used'
            else:
                Feedback['Succeed']='server_error'
        else:
            Feedback['Succeed']='false'
    else:
        print('Authed Failed')
        Feedback['Succeed'] = 'false'
    #Replying
    FeedbackText = '{'
    for x in Feedback:
        FeedbackText = FeedbackText+'\n'+str(x)+'='+str(Feedback[x])
    FeedbackText = FeedbackText+'\n}'
    return FeedbackText
@app.route('/')
def reply():
    return '''Key Authorizer
<br>Please use it like xxx.xxx.xxx.xxx/auth?key=xxx</br>'''
@app.errorhandler(500)
def err_500(info):
    #print(info)
    return '<b>System Error.Please try again later.</b>'
@app.errorhandler(404)
def err_404(info):
    #print(info)
    return '<b>Not Found. Did you mean /auth ?</b>'
app.run(port=80)