from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values(), is_selected=False)
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-默认取消显示某 Series"))
    .render("bar_is_selected.html")
)
