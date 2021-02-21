
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import pyecharts.options as opts
from pyecharts.charts import Parallel

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=parallel-simple
目前无法实现的功能:
1、
"""

parallel_axis = [
    {"dim": 0, "name": "Price"},
    {"dim": 1, "name": "Net Weight"},
    {"dim": 2, "name": "Amount"},
    {
        "dim": 3,
        "name": "Score",
        "type": "category",
        "data": ["Excellent", "Good", "OK", "Bad"],
    },
]

data = [[12.99, 100, 82, "Good"], [9.99, 80, 77, "OK"], [20, 120, 60, "Excellent"]]


(
    Parallel()
    .add_schema(schema=parallel_axis)
    .add(
        series_name="",
        data=data,
        linestyle_opts=opts.LineStyleOpts(width=4, opacity=0.5),
    )
    .render("basic_parallel.html")
)```

<iframe width="100%" height="800px" src="/pyecharts/Parallel/basic_parallel.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Parallel/basic_parallel.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Parallel/basic_parallel.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Parallel/basic_parallel.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Parallel/basic_parallel.md"><button class="mybutton">本页markdown原文档</button></a>