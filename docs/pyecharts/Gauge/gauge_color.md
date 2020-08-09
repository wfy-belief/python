
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add(
        "业务指标",
        [("完成率", 55.5)],
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
            )
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Gauge-不同颜色"),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .render("gauge_color.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Gauge/gauge_color.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_color.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_color.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Gauge/gauge_color.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_color.md"><button class="mybutton">本页markdown原文档</button></a>