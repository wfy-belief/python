## 匹配规则

### `signal char`

匹配某个字符串：

```python
text = 'hello'
ret = re.match('he',text)
print(ret.group())
>> he
```
以上便可以在hello中，匹配出he。

### `'.'`

点（.）匹配任意的字符：

```python
text = "ab"
ret = re.match('.',text)
print(ret.group())

>> a
```
但是点（.）不能匹配不到换行符。示例代码如下：
```python
text = "ab"
ret = re.match('.',text)
print(ret.group())
>> AttributeError: 'NoneType' object has no attribute 'group'
```
### `\d`

\d匹配任意的数字：

```python
text = "123"
ret = re.match('\d',text)
print(ret.group())
>> 1
```
### `\D`

\D匹配任意的非数字：

```python
text = "a"
ret = re.match('\D',text)
print(ret.group())
>> a
```
而如果text是等于一个数字，那么就匹配不成功了。示例代码如下：
```python
text = "1"
ret = re.match('\D',text)
print(ret.group())
>> AttributeError: 'NoneType' object has no attribute 'group'
```
### `\s`

\s匹配的是空白字符（包括：\n，\t，\r和空格）：

```python
text = "\t"
ret = re.match('\s',text)
print(ret.group())
>> 空白
```
### `\w`

\w匹配的是a-z和A-Z以及数字和下划线：

```python
text = "_"
ret = re.match('\w',text)
print(ret.group())
>> _
```
而如果要匹配一个其他的字符，那么就匹配不到。示例代码如下：
```python
text = "+"
ret = re.match('\w',text)
print(ret.group())
>> AttributeError: 'NoneType' object has no attribute
```
### `\W`

\W匹配的是和\w相反的：

```python
text = "+"
ret = re.match('\W',text)
print(ret.group())
>> +
```
而如果你的text是一个下划线或者英文字符，那么就匹配不到了。示例代码如下：
```python
text = "_"
ret = re.match('\W',text)
print(ret.group())
>> AttributeError: 'NoneType' object has no attribute
```
### `'[]'`

[]组合的方式，只要满足中括号中的某一项都算匹配成功：

```python
text = "0731-88888888"
ret = re.match('[\d\-]+',text)
print(ret.group())
>> 0731-88888888
```
之前讲到的几种匹配规则，其实可以使用中括号的形式来进行替代：

- `\d：[0-9]`

- `\D：0-9`

- `\w：[0-9a-zA-Z_]`

- `\W：[^0-9a-zA-Z_]`

## 练习预览
<p>本次练习使用jupyter notebook，对应预览和在线交互如下。</p>
<a href="https://nbviewer.jupyter.org/github/wfy-belief/python/blob/master/docs/re/single-character.ipynb"><button class="mybutton">jupyter notebook在线预览</button></a><a href="https://mybinder.org/v2/gh/wfy-belief/python/master?filepath=docs/re/single-character.ipynb"><button class="mybutton">jupyter notebook在线交互（加载时间长）</button></a>

## jupyter notebook 在线嵌入

由 `nbviewer.jupyter.org` 加载，速度较慢，且部分 `js` 无法加载，请见谅。


<iframe src="https://nbviewer.jupyter.org/github/wfy-belief/python/blob/master/docs/re/single-character.ipynb" width="100%" height="500px" scrolling="yes"></iframe>

## 附文档及代码

<a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/re/single-character.ipynb"><button class="mybutton">jupyter notebook文档下载</button></a><a href="https://cdn.jsdelivr.net/gh/wfy-belief/python/docs/re/single-character.md"><button class="mybutton">本页markdown原文档</button></a>

