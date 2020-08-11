
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType

c = (
    Liquid()
    .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.RECT)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-rect"))
    .render("liquid_shape_rect.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Liquid/liquid_shape_rect.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_shape_rect.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_shape_rect.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Liquid/liquid_shape_rect.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_shape_rect.md"><button class="mybutton">本页markdown原文档</button></a>