
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "商家A",
        Faker.values(),
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
    )
    .add_yaxis(
        "商家B",
        Faker.values(),
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
    .render("line_markpoint.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Line/line_markpoint.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_markpoint.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_markpoint.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Line/line_markpoint.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_markpoint.md"><button class="mybutton">本页markdown原文档</button></a>