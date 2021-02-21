
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Liquid

c = (
    Liquid()
    .add("lq", [0.6, 0.7])
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))
    .render("liquid_base.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/Liquid/liquid_base.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_base.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_base.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Liquid/liquid_base.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Liquid/liquid_base.md"><button class="mybutton">本页markdown原文档</button></a>