
## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Radar

data = [{"value": [4, -4, 2, 3, 0, 1], "name": "预算分配"}]
c_schema = [
    {"name": "销售", "max": 4, "min": -4},
    {"name": "管理", "max": 4, "min": -4},
    {"name": "技术", "max": 4, "min": -4},
    {"name": "客服", "max": 4, "min": -4},
    {"name": "研发", "max": 4, "min": -4},
    {"name": "市场", "max": 4, "min": -4},
]
c = (
    Radar()
    .set_colors(["#4587E7"])
    .add_schema(
        schema=c_schema,
        shape="circle",
        center=["50%", "50%"],
        radius="80%",
        angleaxis_opts=opts.AngleAxisOpts(
            min_=0,
            max_=360,
            is_clockwise=False,
            interval=5,
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=False),
        ),
        radiusaxis_opts=opts.RadiusAxisOpts(
            min_=-4,
            max_=4,
            interval=2,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        polar_opts=opts.PolarOpts(),
        splitarea_opt=opts.SplitAreaOpts(is_show=False),
        splitline_opt=opts.SplitLineOpts(is_show=False),
    )
    .add(
        series_name="预算",
        data=data,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    .render("radar_angle_radius_axis.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Radar/radar_angle_radius_axis.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Radar/radar_angle_radius_axis.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Radar/radar_angle_radius_axis.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Radar/radar_angle_radius_axis.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Radar/radar_angle_radius_axis.md"><button class="mybutton">本页markdown原文档</button></a>