
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import pyecharts.options as opts
from pyecharts.charts import Candlestick

x_data = ["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27"]
y_data = [[20, 30, 10, 35], [40, 35, 30, 55], [33, 38, 33, 40], [40, 40, 32, 42]]

(
    Candlestick()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(series_name="", y_axis=y_data)
    .set_series_opts()
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(width=1)
            )
        )
    )
    .render("basic_candlestick.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Candlestick/basic_candlestick.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Candlestick/basic_candlestick.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Candlestick/basic_candlestick.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Candlestick/basic_candlestick.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Candlestick/basic_candlestick.md"><button class="mybutton">本页markdown原文档</button></a>