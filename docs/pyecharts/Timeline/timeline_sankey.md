
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Sankey, Timeline
from pyecharts.faker import Faker

tl = Timeline()
names = ("商家A", "商家B", "商家C")
nodes = [{"name": name} for name in names]
for i in range(2015, 2020):
    links = [
        {"source": names[0], "target": names[1], "value": Faker.values()[0]},
        {"source": names[1], "target": names[2], "value": Faker.values()[0]},
    ]
    sankey = (
        Sankey()
        .add(
            "sankey",
            nodes,
            links,
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="{}年商店（A, B, C）营业额差".format(i))
        )
    )
    tl.add(sankey, "{}年".format(i))
tl.render("timeline_sankey.html")
```

<iframe width="100%" height="800px" src="/pyecharts/Timeline/timeline_sankey.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_sankey.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_sankey.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Timeline/timeline_sankey.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_sankey.md"><button class="mybutton">本页markdown原文档</button></a>