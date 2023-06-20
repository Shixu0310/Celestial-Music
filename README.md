<h1 align="center">
  <img src="static\picture\logo.svg" alt="JAVClub" width="200">
</h1>

❗ | **本项目为python大作业所用，大一时期的个人工作，对于其他项目可能有一定的借鉴作用（事后会在板块中说明清楚）如有侵权，请联系我删除。**
:---: | :---
⚠️ | 因为是作业，所以此项目以展示和记录为主，这是本人第一次尝试开发前端，基本为边学边做，项目疏漏的地方一定很多，欢迎指正！再次强调（只供学习，如果涉及版权等问题，作者立刻删仓库跑路！）

## Introduction
该项目是一个**歌曲偏好分析系统**，它可以抓取特定用户的网易云音乐数据，进行相关处理，然后在网页上将数据可视化。它还包括根据用户的喜好向他们推荐艺术家和歌单，以及分析艺术家的听众用户情况。项目中存在大量私货，~~请谨慎使用~~
![](static\picture\keainie.gif)

## Technology Included

设计语言：Python + CSV + HTML + CSS + JS

数据爬虫：NeteaseCloudMusicApi + Requset + etree + json 

数据清洗：re + replace + join + spilt

可视化：Flask + Echarts + WordCloud + Html

文本分析：jieba2

数据存储：CSV


## Features

- 支持使用网易云用户id登录
- 支持查询开放数据的用户信息
- 支持对登录用户喜爱的歌手可视化展示
- 支持展示用户最喜爱的top100歌曲
- 支持展示用户听歌偏好标签统计
- 支持展示用户评论区词云图，以及相关热评信息
- 支持通过作者id搜索任意作者信息
- 支持展示作者粉丝群体性别，居住地统计
- 支持展示作者创作偏好
- 支持展示作者热门歌曲以及热门评论
- 支持为登录用户推荐歌曲以及歌单
- ~~网页中存在各种私货，自行寻找喵~~

## TODO
- [ ] 歌曲搜索页面
- [ ] 基于歌曲的用户群体分析
- [ ] ~~更多私货~~
  
## DEMO
> 没有米，所以不能直接放网址展示在线demo喽，大家下载部署一下喵( ｡ớ ₃ờ)ھ
> 以下会展现一些网页基本情况，用简单的gif来展示哩~
> (附: 有问题/赞助请联系[这里](mailto:bican700066@163.com)) ~~但是我不一定会回复~~

<details>

  <summary>页面展示 (点击展开)</summary>

  ![](img\gif\login.gif)

  ![](img\gif\user.gif)

  ![](img\gif\animation_user.gif)

  ![](img\gif\artist.gif)

  ![](img\gif\animation_artist.gif)

  ![](img\gif\recommend.gif)

  ![](img\gif\logout.gif)

</details>

## 部署

下面的信息可能有一些繁琐枯燥甚至还有错误, 希望还可见谅。~~对于dalao来说肯定easy peace啦╮(๑•́ ₃•̀๑)╭~~
+ 部署内容分为两个板块，请认真阅读。
  
