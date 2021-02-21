
## pyecharts 代码 / 效果

```python
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker


c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), is_smooth=True)
    .add_yaxis("商家B", Faker.values(), is_smooth=True)
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Line-面积图（紧贴 Y 轴）"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    )
    .render("line_areastyle_boundary_gap.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Line/line_areastyle_boundary_gap.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_areastyle_boundary_gap.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_areastyle_boundary_gap.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Line/line_areastyle_boundary_gap.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Line/line_areastyle_boundary_gap.md"><button class="mybutton">本页markdown原文档</button></a>