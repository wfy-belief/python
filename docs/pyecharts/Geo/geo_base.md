
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker

c = (
    Geo()
    .add_schema(maptype="china")
    .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
    )
    .render("geo_base.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Geo/geo_base.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_base.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_base.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Geo/geo_base.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_base.md"><button class="mybutton">本页markdown原文档</button></a>

