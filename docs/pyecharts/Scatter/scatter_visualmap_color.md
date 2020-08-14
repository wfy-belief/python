
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.faker import Faker

c = (
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-VisualMap(Color)"),
        visualmap_opts=opts.VisualMapOpts(max_=150),
    )
    .render("scatter_visualmap_color.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Scatter/scatter_visualmap_color.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Scatter/scatter_visualmap_color.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Scatter/scatter_visualmap_color.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Scatter/scatter_visualmap_color.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Scatter/scatter_visualmap_color.md"><button class="mybutton">本页markdown原文档</button></a>