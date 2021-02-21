
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

try:
    register_url("https://echarts-maps.github.io/echarts-china-counties-js/")
except Exception:
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context
    register_url("https://echarts-maps.github.io/echarts-china-counties-js/")

geo = (
    Geo()
    .add_schema(maptype="海淀区")
    .set_global_opts(title_opts=opts.TitleOpts(title="海淀区"))
    .render("geo_echart_china_js.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Geo/geo_echart_china_js.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_echart_china_js.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_echart_china_js.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Geo/geo_echart_china_js.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Geo/geo_echart_china_js.md"><button class="mybutton">本页markdown原文档</button></a>