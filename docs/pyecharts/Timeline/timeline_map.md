
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
from pyecharts.faker import Faker

tl = Timeline()
for i in range(2015, 2020):
    map0 = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-{}年某些数据".format(i)),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    tl.add(map0, "{}年".format(i))
tl.render("timeline_map.html")
```

<iframe width="100%" height="800px" src="/pyecharts/Timeline/timeline_map.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_map.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_map.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Timeline/timeline_map.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_map.md"><button class="mybutton">本页markdown原文档</button></a>