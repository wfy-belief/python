
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode


fn = """
    function(params) {
        if(params.name == '其他')
            return '\n\n\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """


def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center")


c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["剧情", "其他"], [25, 75])],
        center=["20%", "30%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["奇幻", "其他"], [24, 76])],
        center=["55%", "30%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["爱情", "其他"], [14, 86])],
        center=["20%", "70%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["惊悚", "其他"], [11, 89])],
        center=["55%", "70%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-多饼图基本示例"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        ),
    )
    .render("mutiple_pie.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Pie/mutiple_pie.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/mutiple_pie.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/mutiple_pie.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Pie/mutiple_pie.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/mutiple_pie.md"><button class="mybutton">本页markdown原文档</button></a>