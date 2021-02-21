
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import random

from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.faker import Faker


data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
c = (
    Bar3D()
    .add(
        "",
        [[d[1], d[0], d[2]] for d in data],
        xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=20),
        title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
    )
    .render("bar3d_base.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Bar3D/bar3d_base.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Bar3D/bar3d_base.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Bar3D/bar3d_base.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Bar3D/bar3d_base.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Bar3D/bar3d_base.md"><button class="mybutton">本页markdown原文档</button></a>