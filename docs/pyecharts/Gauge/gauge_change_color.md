
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import pyecharts.options as opts
from pyecharts.charts import Gauge

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://gallery.echartsjs.com/editor.html?c=xH1vxib94f

目前无法实现的功能:

1、暂无
"""

(
    Gauge()
    .add(series_name="业务指标", data_pair=[["完成率", 55.5]])
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
    )
    .set_series_opts(
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[[0.3, "#67e0e3"], [0.7, "#37a2da"], [1, "#fd666d"]], width=30
            )
        )
    )
    .render("gauge_change_color.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Gauge/gauge_change_color.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_change_color.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_change_color.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Gauge/gauge_change_color.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_change_color.md"><button class="mybutton">本页markdown原文档</button></a>