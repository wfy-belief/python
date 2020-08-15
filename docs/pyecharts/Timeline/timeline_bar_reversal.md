
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker

tl = Timeline()
for i in range(2015, 2020):
    bar = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), label_opts=opts.LabelOpts(position="right"))
        .add_yaxis("商家B", Faker.values(), label_opts=opts.LabelOpts(position="right"))
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts("Timeline-Bar-Reversal (时间: {} 年)".format(i))
        )
    )
    tl.add(bar, "{}年".format(i))
tl.render("timeline_bar_reversal.html")

```

<iframe width="100%" height="800px" src="/pyecharts/Timeline/timeline_bar_reversal.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bar_reversal.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bar_reversal.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Timeline/timeline_bar_reversal.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Timeline/timeline_bar_reversal.md"><button class="mybutton">本页markdown原文档</button></a>