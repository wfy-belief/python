from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Liquid

c = (
    Liquid()
    .add("lq", [0.6, 0.7, 0.8], is_outline_show=False)
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-无边框"))
    .render("liquid_without_outline.html")
)
