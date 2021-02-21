
## pyecharts 代码 / 效果

```python
import json

from pyecharts import options as opts
from pyecharts.charts import PictorialBar

location = ["山西", "四川", "西藏", "北京", "上海", "内蒙古", "云南", "黑龙江", "广东", "福建"]
values = [13, 42, 67, 81, 86, 94, 166, 220, 249, 262]


with open("symbol.json", "r", encoding="utf-8") as f:
    symbols = json.load(f)


c = (
    PictorialBar()
    .add_xaxis(location)
    .add_yaxis(
        "",
        values,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=22,
        symbol_repeat="fixed",
        symbol_offset=[0, -5],
        is_symbol_clip=True,
        symbol=symbols["boy"],
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="PictorialBar-自定义 Symbol"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("pictorialbar_custom_symbol.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/PictorialBar/pictorialbar_custom_symbol.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/PictorialBar/pictorialbar_custom_symbol.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/PictorialBar/pictorialbar_custom_symbol.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/PictorialBar/pictorialbar_custom_symbol.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/PictorialBar/pictorialbar_custom_symbol.md"><button class="mybutton">本页markdown原文档</button></a>