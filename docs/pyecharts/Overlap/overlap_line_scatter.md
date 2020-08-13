
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Line, Scatter
from pyecharts.faker import Faker

x = Faker.choose()
line = (
    Line()
    .add_xaxis(x)
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Overlap-line+scatter"))
)
scatter = (
    Scatter()
    .add_xaxis(x)
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
)
line.overlap(scatter)
line.render("overlap_line_scatter.html")

```

<iframe width="100%" height="800px" src="/pyecharts/Overlap/overlap_line_scatter.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Overlap/overlap_line_scatter.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Overlap/overlap_line_scatter.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Overlap/overlap_line_scatter.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Overlap/overlap_line_scatter.md"><button class="mybutton">本页markdown原文档</button></a>