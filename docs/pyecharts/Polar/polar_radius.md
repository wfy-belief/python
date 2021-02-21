
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker

c = (
    Polar()
    .add_schema(
        radiusaxis_opts=opts.RadiusAxisOpts(data=Faker.week, type_="category"),
        angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True, max_=10),
    )
    .add("A", [1, 2, 3, 4, 3, 5, 1], type_="bar")
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-RadiusAxis"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .render("polar_radius.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Polar/polar_radius.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_radius.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_radius.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Polar/polar_radius.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Polar/polar_radius.md"><button class="mybutton">本页markdown原文档</button></a>