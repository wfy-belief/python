
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line

c = (
    Line()
    .add_xaxis(xaxis_data=["一", "二", "三", "四", "五", "六", "七", "八", "九"])
    .add_yaxis(
        "2 的指数",
        y_axis=[1, 2, 4, 8, 16, 32, 64, 128, 256],
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .add_yaxis(
        "3 的指数",
        y_axis=[1, 3, 9, 27, 81, 247, 741, 2223, 6669],
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Line-对数轴示例"),
        xaxis_opts=opts.AxisOpts(name="x"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="y",
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    )
    .render("line_yaxis_log.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Line/line_yaxis_log.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_yaxis_log.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_yaxis_log.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Line/line_yaxis_log.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_yaxis_log.md"><button class="mybutton">本页markdown原文档</button></a>