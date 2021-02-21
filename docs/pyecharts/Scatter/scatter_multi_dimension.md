
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker

c = (
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "商家A",
        [list(z) for z in zip(Faker.values(), Faker.choose())],
        label_opts=opts.LabelOpts(
            formatter=JsCode(
                "function(params){return params.value[1] +' : '+ params.value[2];}"
            )
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
        tooltip_opts=opts.TooltipOpts(
            formatter=JsCode(
                "function (params) {return params.name + ' : ' + params.value[2];}"
            )
        ),
        visualmap_opts=opts.VisualMapOpts(
            type_="color", max_=150, min_=20, dimension=1
        ),
    )
    .render("scatter_multi_dimension.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Scatter/scatter_multi_dimension.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Scatter/scatter_multi_dimension.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Scatter/scatter_multi_dimension.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Scatter/scatter_multi_dimension.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Scatter/scatter_multi_dimension.md"><button class="mybutton">本页markdown原文档</button></a>