
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.faker import Faker

attr = Faker.choose()
tl = Timeline()
for i in range(2015, 2020):
    pie = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
    )
    tl.add(pie, "{}年".format(i))
tl.render("timeline_pie.html")
```

<iframe width="100%" height="800px" src="/pyecharts/Timeline/timeline_pie.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_pie.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_pie.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Timeline/timeline_pie.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_pie.md"><button class="mybutton">本页markdown原文档</button></a>