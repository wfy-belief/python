
## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add(
        "",
        [("完成率", 66.6)],
        title_label_opts=opts.LabelOpts(
            font_size=40, color="blue", font_family="Microsoft YaHei"
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-改变轮盘内的字体"))
    .render("gauge_label_title_setting.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Gauge/gauge_label_title_setting.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_label_title_setting.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_label_title_setting.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Gauge/gauge_label_title_setting.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Gauge/gauge_label_title_setting.md"><button class="mybutton">本页markdown原文档</button></a>