<h1 align="center">pyecharts-gallery</h1>

## 前言

- **<font color=#3b9a9c>2021.02.21:版本迭代至1.9.1，若干bug，欢迎指出</font>**
  
- **<font color=#3b9a9c>2020.12.16:部分代码出现问题，版本更新迭代，将会在假期进行逐步更新修复。</font>**
  
  ```python
  from pyecharts.globals import CurrentConfig
  
  CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
  ```
  
- **<font color=#3b9a9c>2020.08.15:全部内容重新适配完毕，耗时十五天。如有bug或者不足之处，将会更新修复。</font>**

- **<font color=#3b9a9c>2020.08.13：该版本是在 `pyecharts 1.8.1`运行，所以1.7.1版本内容做了适配。区别是 Bar y 的参数更改为 `y_axis`(/pyecharts/CDN)</font>**

- **<font color=#3b9a9c>2020.08.10：增加[CDN说明页](/pyecharts/CDN)</font>**

- **<font color=#3b9a9c>2020.08.10：对于默认 `echarts.min.js` 加载缓慢问题，可以由如下方案</font>**

  ```python
  from pyecharts.globals import CurrentConfig
  
  CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/npm/echarts@latest/dist/"
  ```

  

- **<font color=#3b9a9c>自2020.08.08起，所有独立页面增加 `favicon`</font>**

- **<font color=#3b9a9c>自2020.08.08起，因为原可视化网页太大导致加载速度缓慢，将对部分网页 `size >= 50KB` 的网页执行代码压缩，此部分网页在线查看源代码，如遇结构不明显，代码臃肿，请自行 `copy` or `download` 进行格式化查看. 压缩比例为 `1/10` ，单个可视化网页加载速度提升 `10` 倍</font>**

- 所有脚本采用 `jsdelivr` 加速，加载速度提升由原来 `200+ms` 降低至 `20+ms`

- **<font color=#3b9a9c>2020.08.07晚，格式化/美化HTML代码源码，本次不采用HTML压缩，原因是对加载速度影响不大.</font>**

- **<font color=#3b9a9c>2020.08.07晚，修复`echarts.min.js`没有使用CDN加速的bug，`echarts.min.js`加载速度由`1.6s`降低至`70ms`.</font>**

- **<font color=#3b9a9c>2020.08.07晚，防止他人私自调用/滥用加载此网站iframe对象（可视化组件），如果非法调用，重定向到本网站对应地址.</font>**

- **<font color=#3b9a9c>2020.08.07起，使用[CDN](https://cdn.jsdelivr.net/)提供文档预览和下载，优化速度.</font>**

- **<font color=red>基于官方说明和文档进行二次开发和重新部署，并进行维护和修复错误，同时记录自己使用时候的思考，如有不足之处请见谅.</font>**

## 项目简介

* **项目基于 pyecharts `1.9.1` 版本进行展示**
* 百度官方 Echarts [官方实例](https://www.echartsjs.com/examples/zh/)

## 项目须知

* 项目代码结构按照 pyecharts 支持的组件按大写字母顺序进行模块划分
* 代码内有根据 `1.7.1` 版本的 pyecharts 所生成的可视化数据视图和官方的进行对比, 有列出能实现的功能以及未实现的功能
* 以下图例多数会基于 Echarts 的官方实例，不过也有部分会基于 Echarts 的社区 Gallery 实现
