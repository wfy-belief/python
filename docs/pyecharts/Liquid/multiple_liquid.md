
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode

l1 = (
    Liquid()
    .add("lq", [0.6, 0.7], center=["60%", "50%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="多个 Liquid 显示"))
)

l2 = Liquid().add(
    "lq",
    [0.3254],
    center=["25%", "50%"],
    label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),
)

grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
grid.render("multiple_liquid.html")
```

<iframe width="100%" height="800px" src="/pyecharts/Liquid/multiple_liquid.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/multiple_liquid.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/multiple_liquid.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Liquid/multiple_liquid.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/multiple_liquid.md"><button class="mybutton">本页markdown原文档</button></a>