
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=line-simple

目前无法实现的功能:

暂无
"""


x_data = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
y_data = [820, 932, 901, 934, 1290, 1330, 1320]


(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .render("basic_line_chart.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Line/basic_line_chart.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/basic_line_chart.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/basic_line_chart.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Line/basic_line_chart.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/basic_line_chart.md"><button class="mybutton">本页markdown原文档</button></a>