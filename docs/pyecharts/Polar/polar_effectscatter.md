
## pyecharts 代码 / 效果

```python
import random

from pyecharts import options as opts
from pyecharts.charts import Polar


data = [(i, random.randint(1, 100)) for i in range(10)]
c = (
    Polar()
    .add(
        "",
        data,
        type_="effectScatter",
        effect_opts=opts.EffectOpts(scale=10, period=5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-EffectScatter"))
    .render("polar_effectscatter.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Polar/polar_effectscatter.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_effectscatter.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_effectscatter.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Polar/polar_effectscatter.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_effectscatter.md"><button class="mybutton">本页markdown原文档</button></a>