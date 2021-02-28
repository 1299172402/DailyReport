# 每日上报API

## 这些api的header是通用的

header
|参数名|值|必要性|备注|
|---|---|---|---|
|User-Agent| |不必要|建议使用微信浏览器UA|
|Referer|`https://servicewechat.com/wxd2bebfc67ee4a7eb/73/page-frame.html`|必要| |
|token| |必要|验证身份的token|


## 获取index页面

请求方式：GET
https://reserve.25team.com/wxappv1/yi/index?version=16

- requests

header

form data
|参数名|值|必要性|备注|
|---|---|---|---|
|version|16|可选|有没有version=16好像都会返回最新的版本，不知道有什么用|

- response

只对重要的值做表述

在`response["data"]`中
|参数|含义|
|---|---|
|background|其中的image就是滚动横幅|
|conf_time|打卡的开始和结束时间（单位：时）|
|conf_titles|上报的表单样式|
|enable_reported|是否允许上报|
|is_reported|是否已经上报|
|mapkey|未知|
|mapsign|未知|
|my_reported_num|我的上报总次数|
|notice_txt|滚动提醒文字|
|now_datetime|当前时间|
|reported_num|今日上报数|
|reported_total|总上报数|
|showIssue|显示客服（？不确定）|
|version|当前版本|

## 获取当前学生信息

请求方式：GET
https://reserve.25team.com/wxappv1/yi/getStudentInfo

- requests

header

- response
只对重要的值做表述

在`response["data"]`中
|参数|含义|
|---|---|
|birthplace|生源地|
|college|学院|
|college_id|学院id|
|create_time|此信息的创建时间|
|education|学历（本科/研究生）|
|instructor|辅导员姓名|
|instructor_id|辅导员id|
|mobile|手机号（猜测）|
|role|身份（学生/教师）|
|student_id|打卡人学号|
|truename|打卡人姓名|
|user_id|此用户的id|

## 每日上报

请求方式：POST
https://reserve.25team.com/wxappv1/yi/addReport

- request

header

body
（也只说明部分）

content的内容
表单的题目答案，直接写序号和答案，编号从0开始

location的内容
|参数名|值|必要性|
|---|---|---|
|country|国家名|必要|
|province|省份名|必要|
|city|城市名|必要|
|latitude|纬度|必要|
|longitude|经度|必要|

version即为版本号

- response

打卡成功
`{"code":200,"msg":"ok","data":null}`

已经打过卡了
`{"code":500,"msg":"您今天已经打过卡了，请查看“我的上报”","data":null}`
