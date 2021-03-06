

## 前言

爬取这部分内容呐，是因为需要这方面的数据，所以进行爬取。

## 具体方法

### 观察网站

[郑州的历史天气情况](http://tianqi.2345.com/wea_history/57083.htm)

网络上对此部分爬取方法并不统一，老的接口已经弃用，但是还能够爬取信息。为了锻炼，所以选择新的接口。

打开此网址，然后 `F12` 查看请求信息。

![](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images//blog/20200818120509.png)	点击查看动态请求的资源

![](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images//blog/20200818120711.png)

查看回复的信息

![](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images//blog/20200818120739.png)

观看请求链接的形式，但是谷歌环境下链接不太容易观察，所以去火狐

![](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images//blog/20200818120849.png)

至此链接部分已经观察成功

![](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images//blog/20200818120939.png)

### 查看返回信息

我们炸一看，返回信息是乱码，看起来非常不规范，但是还是能够看到返回的是json格式的信息。所以当我们执行如下都是乱码。

![](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images//blog/20200818121354.png)

所以，我们调用json格式加载

![](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images//blog/20200818121525.png)

### 解析

利用lxml加载之后我们发现（部分内容）

```html
<body><ul class="history-msg">
    <li>平均高温：<em class="orange-txt">31°</em>    平均低温：<em class="blue-txt">23°</em></li>
    <li>极端高温：<em class="orange-txt">34°</em><b>(2019-08-15)</b></li>
    <li>极端低温：<em class="blue-txt">20°</em><b>(2019-08-31)</b></li>
        <li>平均空气质量指数：<em class="blod-txt">58</em></li>
    <li>空气最好：<em class="green-txt">26 优</em><b>(08月02日)</b></li>
    <li>空气最差：<em class="yellow-txt">83良</em><b>(08月26日)</b></li>
    </ul>
<table class="history-table" width="100%">
    <tr>
        <th width="169">日期</th>
        <th width="68">最高温</th>
        <th width="68">最低温</th>
        <th width="122">天气</th>
        <th>风力风向</th>
        <th width="140">空气质量指数</th>    </tr>
        <tr>
        <td>2019-08-01 周四</td>
        <td style="color:#ff5040;">32°</td>
        <td style="color:#3097fd;">23°</td>
        <td>小雨~中雨</td>
        <td>东南风2级</td>
        <td><span class="history-aqi wea-aqi-1">40 优</span></td>    </tr>
        <tr>
        <td>2019-08-02 周五</td>
        <td style="color:#ff5040;">30°</td>
        <td style="color:#3097fd;">24°</td>
        <td>小雨</td>
        <td>东北风2级</td>
        <td><span class="history-aqi wea-aqi-1">26 优</span></td>    </tr>
```

索引全部的tr标签即可，但是第一个tr标签不需要。

## 具体实现

<iframe src="https://nbviewer.jupyter.org/github/wfy-belief/python/blob/master/docs/pandas/tianqi/818.ipynb" width="100%" height="500px" scrolling="yes"></iframe>

## 附录

<p>本次练习使用jupyter notebook，对应预览和在线交互如下。</p>
<a href="https://nbviewer.jupyter.org/github/wfy-belief/python/blob/master/docs/pandas/tianqi/818.ipynb"><button class="mybutton">jupyter notebook在线预览</button></a><a href="https://mybinder.org/v2/gh/wfy-belief/python/master?filepath=docs/pandas/tianqi/818.ipynb"><button class="mybutton">jupyter notebook在线交互（加载时间长）</button></a>

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python@master/docs/pandas/tianqi/818.ipynb"><button class="mybutton">jupyter notebook文档下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python@master/docs/pandas/tianqi/818.md"><button class="mybutton">本页markdown原文档</button></a><a href="https://github.com/wfy-belief/python/blob/master/docs/pandas/tianqi/result.xlsx?raw=true"><button class="mybutton">result.xlsx(无法使用CDN较慢)</button></a>