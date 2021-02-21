
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import json

from pyecharts import options as opts
from pyecharts.charts import TreeMap


with open("treemap.json", "r", encoding="utf-8") as f:
    data = json.load(f)
c = (
    TreeMap()
    .add(
        series_name="演示数据",
        data=data,
        levels=[
            opts.TreeMapLevelsOpts(
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color="#555", border_width=4, gap_width=4
                )
            ),
            opts.TreeMapLevelsOpts(
                color_saturation=[0.3, 0.6],
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color_saturation=0.7, gap_width=2, border_width=2
                ),
            ),
            opts.TreeMapLevelsOpts(
                color_saturation=[0.3, 0.5],
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color_saturation=0.6, gap_width=1
                ),
            ),
            opts.TreeMapLevelsOpts(color_saturation=[0.3, 0.5]),
        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-Levels-配置"))
    .render("treemap_levels.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Treemap/treemap_levels.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Treemap/treemap_levels.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Treemap/treemap_levels.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Treemap/treemap_levels.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Treemap/treemap_levels.md"><button class="mybutton">本页markdown原文档</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Treemap/treemap.json"><button class="mybutton">treemap.json</button></a>