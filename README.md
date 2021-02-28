# DailyReport
中国石油大学（北京）每日自动上报打卡

## 特色

- 使用GitHub Action，每日可定时自动打卡

- 支持[Server酱](sc.ftqq.com)微信推送，早上起床后可以直接看见上报结果


## 使用方法

1. fork本仓库 
2. 配置环境变量 Settings => Secrets => New repository secret

|Name |Value|
|---|---|
|TOKEN|从 加油投票平台 上获取的token|
|SCKEY|（可选）Server酱旧消息模板sckey|
|SENDKEY_TURBO|（可选）Server酱企业微信推送sendkey|

3. （**极其重要**）在 `DailyReport.py` 中配置每天打卡的选项（特别是**地理位置/经纬度**）

### Q&A

- 如何获取token?

  使用fiddler（[下载地址](https://www.telerik.com/download/fiddler)）在电脑上抓包。
  
  fiddler建议使用第4版（亦称Classic版，2021.02.25）。
  
  建议使用微信电脑版抓包，因为手机微信7.0以后对安卓只信任自己内置的SSL证书（[详细信息](https://testerhome.com/topics/17746))，或者可以尝试iOS。
  
  具体过程：
  1. 配置fiddler
      1. 菜单栏 tools => Options... => 选项卡HTTPS
      2. 勾选 Capture HTTPS CONNECTs
      3. 勾选 Decrypt HTTPS traffic
      4. 选择 ...from non-browsers only
      5. 勾选 Ignore server certificate errors (unsafe)
      6. 单击右上方的 Actions => Trust Root Certificate （如果有确认就一路确认）
      7. 单击OK
      8. 重启fiddler（务必）
  2. 打开 微信电脑版 => 打开 加油投票平台 小程序 => 等待其加载完成 => 返回fiddler
  3. 如下图所示即可以获取token

  ![捕获](https://user-images.githubusercontent.com/29673994/109407336-fc609c80-79ba-11eb-9a12-f638153370e9.PNG)
  [无法显示图片?](https://github.com/1299172402/hosts)

- 我可以修改打卡时间吗?

  当然可以，请至 `.github\workflows\DailyReport.yml` 修改corn处的时间  
  现在的时间是每天凌晨三点半，既不会妨碍你零点时抢第一个打卡，又可以保证你起床时已经打好了卡。  

- 如何配置Server酱?

  请至其[官网](sc.ftqq.com)查看

- 能看看相关的api吗?

  请至[此处](https://github.com/1299172402/DailyReport/blob/main/APIInfo.md)
  

