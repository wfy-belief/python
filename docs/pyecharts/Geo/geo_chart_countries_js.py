from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

try:
    register_url("https://echarts-maps.github.io/echarts-countries-js/")
except Exception:
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context
    register_url("https://echarts-maps.github.io/echarts-countries-js/")

geo = (
    Geo()
    .add_schema(maptype="china")
    .set_global_opts(title_opts=opts.TitleOpts(title="中国"))
    .render("geo_chart_countries_js.html")
)
