# 简介
高达百万级规则！由我原创&整理的 AdGuardHomeRules ADH广告拦截过滤规则！打造全网最强最全规则集

请前往相关介绍博文：https://www.blueskyxn.com/202012/2940.html

# USE

## 主规则
### 国际用户URL
#### 放在黑名单区
- https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/all.txt
- https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/skyrules.txt
#### 放在白名单区
- https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/ok.txt
#### 动漫&漫画网站定制规则
- 三个等级，互不相同，请叠加使用，越高等级越容易误杀
- 目前这个已停止维护
- https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/manhua.txt
- https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/manhua-plus.txt
- https://raw.githubusercontent.com/BlueSkyXN/AdGuardHomeRules/master/manhua-max.txt
### 中国大陆用户特供URL
#### 放在黑名单区
- https://raw.gitcode.com/BlueSkyXN/AdGuardHomeRules/raw/master/all.txt
- https://raw.gitcode.com/BlueSkyXN/AdGuardHomeRules/master/skyrules.txt
#### 放在白名单区
- https://raw.gitcode.com/BlueSkyXN/AdGuardHomeRules/master/ok.txt
#### 动漫&漫画网站定制规则
- 三个等级，互不相同，请叠加使用，越高等级越容易误杀
- 目前这个已停止维护
- https://raw.gitcode.com/BlueSkyXN/AdGuardHomeRules/master/manhua.txt
- https://raw.gitcode.com/BlueSkyXN/AdGuardHomeRules/master/manhua-plus.txt
- https://raw.gitcode.com/BlueSkyXN/AdGuardHomeRules/master/manhua-max.txt



# 更新日志

20210129更新：滥用报告与调整  https://www.blueskyxn.com/202101/3860.html

20210208更新：修改SKYRULE，增加COCOMANHUA/DMZJ定制规则

20210209更新：AdGuardHome根据实际情况自定义拦截规则  https://www.blueskyxn.com/202102/4002.html

20210307更新：V1.3 DNS允许清单：ok.txt 上线。根据实际使用情况，释放一些域名，避免网站/视频不能正常使用【原规则包含隐私和跟踪器拦截，所以比较严格，但是我看大多数还是只需要广告拦截】

20210423更新：V1.4 manhua 拦截清单改名整合升级

20210424更新：V1.5 新增 manhua-max 调整 manhua-plus 基础版manhua新增多个网站

20210424更新：V2.0 大幅度调整整合规则 之后将会定期抓取几个经常更新的规则组

20230608更新：v3.3.2 增加自动化工作流和对应脚本，实现AUTO抓取处理

20230717更新：v3.4.1 针对 https://github.com/BlueSkyXN/AdGuardHomeRules/issues/16 进行了处理，但是最后发现比较麻烦 ，但是发现问题出现在长行匹配上，请更新官方引导进行处理。

20240626更新：v3.5.0 主要修改了Readme.md 信息以便更好的介绍和入门使用，同时借用了gitnode的境内加速（非即时更新，是csdn等中国大陆公司违法爬取的）


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=BlueSkyXN/AdGuardHomeRules&type=Date)](https://star-history.com/#BlueSkyXN/AdGuardHomeRules&Date)
