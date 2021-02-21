
## pyecharts 代码 / 效果

```python
import math

from pyecharts import options as opts
from pyecharts.charts import Line3D
from pyecharts.faker import Faker

data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    data.append([x, y, z])
c = (
    Line3D()
    .add(
        "",
        data,
        xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="value"),
        grid3d_opts=opts.Grid3DOpts(
            width=100, depth=100, rotate_speed=150, is_rotate=True
        ),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            max_=30, min_=0, range_color=Faker.visual_color
        ),
        title_opts=opts.TitleOpts(title="Line3D-旋转的弹簧"),
    )
    .render("line3d_autorotate.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Line3D/line3d_autorotate.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line3D/line3d_autorotate.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line3D/line3d_autorotate.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Line3D/line3d_autorotate.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line3D/line3d_autorotate.md"><button class="mybutton">本页markdown原文档</button></a>