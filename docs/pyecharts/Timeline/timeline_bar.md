
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker

x = Faker.choose()
tl = Timeline()
for i in range(2015, 2020):
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
    )
    tl.add(bar, "{}年".format(i))
tl.render("timeline_bar.html")
```

<iframe width="100%" height="800px" src="/pyecharts/Timeline/timeline_bar.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bar.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bar.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Timeline/timeline_bar.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bar.md"><button class="mybutton">本页markdown原文档</button></a>