
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), gap="0%")
    .add_yaxis("商家B", Faker.values(), gap="0%")
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-不同系列柱间距离"))
    .render("bar_different_series_gap.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Bar/bar_different_series_gap.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Bar/bar_different_series_gap.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Bar/bar_different_series_gap.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Bar/bar_different_series_gap.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Bar/bar_different_series_gap.md"><button class="mybutton">本页markdown原文档</button></a>