
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Graph

nodes_data = [
    opts.GraphNode(name="结点1", symbol_size=10),
    opts.GraphNode(name="结点2", symbol_size=20),
    opts.GraphNode(name="结点3", symbol_size=30),
    opts.GraphNode(name="结点4", symbol_size=40),
    opts.GraphNode(name="结点5", symbol_size=50),
    opts.GraphNode(name="结点6", symbol_size=60),
]
links_data = [
    opts.GraphLink(source="结点1", target="结点2", value=2),
    opts.GraphLink(source="结点2", target="结点3", value=3),
    opts.GraphLink(source="结点3", target="结点4", value=4),
    opts.GraphLink(source="结点4", target="结点5", value=5),
    opts.GraphLink(source="结点5", target="结点6", value=6),
    opts.GraphLink(source="结点6", target="结点1", value=7),
]
c = (
    Graph()
    .add(
        "",
        nodes_data,
        links_data,
        repulsion=4000,
        edge_label=opts.LabelOpts(
            is_show=True, position="middle", formatter="{b} 的数据 {c}"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink-WithEdgeLabel")
    )
    .render("graph_with_edge_options.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Graph/graph_with_edge_options.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Graph/graph_with_edge_options.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Graph/graph_with_edge_options.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Graph/graph_with_edge_options.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Graph/graph_with_edge_options.md"><button class="mybutton">本页markdown原文档</button></a>