
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Grid, Line, Scatter
from pyecharts.faker import Faker

scatter = (
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Scatter"),
        legend_opts=opts.LegendOpts(pos_left="20%"),
    )
)
line = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Line", pos_right="5%"),
        legend_opts=opts.LegendOpts(pos_right="20%"),
    )
)

grid = (
    Grid()
    .add(scatter, grid_opts=opts.GridOpts(pos_left="55%"))
    .add(line, grid_opts=opts.GridOpts(pos_right="55%"))
    .render("grid_horizontal.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Grid/grid_horizontal.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Grid/grid_horizontal.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Grid/grid_horizontal.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Grid/grid_horizontal.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Grid/grid_horizontal.md"><button class="mybutton">本页markdown原文档</button></a>