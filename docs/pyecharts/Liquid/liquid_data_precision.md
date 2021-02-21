
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.commons.utils import JsCode

c = (
    Liquid()
    .add(
        "lq",
        [0.3254],
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
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-数据精度"))
    .render("liquid_data_precision.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Liquid/liquid_data_precision.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_data_precision.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_data_precision.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Liquid/liquid_data_precision.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_data_precision.md"><button class="mybutton">本页markdown原文档</button></a>