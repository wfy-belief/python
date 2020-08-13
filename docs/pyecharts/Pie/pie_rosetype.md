
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker


v = Faker.choose()
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(v, Faker.values())],
        radius=["30%", "75%"],
        center=["25%", "50%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add(
        "",
        [list(z) for z in zip(v, Faker.values())],
        radius=["30%", "75%"],
        center=["75%", "50%"],
        rosetype="area",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
    .render("pie_rosetype.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Pie/pie_rosetype.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/pie_rosetype.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/pie_rosetype.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Pie/pie_rosetype.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/pie_rosetype.md"><button class="mybutton">本页markdown原文档</button></a>