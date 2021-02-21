from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import random

from pyecharts import options as opts
from pyecharts.charts import Polar


data = [(i, random.randint(1, 100)) for i in range(10)]
c = (
    Polar()
    .add(
        "",
        data,
        type_="effectScatter",
        effect_opts=opts.EffectOpts(scale=10, period=5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar-EffectScatter"))
    .render("polar_effectscatter.html")
)
