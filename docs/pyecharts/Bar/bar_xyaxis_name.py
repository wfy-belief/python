from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-XY 轴名称"),
        yaxis_opts=opts.AxisOpts(name="我是 Y 轴"),
        xaxis_opts=opts.AxisOpts(name="我是 X 轴"),
    )
    .render("bar_xyaxis_name.html")
)
