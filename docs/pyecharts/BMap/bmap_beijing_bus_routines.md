## 百度API接口说明

此部分如出现问题，请自行注册。

## pyecharts 代码 / 效果

```python
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
import json

from pyecharts.charts import BMap
from pyecharts import options as opts

"""
参考地址: https://gallery.echartsjs.com/editor.html?c=bmap-bus
"""

BAIDU_MAP_AK = "53oVIOgmSIejwV7EfphPgTynOZbIiVYu"

# 读取项目中的 json 文件
with open("busRoutines.json", "r", encoding="utf-8") as f:
    bus_lines = json.load(f)

c = (
    BMap(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add_schema(
        baidu_ak=BAIDU_MAP_AK,
        center=[116.40, 40.04],
        zoom=10,
        is_roam=True,
        map_style={
            "styleJson": [
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": {"color": "#031628"},
                },
                {
                    "featureType": "land",
                    "elementType": "geometry",
                    "stylers": {"color": "#000102"},
                },
                {
                    "featureType": "highway",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry.stroke",
                    "stylers": {"color": "#0b3d51"},
                },
                {
                    "featureType": "local",
                    "elementType": "geometry",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "railway",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "railway",
                    "elementType": "geometry.stroke",
                    "stylers": {"color": "#08304b"},
                },
                {
                    "featureType": "subway",
                    "elementType": "geometry",
                    "stylers": {"lightness": -70},
                },
                {
                    "featureType": "building",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.fill",
                    "stylers": {"color": "#857f7f"},
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.stroke",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "building",
                    "elementType": "geometry",
                    "stylers": {"color": "#022338"},
                },
                {
                    "featureType": "green",
                    "elementType": "geometry",
                    "stylers": {"color": "#062032"},
                },
                {
                    "featureType": "boundary",
                    "elementType": "all",
                    "stylers": {"color": "#465b6c"},
                },
                {
                    "featureType": "manmade",
                    "elementType": "all",
                    "stylers": {"color": "#022338"},
                },
                {
                    "featureType": "label",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
            ]
        },
    )
    .add(
        "",
        type_="lines",
        is_polyline=True,
        data_pair=bus_lines,
        linestyle_opts=opts.LineStyleOpts(opacity=0.2, width=0.5),
        # 如果不是最新版本的话可以注释下面的参数（效果差距不大）
        progressive=200,
        progressive_threshold=500,
    )
    .render("bmap_beijing_bus_routines.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/BMap/bmap_beijing_bus_routines.html"></iframe>


## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/BMap/bmap_beijing_bus_routines.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/BMap/bmap_beijing_bus_routines.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/BMap/bmap_beijing_bus_routines.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/BMap/bmap_beijing_bus_routines.md"><button class="mybutton">本页markdown原文档</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/BMap/busRoutines.json"><button class="mybutton">busRoutines.json</button></a>
