
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar, Geo, Grid
from pyecharts.faker import Faker

bar = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="20%"))
)
geo = (
    Geo()
    .add_schema(maptype="china")
    .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Grid-Geo-Bar"),
    )
)

grid = (
    Grid()
    .add(bar, grid_opts=opts.GridOpts(pos_top="50%", pos_right="75%"))
    .add(geo, grid_opts=opts.GridOpts(pos_left="60%"))
    .render("grid_geo_bar.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Grid/grid_geo_bar.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Grid/grid_geo_bar.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Grid/grid_geo_bar.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Grid/grid_geo_bar.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Grid/grid_geo_bar.md"><button class="mybutton">本页markdown原文档</button></a>