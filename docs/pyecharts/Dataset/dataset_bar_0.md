
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_dataset(
        source=[
            ["product", "2015", "2016", "2017"],
            ["Matcha Latte", 43.3, 85.8, 93.7],
            ["Milk Tea", 83.1, 73.4, 55.1],
            ["Cheese Cocoa", 86.4, 65.2, 82.5],
            ["Walnut Brownie", 72.4, 53.9, 39.1],
        ]
    )
    .add_yaxis(series_name="2015", y_axis=[])
    .add_yaxis(series_name="2016", y_axis=[])
    .add_yaxis(series_name="2017", y_axis=[])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Dataset simple bar example"),
        xaxis_opts=opts.AxisOpts(type_="category"),
    )
    .render("dataset_bar_0.html")
)```

<iframe width="100%" height="800px" src="/pyecharts/Dataset/dataset_bar_0.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Dataset/dataset_bar_0.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Dataset/dataset_bar_0.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Dataset/dataset_bar_0.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Dataset/dataset_bar_0.md"><button class="mybutton">本页markdown原文档</button></a>