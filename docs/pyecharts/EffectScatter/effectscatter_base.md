
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker

c = (
    EffectScatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
    .render("effectscatter_base.html")
)
```

<iframe width="100%" height="800px" src="/pyecharts/EffectScatter/effectscatter_base.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/EffectScatter/effectscatter_base.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/EffectScatter/effectscatter_base.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/EffectScatter/effectscatter_base.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/EffectScatter/effectscatter_base.md"><button class="mybutton">本页markdown原文档</button></a>