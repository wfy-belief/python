from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), is_smooth=True)
    .add_yaxis("商家B", Faker.values(), is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-smooth"))
    .render("line_smooth.html")
)
