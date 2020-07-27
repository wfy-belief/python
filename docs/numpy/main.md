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
## 生成零矩阵和单位矩阵

- ones可以创造一个多维度单位矩阵/数组
- zero可以创建零矩阵
- empty则能够创建一个没有初始化的数组
- 创建高维数组，需要通过shape传递一个元组
- np.empty方法来生成一个全0的数组，并不安全，有时候返回没有初始化的垃圾值


```python
import numpy as np
```


```python
np.zeros(10)
```




```python
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```




```python
np.zeros(10).reshape(2,5)
```




```python
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
```




```python
np.empty((2,5,3))
```




```python
array([[[1.77124747e-316, 0.00000000e+000, 0.00000000e+000],
        [0.00000000e+000, 6.90582310e-310, 5.02034658e+175],
        [9.51516005e-043, 2.61253902e-057, 1.14306101e-071],
        [3.54207126e-033, 1.47763641e+248, 1.16096346e-028],
        [7.69165785e+218, 1.35617292e+248, 1.34501351e+161]],

       [[1.23207079e+165, 4.09055525e-037, 9.96917173e-047],
        [4.30514845e-096, 6.32299154e+233, 3.65588282e+233],
        [1.74569531e+238, 1.11763132e+261, 1.16318408e-028],
        [2.24729310e+174, 1.56605686e-076, 8.15067981e-043],
        [2.26436558e-076, 9.51515319e-043, 5.81186266e+294]]])
```




```python
np.zeros((2,3,2))
```




```python
array([[[0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.]]])
```




```python
np.empty((2,3,2))
```




```python
array([[[0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.]]])
```




```python
np.ones((4,5), dtype='int')
```




    array([[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]])



## 数据类型

| 类型                             | 类型代码   | 描述                                                         |
| -------------------------------- | ---------- | ------------------------------------------------------------ |
| int8,uint8                       | i1,u1      | 有符号和无符号的8数位整数                                    |
| int16,uint16                     | i2,u2      | 有符号和无符号的16数位整数                                   |
| int32,uint32                     | i4,u4      | 有符号和无符号的32数位整数                                   |
| int64,uint64                     | i8,u8      | 有符号和无符号的64数位整数                                   |
| float16                          | f2         | 半精度浮点数                                                 |
| float32                          | f4或f      | 标准单精度浮点数；兼顾C语言和float                           |
| float64                          | f8或d      | 标准双精度浮点数；兼容C语言和double和Python float            |
| float128                         | f16或g     | 拓展精度浮点数                                               |
| complex64,complex128,complex256, | c8,c16,c32 | 分别基于32位、64位、128位浮点数的复数                        |
| bool                             | ?          | 布尔值，存储True或False                                      |
| object                           | O          | Python的object类型                                           |
| string_                          | S          | 修正的ascii字符类型；例如生成一个长度为10的字符串类型，使用‘S10’ |
| unicode_                         | U          | 修正带unicode类型，生成一个长度为10的unicode类型，使用‘U10’  |



```python
arr = np.arange(20).reshape(4,5)
```


```python
arr
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])




```python
arr.dtype
```




    dtype('int64')




```python
arr1 = np.arange(20,40,dtype='float').reshape(4,5)
```


```python
arr1
```




    array([[20., 21., 22., 23., 24.],
           [25., 26., 27., 28., 29.],
           [30., 31., 32., 33., 34.],
           [35., 36., 37., 38., 39.]])




```python
arr1.dtype
```




    dtype('float64')



## 数据转换


```python
# astype 
arr = np.arange(10)
```


```python
arr
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
arr.dtype
```




    dtype('int64')




```python
arr.astype('float')
```




    array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])




```python
arr.dtype
```




    dtype('int64')



## 数组运算


```python
arr1 = np.arange(20).reshape(4,5)
arr2 = np.arange(20).reshape(4,5)
```


```python
arr1
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])




```python
arr2
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])




```python
arr1 * arr1
```




    array([[  0,   1,   4,   9,  16],
           [ 25,  36,  49,  64,  81],
           [100, 121, 144, 169, 196],
           [225, 256, 289, 324, 361]])




```python
arr1  - arr2
```




    array([[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]])




```python
arr1 + arr2
```




    array([[ 0,  2,  4,  6,  8],
           [10, 12, 14, 16, 18],
           [20, 22, 24, 26, 28],
           [30, 32, 34, 36, 38]])




```python
1 / arr1
```

    /home/wfy-belief/.local/lib/python3.7/site-packages/ipykernel_launcher.py:1: RuntimeWarning: divide by zero encountered in true_divide
      """Entry point for launching an IPython kernel.





    array([[       inf, 1.        , 0.5       , 0.33333333, 0.25      ],
           [0.2       , 0.16666667, 0.14285714, 0.125     , 0.11111111],
           [0.1       , 0.09090909, 0.08333333, 0.07692308, 0.07142857],
           [0.06666667, 0.0625    , 0.05882353, 0.05555556, 0.05263158]])




```python
arr = np.arange(1,21).reshape(4,5)
```


```python
1/ arr
```




    array([[1.        , 0.5       , 0.33333333, 0.25      , 0.2       ],
           [0.16666667, 0.14285714, 0.125     , 0.11111111, 0.1       ],
           [0.09090909, 0.08333333, 0.07692308, 0.07142857, 0.06666667],
           [0.0625    , 0.05882353, 0.05555556, 0.05263158, 0.05      ]])




```python
arr1 ** 0.5
```




    array([[0.        , 1.        , 1.41421356, 1.73205081, 2.        ],
           [2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ],
           [3.16227766, 3.31662479, 3.46410162, 3.60555128, 3.74165739],
           [3.87298335, 4.        , 4.12310563, 4.24264069, 4.35889894]])




```python
arr1 > arr2
```




    array([[False, False, False, False, False],
           [False, False, False, False, False],
           [False, False, False, False, False],
           [False, False, False, False, False]])



## 基础索引和切片


```python
arr[1:3]
```




    array([[ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15]])




```python
arr
```




    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]])




```python
arr[[0,2]]
```




    array([[ 1,  2,  3,  4,  5],
           [11, 12, 13, 14, 15]])




```python
arr[(1,4)]
```




    10




```python
arr[(0,2),(1,4)]
```




    array([ 2, 15])




```python
arr[(3,1,0),(2,0,0)]
```




    array([18,  6,  1])




```python
arr[[1,2,3],[1,2,3]]
```




    array([ 7, 13, 19])




```python
arr[0:, 1:]
```




    array([[ 2,  3,  4,  5],
           [ 7,  8,  9, 10],
           [12, 13, 14, 15],
           [17, 18, 19, 20]])




```python
arr[0:, 2:]
```




    array([[ 3,  4,  5],
           [ 8,  9, 10],
           [13, 14, 15],
           [18, 19, 20]])




```python
arr[0:, 2:][[0,1,2],[0,1,2]]
```




    array([ 3,  9, 15])




```python
arr
```




    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]])




```python
arr[:,[1,2]]
```




    array([[ 2,  3],
           [ 7,  8],
           [12, 13],
           [17, 18]])

