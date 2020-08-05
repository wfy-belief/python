## 首页

E-mail: 1335680234@qq.com

[Github](<https://github.com/wfy-belief>)

# python
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