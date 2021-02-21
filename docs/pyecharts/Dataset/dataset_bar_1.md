
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
            ["score", "amount", "product"],
            [89.3, 58212, "Matcha Latte"],
            [57.1, 78254, "Milk Tea"],
            [74.4, 41032, "Cheese Cocoa"],
            [50.1, 12755, "Cheese Brownie"],
            [89.7, 20145, "Matcha Cocoa"],
            [68.1, 79146, "Tea"],
            [19.6, 91852, "Orange Juice"],
            [10.6, 101852, "Lemon Juice"],
            [32.7, 20112, "Walnut Brownie"],
        ]
    )
    .add_yaxis(
        series_name="",
        y_axis=[],
        encode={"x": "amount", "y": "product"},
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Dataset normal bar example"),
        xaxis_opts=opts.AxisOpts(name="amount"),
        yaxis_opts=opts.AxisOpts(type_="category"),
        visualmap_opts=opts.VisualMapOpts(
            orient="horizontal",
            pos_left="center",
            min_=10,
            max_=100,
            range_text=["High Score", "Low Score"],
            dimension=0,
            range_color=["#D7DA8B", "#E15457"],
        ),
    )
    .render("dataset_bar_1.html")
)```

<iframe width="100%" height="800px" src="/pyecharts/Dataset/dataset_bar_1.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Dataset/dataset_bar_1.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Dataset/dataset_bar_1.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Dataset/dataset_bar_1.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Dataset/dataset_bar_1.md"><button class="mybutton">本页markdown原文档</button></a>