
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Sankey

colors = [
    "#67001f",
    "#b2182b",
    "#d6604d",
    "#f4a582",
    "#fddbc7",
    "#d1e5f0",
    "#92c5de",
    "#4393c3",
    "#2166ac",
    "#053061",
]
nodes = [
    {"name": "a"},
    {"name": "b"},
    {"name": "a1"},
    {"name": "b1"},
    {"name": "c"},
    {"name": "e"},
]
links = [
    {"source": "a", "target": "a1", "value": 5},
    {"source": "e", "target": "b", "value": 3},
    {"source": "a", "target": "b1", "value": 3},
    {"source": "b1", "target": "a1", "value": 1},
    {"source": "b1", "target": "c", "value": 2},
    {"source": "b", "target": "c", "value": 1},
]
c = (
    Sankey()
    .set_colors(colors)
    .add(
        "sankey",
        nodes=nodes,
        links=links,
        pos_bottom="10%",
        focus_node_adjacency="allEdges",
        orient="vertical",
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="top"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Sankey-Vertical"),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
    )
    .render("sankey_vertical.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Sankey/sankey_vertical.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Sankey/sankey_vertical.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Sankey/sankey_vertical.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Sankey/sankey_vertical.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Sankey/sankey_vertical.md"><button class="mybutton">本页markdown原文档</button></a>