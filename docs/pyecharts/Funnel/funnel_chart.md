
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import pyecharts.options as opts
from pyecharts.charts import Funnel

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=funnel
目前无法实现的功能:
1、暂时无法对漏斗图的长宽等范围操作进行修改
"""
x_data = ["展现", "点击", "访问", "咨询", "订单"]
y_data = [100, 80, 60, 40, 20]

data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

(
    Funnel()
    .add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图", subtitle="纯属虚构"))
    .render("funnel_chart.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Funnel/funnel_chart.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Funnel/funnel_chart.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Funnel/funnel_chart.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Funnel/funnel_chart.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Funnel/funnel_chart.md"><button class="mybutton">本页markdown原文档</button></a>