from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add("", [("完成率", 66.6)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
    .render("gauge_base.html")
)
