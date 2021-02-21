
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add(
        "业务指标",
        [("完成率", 55.5)],
        split_number=5,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
            )
        ),
        detail_label_opts=opts.LabelOpts(formatter="{value}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Gauge-分割段数-Label"),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .render("gauge_splitnum_label.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Gauge/gauge_splitnum_label.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_splitnum_label.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_splitnum_label.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Gauge/gauge_splitnum_label.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_splitnum_label.md"><button class="mybutton">本页markdown原文档</button></a>