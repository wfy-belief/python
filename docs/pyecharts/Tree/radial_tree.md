
## pyecharts 代码 / 效果

```python
import asyncio
from aiohttp import TCPConnector, ClientSession

import pyecharts.options as opts
from pyecharts.charts import Tree

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=tree-radial

目前无法实现的功能:

1、
"""


async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()


# 获取官方的数据
data = asyncio.run(
    get_json_data(url="https://echarts.apache.org/examples/data/asset/data/flare.json")
)

(
    Tree(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add(
        series_name="",
        data=[data],
        pos_top="18%",
        pos_bottom="14%",
        layout="radial",
        symbol="emptyCircle",
        symbol_size=7,
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove")
    )
    .render("radial_tree.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Tree/radial_tree.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Tree/radial_tree.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Tree/radial_tree.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Tree/radial_tree.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Tree/radial_tree.md"><button class="mybutton">本页markdown原文档</button></a>