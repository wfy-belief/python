## 版本更新说明

优化了index的大小，删除繁琐代码，但保留原来代码文件。

- index.html 从 12KB 减少到  3KB
- 修改样式 主页面大小为 `95%`
- 了解新的可视化方法
- 把加载的脚本隐藏到 `div[@id='app']`标签内

## 基于docsify可视化使用

引入插件

```
<script src="//cdn.jsdelivr.net/npm/echarts@latest/dist/echarts.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/docsify-echarts-plugin/lib/index.min.js"></script>
```

然后md文档生成代码块

```
` ` `chart

` ` `
```

里面传递的参数为json格式，可以在echarts官网参考示例，然后复制代码，到浏览器console命令行执行 `JSON.stringify(option)` 仅供参考。

## 通用

[寻找可视化插件](https://docsify.js.org/#/awesome?id=plugins) 执行查找 `echarts` 即可

例如示例 [gallery](https://gallery.pyecharts.org/#/Grid/grid_multi_yaxis)

md文档添加如下代码即可

```
<iframe width="900px" height="500px" src="./grid_multi_yaxis.html"></iframe>
```

展示

<p align="center"><iframe width="100%" height="530px" src="./grid_multi_yaxis.html"></iframe></p>

## 首页

E-mail: 1335680234@qq.com

[Github](<https://github.com/wfy-belief>)

## python
python学习的文档，构建于docsify，地址为wfyblog.cn/python

1. 初始化仓库

   ```
   git  init
   ```

2. 于远程仓库建立连接

   ```
   git remote add origin https://github.com/wfy-belief/python.git
   ```

3. 拉取远程主分支

   ```
   git pull origin master
   ```

4. 推送到远程分支

   ```
   git push -u origin master
   ```

这样就与远程仓库建立了连接就可以用Git提交代码了

```
git add .     //将代码放到缓存区
git commit -m""   //提交到本地仓库
git push          //推送到远程
```
## 可视化展示1

```chart
{
    color: ['#3398DB'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [
        {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisTick: {
                alignWithLabel: true
            }
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            name: '直接访问',
            type: 'bar',
            barWidth: '60%',
            data: [10, 52, 200, 334, 390, 330, 220]
        }
    ]
};

```


## 可视化展示2




```chart
{"backgroundColor":"#0f375f","tooltip":{"trigger":"axis","axisPointer":{"type":"shadow"}},"legend":{"data":["line","bar"],"textStyle":{"color":"#ccc"}},"xAxis":{"data":["2020-8-6","2020-8-7","2020-8-8","2020-8-9","2020-8-10","2020-8-11","2020-8-12","2020-8-13","2020-8-14","2020-8-15","2020-8-16","2020-8-17","2020-8-18","2020-8-19","2020-8-20","2020-8-21","2020-8-22","2020-8-23","2020-8-24","2020-8-25"],"axisLine":{"lineStyle":{"color":"#ccc"}}},"yAxis":{"splitLine":{"show":false},"axisLine":{"lineStyle":{"color":"#ccc"}}},"series":[{"name":"line","type":"line","smooth":true,"showAllSymbol":true,"symbol":"emptyCircle","symbolSize":15,"data":[198.942212563156,366.8060699512149,196.48967479337725,24.29298675810525,168.0338457269178,153.5156766806652,223.4195712611015,181.6460561593846,213.45620369147406,82.00441926151765,157.38645624463098,183.16585974533535,239.93047972498016,179.88631616746625,123.39764182675036,113.29055089043462,280.8749699195737,325.44613516324455,176.2889275563062,69.11124457501114]},{"name":"bar","type":"bar","barWidth":10,"itemStyle":{"barBorderRadius":5,"color":{"x":0,"y":0,"x2":0,"y2":1,"type":"linear","global":false,"colorStops":[{"offset":0,"color":"#14c8d4"},{"offset":1,"color":"#43eec6"}]}},"data":[97.88187483052462,194.49269817041207,36.21757125044858,0.45554376375225303,131.02762043759824,22.75921309225599,42.58443238130387,140.9373854855118,148.98963559302598,59.79003018838185,153.09649883939764,157.64904164280122,154.48031843379954,150.11893296432376,119.31654201071376,6.402649516036796,94.86033856249989,154.7511176577258,124.59229259544351,51.35249168772948]},{"name":"line","type":"bar","barGap":"-100%","barWidth":10,"itemStyle":{"color":{"x":0,"y":0,"x2":0,"y2":1,"type":"linear","global":false,"colorStops":[{"offset":0,"color":"rgba(20,200,212,0.5)"},{"offset":0.2,"color":"rgba(20,200,212,0.2)"},{"offset":1,"color":"rgba(20,200,212,0)"}]}},"z":-12,"data":[198.942212563156,366.8060699512149,196.48967479337725,24.29298675810525,168.0338457269178,153.5156766806652,223.4195712611015,181.6460561593846,213.45620369147406,82.00441926151765,157.38645624463098,183.16585974533535,239.93047972498016,179.88631616746625,123.39764182675036,113.29055089043462,280.8749699195737,325.44613516324455,176.2889275563062,69.11124457501114]},{"name":"dotted","type":"pictorialBar","symbol":"rect","itemStyle":{"color":"#0f375f"},"symbolRepeat":true,"symbolSize":[12,4],"symbolMargin":1,"z":-10,"data":[198.942212563156,366.8060699512149,196.48967479337725,24.29298675810525,168.0338457269178,153.5156766806652,223.4195712611015,181.6460561593846,213.45620369147406,82.00441926151765,157.38645624463098,183.16585974533535,239.93047972498016,179.88631616746625,123.39764182675036,113.29055089043462,280.8749699195737,325.44613516324455,176.2889275563062,69.11124457501114]}]}
```





## 可视化展示3



```chart
{"title":{"text":"Anscombe's quartet","left":"center","top":0},"grid":[{"x":"7%","y":"7%","width":"38%","height":"38%"},{"x2":"7%","y":"7%","width":"38%","height":"38%"},{"x":"7%","y2":"7%","width":"38%","height":"38%"},{"x2":"7%","y2":"7%","width":"38%","height":"38%"}],"tooltip":{"formatter":"Group {a}: ({c})"},"xAxis":[{"gridIndex":0,"min":0,"max":20},{"gridIndex":1,"min":0,"max":20},{"gridIndex":2,"min":0,"max":20},{"gridIndex":3,"min":0,"max":20}],"yAxis":[{"gridIndex":0,"min":0,"max":15},{"gridIndex":1,"min":0,"max":15},{"gridIndex":2,"min":0,"max":15},{"gridIndex":3,"min":0,"max":15}],"series":[{"name":"I","type":"scatter","xAxisIndex":0,"yAxisIndex":0,"data":[[10,8.04],[8,6.95],[13,7.58],[9,8.81],[11,8.33],[14,9.96],[6,7.24],[4,4.26],[12,10.84],[7,4.82],[5,5.68]],"markLine":{"animation":false,"label":{"formatter":"y = 0.5 * x + 3","align":"right"},"lineStyle":{"type":"solid"},"tooltip":{"formatter":"y = 0.5 * x + 3"},"data":[[{"coord":[0,3],"symbol":"none"},{"coord":[20,13],"symbol":"none"}]]}},{"name":"II","type":"scatter","xAxisIndex":1,"yAxisIndex":1,"data":[[10,9.14],[8,8.14],[13,8.74],[9,8.77],[11,9.26],[14,8.1],[6,6.13],[4,3.1],[12,9.13],[7,7.26],[5,4.74]],"markLine":{"animation":false,"label":{"formatter":"y = 0.5 * x + 3","align":"right"},"lineStyle":{"type":"solid"},"tooltip":{"formatter":"y = 0.5 * x + 3"},"data":[[{"coord":[0,3],"symbol":"none"},{"coord":[20,13],"symbol":"none"}]]}},{"name":"III","type":"scatter","xAxisIndex":2,"yAxisIndex":2,"data":[[10,7.46],[8,6.77],[13,12.74],[9,7.11],[11,7.81],[14,8.84],[6,6.08],[4,5.39],[12,8.15],[7,6.42],[5,5.73]],"markLine":{"animation":false,"label":{"formatter":"y = 0.5 * x + 3","align":"right"},"lineStyle":{"type":"solid"},"tooltip":{"formatter":"y = 0.5 * x + 3"},"data":[[{"coord":[0,3],"symbol":"none"},{"coord":[20,13],"symbol":"none"}]]}},{"name":"IV","type":"scatter","xAxisIndex":3,"yAxisIndex":3,"data":[[8,6.58],[8,5.76],[8,7.71],[8,8.84],[8,8.47],[8,7.04],[8,5.25],[19,12.5],[8,5.56],[8,7.91],[8,6.89]],"markLine":{"animation":false,"label":{"formatter":"y = 0.5 * x + 3","align":"right"},"lineStyle":{"type":"solid"},"tooltip":{"formatter":"y = 0.5 * x + 3"},"data":[[{"coord":[0,3],"symbol":"none"},{"coord":[20,13],"symbol":"none"}]]}}]}
```


