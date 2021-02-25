# DailyReport
中国石油大学（北京）每日自动上报打卡

## 特色

- 使用GitHub Action，妈妈在也不用担心我没有服务器了

- 支持[Server酱](sc.ftqq.com)微信推送，早上起床后可以直接看见上报结果


## 使用前请在本仓库 Settings => Secrets => New repository secret 配置环境变量

|Name |Value|
|---|---|
|TOKEN|从 加油投票平台 上获取的token|
|SCKEY|（可选）Server酱旧消息模板sckey）|
|SENDKEY_TURBO|（可选）Server酱企业微信推送sendkey|

### Q&A

- 如何获取token?

  使用fiddler（[下载地址](https://www.telerik.com/download/fiddler)）在电脑上抓包。
  
  fiddler建议使用第4版（亦称Classic版，2021.02.25）。
  
  建议使用微信电脑版抓包，因为手机微信7.0以后对安卓只信任自己内置的SSL证书（[详细信息](https://testerhome.com/topics/17746))，或者可以尝试iOS。
  
- 如何配置Server酱?

  请致其[官网](sc.ftqq.com)查看
  

