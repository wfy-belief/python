
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import math
import pyecharts.options as opts
from pyecharts.charts import Polar

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=line-polar2
目前无法实现的功能:
1、赞无
"""

data = []

for i in range(0, 360 + 1):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])

(
    Polar()
    .add(
        series_name="line",
        data=data,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=0,
    )
    .add_schema(
        angleaxis_opts=opts.AngleAxisOpts(
            start_angle=0, type_="value", is_clockwise=True
        ),
        radiusaxis_opts=opts.RadiusAxisOpts(min_=0),
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        title_opts=opts.TitleOpts(title="极坐标双数值轴"),
    )
    .render("two_value_axes_in_polar_2.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Polar/two_value_axes_in_polar_2.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/two_value_axes_in_polar_2.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/two_value_axes_in_polar_2.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Polar/two_value_axes_in_polar_2.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/two_value_axes_in_polar_2.md"><button class="mybutton">本页markdown原文档</button></a>