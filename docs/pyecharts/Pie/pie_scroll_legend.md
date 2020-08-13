
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add(
        "",
        [
            list(z)
            for z in zip(
                Faker.choose() + Faker.choose() + Faker.choose(),
                Faker.values() + Faker.values() + Faker.values(),
            )
        ],
        center=["40%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-Legend 滚动"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_scroll_legend.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Pie/pie_scroll_legend.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/pie_scroll_legend.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/pie_scroll_legend.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Pie/pie_scroll_legend.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/pie_scroll_legend.md"><button class="mybutton">本页markdown原文档</button></a>