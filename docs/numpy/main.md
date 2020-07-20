## 待更新

对应的b站视频在这个地方，为了增加网站的浏览速度，所以不再引视频连接，直接b站观看。
引入第一小节P1的视频。
<iframe 
src="//player.bilibili.com/player.html?aid=711473196&bvid=BV1SD4y1m7e8&cid=214650391&page=1&as_wide=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="640" height="430" > </iframe>

## python -> numpy

<b>个人理解：</b><b><font color='#8ac6d1'>python的列表和元组对象呢，说实话写了很多，不能说有多么精通但是熟练掌握还是没有问题的，python的语法是比较简单的，也是能够快速入门的，当然在处理数据方面也是有很大的优势的。列表或者元组来模拟二维数组对象，或者更高维度的数组对象，其实没有问题。注意是模拟，但是我们得到这些高维度的数组，就是为了计算，例如二维数组可以当作矩阵（自定义一些逻辑和方法）来计算。但是python的数组对象没有方法，只有最基本的索引和切片。那就别谈矩阵的转置，乘法等计算了，自己定义起来不说有bug，效率问题和代码的简洁程度肯定是有欠缺的。</font></b>

<b><font color='#8ac6d1'>所以numpy应运而生，在数组和向量化计算方面有独特的优势</font></b>

## array()

使用`numpy.array`方法将`tuple`和`list`, `array`, 或者其他的序列模式的数据转创建为 `ndarray`, 默认创建一个新的 ndarray.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
</pre></div>
</div>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
    <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>
<span class="p">]</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[14]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([[1, 2, 3],
       [4, 5, 6]])</pre>
</div>
</div>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">9</span><span class="p">]</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="n">data</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[15]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([1, 2, 3, 4, 5, 6, 7, 8, 9])</pre>
</div>
</div>
</div>
</div>
</div>
元组不在展示。

## python->range()

函数说明： range(start, stop[, step]) -> range object，根据start与stop指定的范围以及step设定的步长，生成一个序列。
参数含义：start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
       end:技术到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
       scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
函数返回的是一个range object

## arange()

**<font color=red>传参</font>**

numpy.arange(start, stop, step, dtype = None)

在给定间隔内返回均匀间隔的值。

值在半开区间 [开始，停止]内生成（换句话说，包括开始但不包括停止的区间）,**返回的是 ndarray 。**

**<font color=red>参数</font>**

start —— 开始位置，数字，**可选项**，默认起始值为0

stop —— 停止位置，数字

step —— 步长，数字，**可选项**， 默认步长为1，如果指定了step，则还必须给出start。

dtype —— 输出数组的类型。 如果未给出dtype，则从其他输入参数推断数据类型。

**<font color=red>返回值</font>**

arange：ndarray

均匀间隔值的数组。

**注意：对于浮点参数（参数为浮点），结果的长度为ceil（（stop - start）/ step）） 由于浮点溢出，此规则可能导致最后一个元素大于stop。因此要特别注意**

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[21]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">range</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[22]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>range(0, 17)</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">17</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[23]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([ 1,  6, 11, 16])</pre>
</div>
</div>
</div>
</div>
</div>

## genfromtxt()

- genfromtxt函数创建数组表格数据

- genfromtxt主要执行两个循环运算。第一个循环将文件的每一行转换成字符串序列。第二个循环将每个字符串序列转换为相应的数据类型。

- genfromtxt能够考虑缺失的数据,但其他更快和更简单的函数像loadtxt不能考虑缺失值。

- 使用前需导入相应模块

- 详见 [文档](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)

  常用参数

| 参数      | 解释                   |
| --------- | ---------------------- |
| file_path | 文件的路径位置         |
| encoding  | 指定编码方式，防止乱码 |
| delimiter | 分隔符号，用来分隔内容 |
| dtype     | 指定数据类型 int/float |

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">genfromtxt</span><span class="p">(</span><span class="s2">"./data.csv"</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s1">'.'</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
<span class="n">data</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[42]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10]])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">float</span><span class="p">)</span>
<span class="n">data</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[43]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12.,
       13., 14., 15., 16., 17., 18., 19.])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">20</span><span class="p">,)</span>
<span class="n">data</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[46]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])</pre>
</div>
</div>
</div>
</div>
</div>

## reshape()

*reshape*函数定义如下：

```python
numpy.reshape(a, newshape, order='C')
```

前两个参数很好理解，分别指定了需要改变的张量及新的形状。第三个参数指定改变形状过程中的检索及放置元素的顺序。NumPy的文档中对第三个参数解释如下：

> order : {‘C’, ‘F’, ‘A’}, optional
>
> Read the elements of a using this index order, and place the elements into the reshaped array using this index order. ‘C’ means to read / write the elements using C-like index order, with the last axis index changing fastest, back to the first axis index changing slowest. ‘F’ means to read / write the elements using Fortran-like index order, with the first index changing fastest, and the last index changing slowest. Note that the ‘C’ and ‘F’ options take no account of the memory layout of the underlying array, and only refer to the order of indexing. ‘A’ means to read / write the elements in Fortran-like index order if a is Fortran contiguous in memory, C-like order otherwise.

其中，'A'表示自动选择顺序，所以顺序其实只有两种：'C'和'F'。

- C顺序：指类似C语言的多维数组存储顺序，先遍历数组高维的索引；
- F顺序：指类似Fortran语言的多维数组存储顺序，先遍历数组低维的索引；

具体解释请看配套视频或文档

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">20</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[48]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[48]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[49]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[51]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[51]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[52]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">ndim</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[52]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>1</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[53]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span><span class="o">.</span><span class="n">ndim</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[53]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>2</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[54]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt"></div>
<div class="output_subarea output_text output_error">
<pre><span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">ValueError</span>                                Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-54-ebf5768d41c7&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 1</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>arr<span class="ansi-yellow-intense-fg ansi-bold">.</span>reshape<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-cyan-intense-fg ansi-bold">5</span><span class="ansi-yellow-intense-fg ansi-bold">,</span><span class="ansi-cyan-intense-fg ansi-bold">6</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-red-intense-fg ansi-bold">ValueError</span>: cannot reshape array of size 20 into shape (5,6)</pre>
</div>
</div>
</div>
</div>
</div>

## resize()

如果新数组比原数组大，则将会copy原数组中的值对新数组进行填充，并且是对原数据的改动，其余同reshape（）。

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[55]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[55]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[56]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[57]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[57]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[60]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">,</span><span class="n">refcheck</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">arr</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[60]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0]])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[61]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">6</span><span class="p">,</span><span class="n">refcheck</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">arr</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[61]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[62]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">50</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">10</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[62]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]])</pre>
</div>
</div>
</div>
</div>
</div>