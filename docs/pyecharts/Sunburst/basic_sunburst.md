
## pyecharts 代码 / 效果

```python
from pyecharts.charts import Sunburst
from pyecharts import options as opts

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=sunburst-simple

目前无法实现的功能:

1、
"""

data = [
    opts.SunburstItem(
        name="Grandpa",
        children=[
            opts.SunburstItem(
                name="Uncle Leo",
                value=15,
                children=[
                    opts.SunburstItem(name="Cousin Jack", value=2),
                    opts.SunburstItem(
                        name="Cousin Mary",
                        value=5,
                        children=[opts.SunburstItem(name="Jackson", value=2)],
                    ),
                    opts.SunburstItem(name="Cousin Ben", value=4),
                ],
            ),
            opts.SunburstItem(
                name="Father",
                value=10,
                children=[
                    opts.SunburstItem(name="Me", value=5),
                    opts.SunburstItem(name="Brother Peter", value=1),
                ],
            ),
        ],
    ),
    opts.SunburstItem(
        name="Nancy",
        children=[
            opts.SunburstItem(
                name="Uncle Nike",
                children=[
                    opts.SunburstItem(name="Cousin Betty", value=1),
                    opts.SunburstItem(name="Cousin Jenny", value=2),
                ],
            )
        ],
    ),
]

sunburst = (
    Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .add(series_name="", data_pair=data, radius=[0, "90%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    .render("basic_sunburst.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Sunburst/basic_sunburst.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Sunburst/basic_sunburst.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Sunburst/basic_sunburst.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Sunburst/basic_sunburst.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Sunburst/basic_sunburst.md"><button class="mybutton">本页markdown原文档</button></a>