
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker

c = (
    Geo()
    .add_schema(maptype="china")
    .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True),
        title_opts=opts.TitleOpts(title="Geo-VisualMap（分段型）"),
    )
    .render("geo_visualmap_piecewise.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Geo/geo_visualmap_piecewise.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_visualmap_piecewise.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_visualmap_piecewise.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Geo/geo_visualmap_piecewise.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_visualmap_piecewise.md"><button class="mybutton">本页markdown原文档</button></a>