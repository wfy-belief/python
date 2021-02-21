
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import TreeMap

data = [
    {"value": 40, "name": "我是A"},
    {
        "value": 180,
        "name": "我是B",
        "children": [
            {
                "value": 76,
                "name": "我是B.children",
                "children": [
                    {"value": 12, "name": "我是B.children.a"},
                    {"value": 28, "name": "我是B.children.b"},
                    {"value": 20, "name": "我是B.children.c"},
                    {"value": 16, "name": "我是B.children.d"},
                ],
            }
        ],
    },
]

c = (
    TreeMap()
    .add("演示数据", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-基本示例"))
    .render("treemap_base.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Treemap/treemap_base.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Treemap/treemap_base.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Treemap/treemap_base.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Treemap/treemap_base.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Treemap/treemap_base.md"><button class="mybutton">本页markdown原文档</button></a>