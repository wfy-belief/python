
## pyecharts 代码 / 效果

```python
from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts


image = Image()

img_src = (
    "https://user-images.githubusercontent.com/19553554/"
    "71825144-2d568180-30d6-11ea-8ee0-63c849cfd934.png"
)
image.add(
    src=img_src,
    style_opts={"width": "200px", "height": "200px", "style": "margin-top: 20px"},
)
image.set_global_opts(
    title_opts=ComponentTitleOpts(title="Image-基本示例", subtitle="我是副标题支持换行哦")
)
image.render("image_base.html")

```

<iframe width="100%" height="800px" src="/pyecharts/Image/image_base.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Image/image_base.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Image/image_base.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Image/image_base.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Image/image_base.md"><button class="mybutton">本页markdown原文档</button></a>