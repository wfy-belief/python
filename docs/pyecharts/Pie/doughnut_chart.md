
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import pyecharts.options as opts
from pyecharts.charts import Pie

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=pie-doughnut
目前无法实现的功能:
1、饼状图中间的图例名称暂时无法显示
"""

x_data = ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"]
y_data = [335, 310, 234, 135, 1548]

(
    Pie()
    .add(
        series_name="访问来源",
        data_pair=[list(z) for z in zip(x_data, y_data)],
        radius=["50%", "70%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        # label_opts=opts.LabelOpts(formatter="{b}: {c}")
    )
    .render("doughnut_chart.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Pie/doughnut_chart.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/doughnut_chart.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/doughnut_chart.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Pie/doughnut_chart.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Pie/doughnut_chart.md"><button class="mybutton">本页markdown原文档</button></a>