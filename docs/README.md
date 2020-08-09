## 版本更新说明

优化了index的大小，删除繁琐代码，但保留原来代码文件。

- 合并 `js` `cdn` 加载，避免多次请求。

  ```
  <script src="//cdn.jsdelivr.net/npm/docsify@latest/lib/docsify.min.js">//@4.11.4</script>
  <script src="//cdn.jsdelivr.net/npm/docsify@latest/lib/plugins/search.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/docsify-copy-code@latest/dist/docsify-copy-code.min.js">//@2.1.0</script>
  <script src="//cdn.jsdelivr.net/npm/docsify@latest/lib/plugins/zoom-image.min.js">//@4.11.4</script>
  <script src="//cdn.jsdelivr.net/npm/prismjs@latest/components/prism-python.min.js">//@1.21.0</script>
  ```

  ```
  <script src="//cdn.jsdelivr.net/combine/npm/docsify@latest/lib/docsify.min.js,npm/docsify@latest/lib/plugins/search.min.js,npm/docsify-copy-code@latest/dist/docsify-copy-code.min.js,npm/docsify@latest/lib/plugins/zoom-image.min.js,npm/prismjs@latest/components/prism-python.min.js">//@4.11.4</script>
  ```

  

- 更改字体加载缓慢的[问题](https://web.dev/font-display/)提升性能，即字体链接后面添加 `&display=swap`

- 所有脚本采用 `jsdelivr` 加速，加载速度提升由原来 `200+ms` 降低至 `20+ms`

- index.html 从 12KB 减少到  3KB

- ~~修改样式 主页面大小为 `80%`~~存在若干bug,修改为指定值`1000px`

- 了解新的可视化方法

- 把加载的脚本隐藏到 `div[@id='app']`标签内

## 基于docsify可视化使用

引入插件

```
<script src="//cdn.jsdelivr.net/npm/echarts@latest/dist/echarts.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/docsify-echarts-plugin/lib/index.min.js"></script>
```

然后md文档生成代码块

```
` ` `chart

` ` `
```

里面传递的参数为json格式，可以在echarts官网参考示例，然后复制代码，到浏览器console命令行执行 `JSON.stringify(option)` 仅供参考。

## 通用

[寻找可视化插件](https://docsify.js.org/#/awesome?id=plugins) 执行查找 `echarts` 即可

例如示例 [gallery](https://gallery.pyecharts.org/#/Grid/grid_multi_yaxis)

md文档添加如下代码即可

```
<iframe width="900px" height="500px" src="./grid_multi_yaxis.html"></iframe>
```

<iframe width="100%" height="520px" src="./grid_multi_yaxis.html"></iframe>

## 首页

E-mail: 1335680234@qq.com

[Github](<https://github.com/wfy-belief>)

## python
python学习的文档，构建于docsify，地址为wfyblog.cn/python

1. 初始化仓库

   ```
   git  init
   ```

2. 于远程仓库建立连接

   ```
   git remote add origin https://github.com/wfy-belief/python.git
   ```

3. 拉取远程主分支

   ```
   git pull origin master
   ```

4. 推送到远程分支

   ```
   git push -u origin master
   ```

这样就与远程仓库建立了连接就可以用Git提交代码了

```
git add .     //将代码放到缓存区
git commit -m""   //提交到本地仓库
git push          //推送到远程
```