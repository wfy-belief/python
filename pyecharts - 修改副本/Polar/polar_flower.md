
## pyecharts 代码 / 效果

```python
import math

from pyecharts import options as opts
from pyecharts.charts import Polar

data = []
for i in range(361):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])
c = (
    Polar()
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(start_angle=0, min_=0))
    .add("flower", data, label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Flower"))
    .render("polar_flower.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Polar/polar_flower.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_flower.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_flower.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Polar/polar_flower.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_flower.md"><button class="mybutton">本页markdown原文档</button></a>