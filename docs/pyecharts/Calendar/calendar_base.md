
## pyecharts 代码 / 效果

```python
import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar


begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

c = (
    Calendar()
    .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000,
            min_=500,
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="100px",
        ),
    )
    .render("calendar_base.html")
)

```

<iframe width="100%" height="800px" src="/pyecharts/Calendar/calendar_base.html"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Calendar/calendar_base.py"><button class="mybutton">pyecharts代码下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Calendar/calendar_base.html"><button class="mybutton">HTML源代码</button></a><a href="https://python.wfyblog.cn/pyecharts/Calendar/calendar_base.html"><button class="mybutton">独立图形演示界面</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/pyecharts/Calendar/calendar_base.md"><button class="mybutton">本页markdown原文档</button></a>