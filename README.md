# 简介
有点像序列号服务器，基于flask，对Get方式提交的序列号(密码)进行验证，并对已验证序列号进行作废处理(练手项目)
# 使用方式
在软件目录创建Key文件。待程序读取完毕之后，所有的数据均已导入到程序中。
验证方式: GET http://localhost:80/auth?key=需要验证的秘钥
返回格式: 
{
Succeed=true/false/used/server_error #验证状态
Remaining=1/2/3/... #剩余可使用次数 *不一定有
Used=1/2/3/... #使用了多少次 *不一定有
}
