## 背景介绍

某美发网上商城（以下简称S商城）在微信平台上举办了一场在线投票活动，微信用户可通过活动链接访问到投票页面，对喜欢的发型师作品进行投票；每个微信帐号每天只能给单个作品投1张选票。

投票活动页面如下图所示：

![](images/voteRobot_01.png)

该投票活动的选票计数程序运行在S商城的服务器上，微信用户访问投票页面时，经过了微信服务器的转发，其网络拓扑结果示意图如下图所示：

![](images/voteRobot_02.png)

S商城的选票计数程序存在系统漏洞，对投票请求的报文参数进行替换以后，选票计数程序无法判断投票的真实性，仍然进行正常计票。因此，可以利用工具模拟微信用户的投票请求，通过动态替换投票中的微信ID，实现批量投票的投票机器人（VoteRobot）。

若需了解漏洞的详细发现过程，可查看[网站微信投票系统“批量投票”漏洞](http://52test.org/posts/voting-system-flaw-on-wechat.html)。

## VoteRobot介绍

投票的原理确定后，就可采用任何一种编程语言轻松实现了。在这里提供了2种实现方式，Python和LoadRunner C Vuser。

在Python中执行代码后，输入日志如下所示：

```
VoteHelper.py [39] INFO: Start Voting to zpid(38), Total votes: 3
VoteHelper.py [43] INFO: 1 tickets has been voted, the next ticket will be voted after 35 seconds.
VoteHelper.py [43] INFO: 2 tickets has been voted, the next ticket will be voted after 31 seconds.
VoteHelper.py [43] INFO: 3 tickets has been voted, the next ticket will be voted after 10 seconds.
VoteHelper.py [45] INFO: Voting Ended!
[Finished in 76.8s]
```