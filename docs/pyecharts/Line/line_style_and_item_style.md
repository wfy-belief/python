
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-style

目前无法实现的功能:

暂无
"""


(
    Line(init_opts=opts.InitOpts(width="1280px", height="720px"))
    .add_xaxis(xaxis_data=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    .add_yaxis(
        series_name="",
        y_axis=[120, 200, 150, 80, 70, 110, 130],
        symbol="triangle",
        symbol_size=20,
        linestyle_opts=opts.LineStyleOpts(color="green", width=4, type_="dashed"),
        label_opts=opts.LabelOpts(is_show=False),
        itemstyle_opts=opts.ItemStyleOpts(
            border_width=3, border_color="yellow", color="blue"
        ),
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .render("line_style_and_item_style.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Line/line_style_and_item_style.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_style_and_item_style.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_style_and_item_style.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Line/line_style_and_item_style.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_style_and_item_style.md"><button class="mybutton">本页markdown原文档</button></a>