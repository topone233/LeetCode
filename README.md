# 自动发送 LeetCode每日一题

利用Action 每天早上八点 发送LeetCode每日一题。

适用于电脑不在身边或者不方便打开电脑的情况下查看每日一题。

灵感来自于 Wchert 的项目：https://github.com/Wchert/leetcode-every-day-auto-push

## 使用
1. Fork此项目
2. 配置postplus推送或者邮箱发送
- postplus配置如下：在仓库Settings -> Secrets -> New Repository Secret -> 创建 TOKEN，如无需配置邮箱则无视下面所有步骤
- 邮箱配置如下：
1. 在仓库Settings -> Secrets -> New Repository Secret -> 创建 MAILPASSWORD、MAILUSERNAME（邮箱密码、用户名）
2. 开启邮箱STOMP服务，记得保存授权码（作为密码 也就是MAILPASSWORD）
3. 如果是163邮箱跳过。其他邮箱服务器，记得修改邮箱地址
4. Actions -> LeetCode -> Run workflowe 大功告成！