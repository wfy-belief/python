
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import BMap, Timeline
from pyecharts.faker import Faker

tl = Timeline()
tl.add_schema(pos_left="50%", pos_right="10px", pos_bottom="15px")
for i in range(2015, 2020):
    bmap = (
        BMap()
        .add_schema(baidu_ak="53oVIOgmSIejwV7EfphPgTynOZbIiVYu", center=[120.13066322374, 30.240018034923])
        .add(
            "bmap",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_="heatmap",
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Timeline-BMap-热力图-{}年".format(i)),
            visualmap_opts=opts.VisualMapOpts(pos_bottom="center", pos_right="10px"),
            tooltip_opts=opts.TooltipOpts(formatter=None),
        )
    )
    tl.add(bmap, "{}年".format(i))
tl.render("timeline_bmap.html")

```

<iframe width="100%" height="800px" src="/pyecharts/Timeline/timeline_bmap.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bmap.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bmap.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Timeline/timeline_bmap.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bmap.md"><button class="mybutton">本页markdown原文档</button></a>