### 网易云api部署
项目中使用了网易云api作为爬虫的一部分，保证了实时爬虫的稳定性同时减少了用户配置爬虫的阶段。
> 详细配置流程请[看这里](https://github.com/Binaryify/NeteaseCloudMusicApi)

部署之前请确保你拥有/完成以下能力/事情:
- Node.js / JavaScript 基础
- 基本的报错阅读能力
- ~~说白了其实只要配置好node环境就可以了（😓）~~

<details>

  <summary>简略部署流程 (点击展开)</summary>

  #### 安装
```
$ git clone git@github.com:Binaryify/NeteaseCloudMusicApi.git
$ cd NeteaseCloudMusicApi
$ npm install
```

  #### 运行
```shell
$ node app.js
```

服务器启动默认端口为 3000, 若不想使用 3000 端口 , 可使用以下命令 : Mac/Linux

```shell
$ PORT=4000 node app.js
```

windows 下使用 git-bash 或者 cmder 等终端执行以下命令 :

```shell
$ set PORT=4000 && node app.js
```

服务器启动默认 host 为 localhost,如果需要更改, 可使用以下命令 : Mac/Linux

```shell
$ HOST=127.0.0.1 node app.js
```

windows 下使用 git-bash 或者 cmder 等终端执行以下命令 :

```shell
$ set HOST=127.0.0.1 && node app.js
```
</details>

### Celestial Music部署

项目使用的是python 3.10，不知道低版本会不会有什么问题。可以通过以下语句创建py 3.10的虚拟环境

```shell
conda create -n music_work python=3.10
```

都是一些很常见的库，可以通过pip来安装。不过这边建议使用虚拟环境捏~
> pip list
```shell
pip install pandas flask bs4 html5lib Jinja2 lxml requests jieba 
pip install wordcloud imageio matplotlib numpy
```
如果还有没有覆盖到的，出现报错时pip一下就可以了

## 启动流程

1. 首先参照部署一中的内容，我们cd到NeteaseCloudMusicApi的目录下，运行以下内容：
```shell
node app.js
```
出现以下内容则说明运行成功：
```powershell
server running @ http://localhost:3000
```

2. 打开新的终端，cd到项目文件夹下，开启虚拟环境，并运行以下内容：
```shell
python app.py
```
出现以下内容则说明运行成功：
```shell
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
Press CTRL+C to quit
```
在浏览器中访问[这里](http://localhost:5000)(运行成功了再点这里哦！！)

## 网页使用教程

1. **进入初始登录界面用户可以使用网易云id登录：**
   - 如果输入的用户id是正常的即可进入用户界面，**注意**因为数据均为现场爬取所以需要等待一段时间，可以在**app.py**终端上查看爬取进程。
   - 爬取阶段请耐心等待~~才不是没有解决的bug呢~~
   - 如果输入错误的用户id将会跳转到**42**报错网址~~这里有彩蛋捏~~
   - 如果爬取失败，将会进入**25252**报错界面

![](img\login.png)

2. **进入用户界面后，用户可以查看基本操作信息：**
    <details>
      <summary>可查看信息 (点击展开)</summary>
      user：

      - Top 10 Listening Tags
             
      - User Avatar
        
      - Basic Information

      - Top100 Hot Music

      - Top100 My Hot Music

      - Favourite Singers Top8

      - Hotword Cloud Chart

      - Popular Reviews

    </details>


3. **下一步操作：**
   - 可以在Dash Menu上选择需要查看的板块
   - 左上角可以收起Dash Menu
   - 右上角有信息提醒板块，logout按钮，Help按钮
   - 右下角齿轮可以更改UI配色
   - 点击Favourite Singers Top8下的歌手名，可以直接跳转到相应歌手界面
   - ~~关注塔菲喵~~没错这就是广告，我不是雏草姬

![](img\user.png)

4. **Search Artist板块：**
   - 搜索板块可以基于作者的id搜索作者
     - 如果id不正确会进入**42**报错页面
     - 如果爬虫运行失败会进入**25252**报错页面，可以在终端查看爬虫运行进程
     - Favourite Singers Top8板块提供了推荐作者以供选择

![](img\search.png)

5. **Recommend To You板块：**
   - Recommended Songs 1~4 推荐了四首当前user可能喜欢的歌曲，是基于网易云的推荐系统实现的。通过用户常听音乐的tag和相关分类搜索获得。
   - Recommended Songs 5~8 同上推荐
   - Singer Hit Song Hot Reviews 推荐了10个歌单并展示了歌单的tag
  
![](img\recommend.png)

6. **Artist板块介绍（通过歌手搜索进入）：**
   <details>
      <summary>可查看信息 (点击展开)</summary>
      artist：

      - Basic Information
             
      - Quantitative Table Of Creative Directions
        
      - Singer Production Label Statistics

      - Singer Fan Gender Statistics Review

      - Heat Map

      - Singer Hit Song Hot Reviews

    </details>

![](img\artist.png)

## 参考说明与鸣谢

本项目在实现的的过程中参考了以下内容：

BiliBili： [基础python+Flask+爬虫 ](https://www.bilibili.com/video/BV12E411A7ZQ?from=search&seid=17327553224685529336) 通过这个课程了解了爬虫的基础知识并且学习了网站搭建的知识（负基础教程，老师讲的很细很细，我是跳着看的，还是很推荐的

Github： [guanchazhe_spider](https://github.com/hunter-lee1/guanchazhe_spider) 虽然没有参考这个项目的代码，但是上面那个课是这个项目上推荐的，所以姑且也将这个项目放上来 ~~其实这个我没跑通，难绷(•ิ_•ิ)~~

Github： [NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi) 本项目引用了这个项目的部分功能，为了保证实时爬虫爬取的稳定性，同时减轻用户填写cookies和useragent的负担

HTML： [站长之家](https://aspx.sc.chinaz.com/) 本项目使用了来自该网站的网页模板，均为免费资源。本项目在实际设计中对原样板网站做了大量删改，除框架外基本原创。

README:  [JAVClub](https://github.com/JAVClub/core) 本项目的README书写参考了部分该项目的README内容，作者第一次写README见谅。~~不要在意为什么是这篇~~

Echarts： [Echarts](https://echarts.apache.org/zh/index.html) 本项目内的可视化方案大部分由echarts提供，项目中引用了echarts.js和bmap.js两个JS文件

miHoYo： [miHoYo](https://www.mihoyo.com/) 本项目界面中引用了部分来自米哈游旗下的三款游戏中的画面，特别是引用了"银狼"这一虚拟形象，如有侵权，马上删除 ~~dddd~~

Music_163： [Music_163](https://music.163.com/) 本项目爬取的均为网易云音乐中的内容，数据均来源于网易云音乐。



## 后续

先感谢看完这篇废话连篇的使用文档, 有很多东西可能没有说明白, 如果有问题请尽管开 IS 来轰炸我吧

正常来讲现在整套系统应该是可以正常工作的, 如果没有请再次检查是否漏掉了任何一个步骤


