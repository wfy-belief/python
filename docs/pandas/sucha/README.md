# Pandas基础命令速查清单

本文翻译整理自[Pandas Cheat Sheet - Python for Data Science](https://www.dataquest.io/blog/pandas-cheat-sheet/),结合K-Lab的工具属性，添加了具体的内容将速查清单里面的代码实践了一遍。

## 速查表内容概要

- [缩写解释 & 库的导入]
- [数据的导入]
- [数据的导出]
- [创建测试对象]
- [数据的查看与检查]
- [数据的选取]
- [数据的清洗]
- [数据的过滤(`filter`),排序(`sort`)和分组(`groupby`)]
- [数据的连接(`join`)与组合(`combine`)]
- [数据的统计]

## 缩写解释 & 库的导入

**`df`** --- 任意的`pandas DataFrame`(数据框)对象
**`s`** --- 任意的`pandas Series`(数组)对象
`pandas`和`numpy`是用Python做数据分析最基础且最核心的库

In [1]:

```python
import pandas as pd  # 导入pandas库并简写为pd
import numpy as np  # 导入numpy库并简写为np
```

## 数据的导入

```python
pd.read_csv(filename) # 导入csv格式文件中的数据
pd.read_table(filename) # 导入有分隔符的文本 (如TSV) 中的数据
pd.read_excel(filename) # 导入Excel格式文件中的数据
pd.read_sql(query, connection_object) # 导入SQL数据表/数据库中的数据
pd.read_json(json_string) # 导入JSON格式的字符，URL地址或者文件中的数据
pd.read_html(url) # 导入经过解析的URL地址中包含的数据框 (DataFrame) 数据
pd.read_clipboard() # 导入系统粘贴板里面的数据
pd.DataFrame(dict)  # 导入Python字典 (dict) 里面的数据，其中key是数据框的表头，value是数据框的内容。
```

## 数据的导出

```python
df.to_csv(filename) # 将数据框 (DataFrame)中的数据导入csv格式的文件中
df.to_excel(filename) # 将数据框 (DataFrame)中的数据导入Excel格式的文件中
df.to_sql(table_name,connection_object) # 将数据框 (DataFrame)中的数据导入SQL数据表/数据库中
df.to_json(filename) # 将数据框 (DataFrame)中的数据导入JSON格式的文件中
```

## 创建测试对象

```python
pd.DataFrame(np.random.rand(10,5)) # 创建一个5列10行的由随机浮点数组成的数据框 DataFrame
```

In [2]:

```python
pd.DataFrame(np.random.rand(10, 5))
```

Out[2]:

|      |        0 |        1 |        2 |        3 |        4 |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    0 | 0.992383 | 0.716095 | 0.161663 | 0.116856 | 0.522272 |
|    1 | 0.289110 | 0.619757 | 0.647899 | 0.916869 | 0.860023 |
|    2 | 0.964962 | 0.313809 | 0.173300 | 0.339013 | 0.404588 |
|    3 | 0.784580 | 0.955864 | 0.928128 | 0.972325 | 0.433533 |
|    4 | 0.321733 | 0.137054 | 0.560381 | 0.880524 | 0.030349 |
|    5 | 0.134500 | 0.142481 | 0.503147 | 0.045774 | 0.794175 |
|    6 | 0.224073 | 0.952283 | 0.561509 | 0.436029 | 0.995951 |
|    7 | 0.025046 | 0.452812 | 0.867835 | 0.246056 | 0.759832 |
|    8 | 0.244290 | 0.201439 | 0.150967 | 0.990055 | 0.648998 |
|    9 | 0.139209 | 0.491698 | 0.653071 | 0.075284 | 0.783967 |

```python
pd.Series(my_list) # 从一个可迭代的对象 my_list 中创建一个数据组
```

In [3]:

```python
my_list = ['Kesci', 100, '欢迎来到科赛网']
pd.Series(my_list)
```

Out[3]:

```python
0      Kesci
1        100
2    欢迎来到科赛网
dtype: object
df.index = pd.date_range('2017/1/1', periods=df.shape[0]) # 添加一个日期索引 index
```

In [4]:

```python
df = pd.DataFrame(np.random.rand(10, 5))
df.index = pd.date_range('2017/1/1', periods=df.shape[0])
df
```

Out[4]:

|            |        0 |        1 |        2 |        3 |        4 |
| ---------: | -------: | -------: | -------: | -------: | -------: |
| 2017-01-01 | 0.498020 | 0.329772 | 0.911521 | 0.830506 | 0.278821 |
| 2017-01-02 | 0.162519 | 0.863247 | 0.598759 | 0.109701 | 0.938164 |
| 2017-01-03 | 0.052235 | 0.402670 | 0.798829 | 0.950793 | 0.303408 |
| 2017-01-04 | 0.128301 | 0.515292 | 0.151855 | 0.783872 | 0.960438 |
| 2017-01-05 | 0.337411 | 0.816003 | 0.149155 | 0.315505 | 0.926379 |
| 2017-01-06 | 0.508463 | 0.669975 | 0.851335 | 0.502627 | 0.630517 |
| 2017-01-07 | 0.944626 | 0.534885 | 0.939777 | 0.714156 | 0.991689 |
| 2017-01-08 | 0.933364 | 0.751127 | 0.423170 | 0.805714 | 0.418434 |
| 2017-01-09 | 0.783284 | 0.486414 | 0.142663 | 0.090776 | 0.338737 |
| 2017-01-10 | 0.396959 | 0.254154 | 0.841090 | 0.201598 | 0.716140 |

## 数据的查看与检查

```python
df.head(n)  # 查看数据框的前n行
```

In [5]:

```python
df = pd.DataFrame(np.random.rand(10, 5))
df.head(3)
```

Out[5]:

|      |        0 |        1 |        2 |        3 |        4 |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    0 | 0.582419 | 0.869463 | 0.704490 | 0.846024 | 0.070841 |
|    1 | 0.833783 | 0.826977 | 0.976930 | 0.686765 | 0.655928 |
|    2 | 0.818402 | 0.688457 | 0.914534 | 0.122423 | 0.271376 |

```python
df.tail(n) # 查看数据框的最后n行
```

In [6]:

```python
df = pd.DataFrame(np.random.rand(10, 5))
df.tail(3)
```

Out[6]:

|      |        0 |        1 |        2 |        3 |        4 |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    7 | 0.535778 | 0.266737 | 0.311919 | 0.627568 | 0.792100 |
|    8 | 0.263778 | 0.966157 | 0.866713 | 0.646549 | 0.632052 |
|    9 | 0.138778 | 0.174860 | 0.346286 | 0.005019 | 0.559075 |

```python
df.shape # 查看数据框的行数与列数
```

In [7]:

```python
df = pd.DataFrame(np.random.rand(10, 5))
df.shape
```

Out[7]:

```python
(10, 5)
df.info() # 查看数据框 (DataFrame) 的索引、数据类型及内存信息
```

In [8]:

```python
df = pd.DataFrame(np.random.rand(10, 5))
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   0       10 non-null     float64
 1   1       10 non-null     float64
 2   2       10 non-null     float64
 3   3       10 non-null     float64
 4   4       10 non-null     float64
dtypes: float64(5)
memory usage: 528.0 bytes
df.describe() # 对于数据类型为数值型的列，查询其描述性统计的内容
```

In [9]:

```python
df.describe()
```

Out[9]:

|       |         0 |         1 |         2 |         3 |         4 |
| ----: | --------: | --------: | --------: | --------: | --------: |
| count | 10.000000 | 10.000000 | 10.000000 | 10.000000 | 10.000000 |
|  mean |  0.589169 |  0.610924 |  0.391939 |  0.528355 |  0.520741 |
|   std |  0.276406 |  0.225767 |  0.314642 |  0.261843 |  0.247268 |
|   min |  0.168179 |  0.288093 |  0.008446 |  0.141790 |  0.101371 |
|   25% |  0.346597 |  0.446950 |  0.162467 |  0.357671 |  0.349708 |
|   50% |  0.709907 |  0.695218 |  0.316381 |  0.502049 |  0.531618 |
|   75% |  0.798754 |  0.743281 |  0.628665 |  0.636728 |  0.640683 |
|   max |  0.894095 |  0.985350 |  0.885117 |  0.935236 |  0.980475 |

```python
s.value_counts(dropna=False) # 查询每个独特数据值出现次数统计
```

In [10]:

```python
s = pd.Series([1, 2, 3, 3, 4, np.nan, 5, 5, 5, 6, 7])
s.value_counts(dropna=False)
```

Out[10]:

```python
5.0    3
3.0    2
7.0    1
6.0    1
NaN    1
4.0    1
2.0    1
1.0    1
dtype: int64
df.apply(pd.Series.value_counts) # 查询数据框 (Data Frame) 中每个列的独特数据值出现次数统计
```

## 数据的选取

```python
df[col] # 以数组 Series 的形式返回选取的列
```

In [11]:

```python
df = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))
df['C']
```

Out[11]:

```python
0    0.476771
1    0.494334
2    0.247432
3    0.485696
4    0.222725
Name: C, dtype: float64
df[[col1, col2]] # 以新的数据框(DataFrame)的形式返回选取的列
```

In [12]:

```python
df = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))
df[['B', 'E']]
```

Out[12]:

|      |        B |        E |
| ---: | -------: | -------: |
|    0 | 0.401503 | 0.314893 |
|    1 | 0.099793 | 0.943586 |
|    2 | 0.740511 | 0.122502 |
|    3 | 0.207337 | 0.795587 |
|    4 | 0.671841 | 0.471724 |

```python
s.iloc[0] # 按照位置选取
```

In [13]:

```python
s = pd.Series(np.array(['I', 'Love', 'Data']))
s.iloc[0]
```

Out[13]:

```python
'I'
s.loc['index_one'] # 按照索引选取
```

In [14]:

```python
s = pd.Series(np.array(['I', 'Love', 'Data']))
s.loc[1]
```

Out[14]:

```python
'Love'
df.iloc[0,:] # 选取第一行
```

In [15]:

```python
df = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))
df.iloc[0, :]
```

Out[15]:

```python
A    0.549987
B    0.766152
C    0.934897
D    0.893586
E    0.176361
Name: 0, dtype: float64
df.iloc[0,0] # 选取第一行的第一个元素
```

In [16]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.iloc[0, 0]
```

Out[16]:

```python
0.340428204447891
```

## 数据的清洗

```python
df.columns = ['a','b'] # 重命名数据框的列名称
```

In [17]:

```python
df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
                   'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
                   'C': 'foo'})
df.columns = ['a', 'b', 'c']
df
```

Out[17]:

|      |    a |    b |    c |
| ---: | ---: | ---: | ---: |
|    0 |  1.0 |  NaN |  foo |
|    1 |  NaN |  4.0 |  foo |
|    2 |  2.0 |  NaN |  foo |
|    3 |  3.0 |  5.0 |  foo |
|    4 |  6.0 |  9.0 |  foo |
|    5 |  NaN |  NaN |  foo |

```python
pd.isnull() # 检查数据中空值出现的情况，并返回一个由布尔值(True,Fale)组成的列
```

In [18]:

```python
df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
                   'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
                   'C': 'foo'})
pd.isnull(df)
```

Out[18]:

|      |     A |     B |     C |
| ---: | ----: | ----: | ----: |
|    0 | False |  True | False |
|    1 |  True | False | False |
|    2 | False |  True | False |
|    3 | False | False | False |
|    4 | False | False | False |
|    5 |  True |  True | False |

```python
pd.notnull() # 检查数据中非空值出现的情况，并返回一个由布尔值(True,False)组成的列
```

In [19]:

```python
df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
                   'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
                   'C': 'foo'})
pd.notnull(df)
```

Out[19]:

|      |     A |     B |    C |
| ---: | ----: | ----: | ---: |
|    0 |  True | False | True |
|    1 | False |  True | True |
|    2 |  True | False | True |
|    3 |  True |  True | True |
|    4 |  True |  True | True |
|    5 | False | False | True |

```python
df.dropna() # 移除数据框 DataFrame 中包含空值的行
```

In [20]:

```python
df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
                   'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
                   'C': 'foo'})
df.dropna()
```

Out[20]:

|      |    A |    B |    C |
| ---: | ---: | ---: | ---: |
|    3 |  3.0 |  5.0 |  foo |
|    4 |  6.0 |  9.0 |  foo |

```python
df.dropna(axis=1) # 移除数据框 DataFrame 中包含空值的列
```

In [21]:

```python
df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
                   'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
                   'C': 'foo'})
df.dropna(axis=1)
```

Out[21]:

|      |    C |
| ---: | ---: |
|    0 |  foo |
|    1 |  foo |
|    2 |  foo |
|    3 |  foo |
|    4 |  foo |
|    5 |  foo |

```python
df.dropna(axis=0,thresh=n)
```

In [22]:

```python
df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
                   'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
                   'C': 'foo'})
test = df.dropna(axis=1, thresh=1)
test
```

Out[22]:

|      |    A |    B |    C |
| ---: | ---: | ---: | ---: |
|    0 |  1.0 |  NaN |  foo |
|    1 |  NaN |  4.0 |  foo |
|    2 |  2.0 |  NaN |  foo |
|    3 |  3.0 |  5.0 |  foo |
|    4 |  6.0 |  9.0 |  foo |
|    5 |  NaN |  NaN |  foo |

```python
df.fillna(x) # 将数据框 DataFrame 中的所有空值替换为 x
```

In [23]:

```python
df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
                   'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
                   'C': 'foo'})
df.fillna('Test')
```

Out[23]:

|      |    A |    B |    C |
| ---: | ---: | ---: | ---: |
|    0 |    1 | Test |  foo |
|    1 | Test |    4 |  foo |
|    2 |    2 | Test |  foo |
|    3 |    3 |    5 |  foo |
|    4 |    6 |    9 |  foo |
|    5 | Test | Test |  foo |

`s.fillna(s.mean())` -> 将所有空值替换为平均值

In [24]:

```python
s = pd.Series([1, 3, 5, np.nan, 7, 9, 9])
s.fillna(s.mean())
```

Out[24]:

```python
0    1.000000
1    3.000000
2    5.000000
3    5.666667
4    7.000000
5    9.000000
6    9.000000
dtype: float64
s.astype(float) # 将数组(Series)的格式转化为浮点数
```

In [25]:

```python
s = pd.Series([1, 3, 5, np.nan, 7, 9, 9])
s.astype(float)
```

Out[25]:

```python
0    1.0
1    3.0
2    5.0
3    NaN
4    7.0
5    9.0
6    9.0
dtype: float64
s.replace(1,'one') # 将数组(Series)中的所有1替换为'one'
```

In [26]:

```python
s = pd.Series([1, 3, 5, np.nan, 7, 9, 9])
s.replace(1, 'one')
```

Out[26]:

```python
0    one
1      3
2      5
3    NaN
4      7
5      9
6      9
dtype: object
s.replace([1,3],['one','three']) # 将数组(Series)中所有的1替换为'one', 所有的3替换为'three'
```

In [27]:

```python
s = pd.Series([1, 3, 5, np.nan, 7, 9, 9])
s.replace([1, 3], ['one', 'three'])
```

Out[27]:

```python
0      one
1    three
2        5
3      NaN
4        7
5        9
6        9
dtype: object
df.rename(columns=lambda x: x + 2) # 将全体列重命名
```

In [28]:

```python
df = pd.DataFrame(np.random.rand(4, 4))
df.rename(columns=lambda x: x + 2)
```

Out[28]:

|      |        2 |        3 |        4 |        5 |
| ---: | -------: | -------: | -------: | -------: |
|    0 | 0.039120 | 0.690044 | 0.171641 | 0.187174 |
|    1 | 0.597687 | 0.421282 | 0.087235 | 0.774940 |
|    2 | 0.170161 | 0.650976 | 0.178237 | 0.207947 |
|    3 | 0.501003 | 0.456650 | 0.684570 | 0.638107 |

```python
df.rename(columns={'old_name': 'new_ name'}) # 将选择的列重命名
```

In [29]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.rename(columns={'A': 'newA', 'C': 'newC'})
```

Out[29]:

|      |     newA |        B |     newC |        D |        E |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    0 | 0.564240 | 0.130336 | 0.744366 | 0.009874 | 0.103483 |
|    1 | 0.049422 | 0.379704 | 0.076864 | 0.016094 | 0.205143 |
|    2 | 0.759474 | 0.219868 | 0.202509 | 0.321344 | 0.095714 |
|    3 | 0.246577 | 0.224125 | 0.393572 | 0.358476 | 0.629874 |
|    4 | 0.287901 | 0.424431 | 0.167274 | 0.072632 | 0.553908 |
|    5 | 0.782189 | 0.791870 | 0.427531 | 0.615957 | 0.507143 |
|    6 | 0.659629 | 0.938048 | 0.904857 | 0.719031 | 0.390149 |
|    7 | 0.711851 | 0.695431 | 0.290404 | 0.289281 | 0.019986 |
|    8 | 0.241688 | 0.916922 | 0.211505 | 0.915913 | 0.093236 |
|    9 | 0.600458 | 0.394810 | 0.474375 | 0.785903 | 0.147838 |

```python
df.set_index('column_one') # 改变索引
```

In [30]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.set_index('B')
```

Out[30]:

|          |        A |        C |        D |        E |
| -------: | -------: | -------: | -------: | -------: |
|        B |          |          |          |          |
| 0.385448 | 0.879960 | 0.536482 | 0.730074 | 0.170356 |
| 0.363562 | 0.048175 | 0.505362 | 0.865739 | 0.286770 |
| 0.036223 | 0.279795 | 0.974306 | 0.902042 | 0.401785 |
| 0.620656 | 0.860259 | 0.672643 | 0.281486 | 0.684360 |
| 0.654486 | 0.152644 | 0.004815 | 0.952303 | 0.599696 |
| 0.681292 | 0.029903 | 0.240921 | 0.151107 | 0.832835 |
| 0.256339 | 0.568686 | 0.323086 | 0.134549 | 0.542373 |
| 0.530859 | 0.788472 | 0.858628 | 0.580164 | 0.040929 |
| 0.110683 | 0.545847 | 0.460413 | 0.543227 | 0.929097 |
| 0.019038 | 0.223477 | 0.497246 | 0.061327 | 0.738607 |

```python
df.rename(index = lambda x: x+ 1) # 改变全体索引
```

In [31]:

```python
df = pd.DataFrame(np.random.rand(10, 5))
df.rename(index=lambda x: x + 1)
```

Out[31]:

|      |        0 |        1 |        2 |        3 |        4 |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    1 | 0.389327 | 0.754920 | 0.627689 | 0.517485 | 0.837760 |
|    2 | 0.105335 | 0.479006 | 0.144424 | 0.157142 | 0.104914 |
|    3 | 0.309137 | 0.584110 | 0.183372 | 0.574634 | 0.564165 |
|    4 | 0.954056 | 0.744852 | 0.137678 | 0.673362 | 0.404816 |
|    5 | 0.753247 | 0.087437 | 0.184610 | 0.748287 | 0.608873 |
|    6 | 0.035664 | 0.661187 | 0.246439 | 0.227717 | 0.938146 |
|    7 | 0.262410 | 0.225042 | 0.277211 | 0.710138 | 0.675527 |
|    8 | 0.883649 | 0.171360 | 0.627889 | 0.878054 | 0.559566 |
|    9 | 0.591810 | 0.174026 | 0.701503 | 0.678402 | 0.994334 |
|   10 | 0.701636 | 0.060573 | 0.513308 | 0.454019 | 0.402268 |

## 数据的过滤(`filter`),排序(`sort`)和分组(`groupby`)

```python
df[df[col] > 0.5] # 选取数据框df中对应行的数值大于0.5的全部列
```

In [32]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df[df['A'] > 0.5]
```

Out[32]:

|      |        A |        B |        C |        D |        E |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    0 | 0.693879 | 0.456541 | 0.455010 | 0.993185 | 0.959357 |
|    3 | 0.646641 | 0.194007 | 0.149751 | 0.967932 | 0.436454 |
|    5 | 0.774606 | 0.721484 | 0.322516 | 0.554003 | 0.385439 |
|    6 | 0.712382 | 0.351449 | 0.432008 | 0.096635 | 0.089920 |
|    8 | 0.523279 | 0.909140 | 0.930049 | 0.906749 | 0.078852 |

```python
df[(df[col] > 0.5) & (df[col] < 0.7)] # 选取数据框df中对应行的数值大于0.5，并且小于0.7的全部列
```

In [33]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df[(df['C'] > 0.5) & (df['D'] < 0.7)]
```

Out[33]:

|      |        A |        B |        C |        D |        E |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    0 | 0.922783 | 0.177324 | 0.684640 | 0.278763 | 0.204582 |
|    5 | 0.617559 | 0.059023 | 0.678670 | 0.022527 | 0.139393 |
|    6 | 0.301231 | 0.664538 | 0.940991 | 0.295420 | 0.117700 |
|    8 | 0.328655 | 0.964972 | 0.929662 | 0.611708 | 0.631567 |
|    9 | 0.266233 | 0.622073 | 0.547397 | 0.667184 | 0.529296 |

```python
df.sort_values(col1) # 按照数据框的列col1升序(ascending)的方式对数据框df做排序
```

In [34]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.sort_values('E')
```

Out[34]:

|      |        A |        B |        C |        D |        E |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    3 | 0.721501 | 0.079721 | 0.549805 | 0.645155 | 0.235857 |
|    2 | 0.146009 | 0.854982 | 0.674135 | 0.450298 | 0.281226 |
|    7 | 0.633146 | 0.365379 | 0.032499 | 0.373151 | 0.317509 |
|    5 | 0.709059 | 0.978207 | 0.569809 | 0.845665 | 0.320445 |
|    4 | 0.453705 | 0.037362 | 0.461966 | 0.301737 | 0.432204 |
|    0 | 0.795553 | 0.585600 | 0.763285 | 0.923194 | 0.461403 |
|    8 | 0.430839 | 0.220663 | 0.230400 | 0.895529 | 0.499241 |
|    1 | 0.652674 | 0.961533 | 0.629068 | 0.627334 | 0.528052 |
|    6 | 0.941002 | 0.496111 | 0.618649 | 0.899071 | 0.825232 |
|    9 | 0.074218 | 0.546182 | 0.940444 | 0.679209 | 0.865196 |

```python
df.sort_values(col2,ascending=False) # 按照数据框的列col2降序(descending)的方式对数据框df做排序
```

In [35]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.sort_values('A', ascending=False)
```

Out[35]:

|      |        A |        B |        C |        D |        E |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    9 | 0.823613 | 0.233609 | 0.943317 | 0.029255 | 0.966745 |
|    0 | 0.819282 | 0.446959 | 0.652876 | 0.535949 | 0.121519 |
|    2 | 0.805077 | 0.719059 | 0.704812 | 0.629141 | 0.599756 |
|    3 | 0.798725 | 0.732774 | 0.199525 | 0.758943 | 0.028083 |
|    1 | 0.763993 | 0.181730 | 0.416662 | 0.058995 | 0.573182 |
|    4 | 0.715854 | 0.140384 | 0.759268 | 0.395065 | 0.282308 |
|    6 | 0.627041 | 0.228966 | 0.388350 | 0.890482 | 0.158743 |
|    5 | 0.530041 | 0.782867 | 0.762835 | 0.157307 | 0.056667 |
|    7 | 0.514663 | 0.379581 | 0.294378 | 0.442238 | 0.776028 |
|    8 | 0.366379 | 0.032669 | 0.602993 | 0.508338 | 0.058742 |

```python
df.sort_values([col1,col2],ascending=[True,False]) # 按照数据框的列col1升序，col2降序的方式对数据框df做排序
```

In [36]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.sort_values(['A', 'E'], ascending=[True, False])
```

Out[36]:

|      |        A |        B |        C |        D |        E |
| ---: | -------: | -------: | -------: | -------: | -------: |
|    6 | 0.117891 | 0.193781 | 0.211916 | 0.307558 | 0.798481 |
|    2 | 0.220438 | 0.148594 | 0.745653 | 0.125348 | 0.075224 |
|    1 | 0.254839 | 0.148040 | 0.429642 | 0.126434 | 0.978878 |
|    5 | 0.293847 | 0.731311 | 0.160822 | 0.545814 | 0.667201 |
|    7 | 0.414441 | 0.187809 | 0.741260 | 0.652332 | 0.762700 |
|    9 | 0.447650 | 0.830519 | 0.137817 | 0.200369 | 0.514270 |
|    3 | 0.485170 | 0.911830 | 0.388681 | 0.971249 | 0.150237 |
|    4 | 0.496401 | 0.908903 | 0.181293 | 0.199229 | 0.651060 |
|    0 | 0.557614 | 0.805830 | 0.497868 | 0.970623 | 0.719473 |
|    8 | 0.686097 | 0.559635 | 0.128870 | 0.379140 | 0.590979 |

```python
df.groupby(col) # 按照某列对数据框df做分组
```

In [37]:

```python
df = pd.DataFrame({'A': np.array(['foo', 'foo', 'foo', 'foo', 'bar', 'bar']),
                   'B': np.array(['one', 'one', 'two', 'two', 'three', 'three']),
                   'C': np.array(['small', 'medium', 'large', 'large', 'small', 'small']),
                   'D': np.array([1, 2, 2, 3, 3, 5])})

df.groupby('A').count()
```

Out[37]:

|      |    B |    C |    D |
| ---: | ---: | ---: | ---: |
|    A |      |      |      |
|  bar |    2 |    2 |    2 |
|  foo |    4 |    4 |    4 |

```python
df.groupby([col1,col2]) # 按照列col1和col2对数据框df做分组
```

In [38]:

```python
df = pd.DataFrame({'A': np.array(['foo', 'foo', 'foo', 'foo', 'bar', 'bar']),
                   'B': np.array(['one', 'one', 'two', 'two', 'three', 'three']),
                   'C': np.array(['small', 'medium', 'large', 'large', 'small', 'small']),
                   'D': np.array([1, 2, 2, 3, 3, 5])})

df.groupby(['B', 'C']).sum()
```

Out[38]:

|       |        |    D |
| ----: | -----: | ---: |
|     B |      C |      |
|   one | medium |    2 |
| small |      1 |      |
| three |  small |    8 |
|   two |  large |    5 |

```python
df.groupby(col1)[col2].mean() # 按照列col1对数据框df做分组处理后，返回对应的col2的平均值
```

In [39]:

```python
df = pd.DataFrame({'A': np.array(['foo', 'foo', 'foo', 'foo', 'bar', 'bar']),
                   'B': np.array(['one', 'one', 'two', 'two', 'three', 'three']),
                   'C': np.array(['small', 'medium', 'large', 'large', 'small', 'small']),
                   'D': np.array([1, 2, 2, 3, 3, 5])})
df.groupby('B')['D'].mean()
```

Out[39]:

```python
B
one      1.5
three    4.0
two      2.5
Name: D, dtype: float64
pythyon
df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean) # 做透视表，索引为col1,针对的数值列为col2和col3，分组函数为平均值
```

In [40]:

```python
df = pd.DataFrame({'A': np.array(['foo', 'foo', 'foo', 'foo', 'bar', 'bar']),
                   'B': np.array(['one', 'one', 'two', 'two', 'three', 'three']),
                   'C': np.array(['small', 'medium', 'large', 'large', 'small', 'small']),
                   'D': np.array([1, 2, 2, 3, 3, 5])})

df.pivot_table(df, index=['A', 'B'],
               columns=['C'], aggfunc=np.sum)
```

Out[40]:

|      |       |     D |        |       |
| ---: | ----: | ----: | -----: | ----: |
|      |     C | large | medium | small |
|    A |     B |       |        |       |
|  bar | three |   NaN |    NaN |   8.0 |
|  foo |   one |   NaN |    2.0 |   1.0 |
|  two |   5.0 |   NaN |    NaN |       |

```python
df.groupby(col1).agg(np.mean)
```

In [41]:

```python
df = pd.DataFrame({'A': np.array(['foo', 'foo', 'foo', 'foo', 'bar', 'bar']),
                   'B': np.array(['one', 'one', 'two', 'two', 'three', 'three']),
                   'C': np.array(['small', 'medium', 'large', 'large', 'small', 'small']),
                   'D': np.array([1, 2, 2, 3, 3, 5])})
df.groupby('A').agg(np.mean)
```

Out[41]:

|      |    D |
| ---: | ---: |
|    A |      |
|  bar |    4 |
|  foo |    2 |

```python
df.apply(np.mean) # 对数据框df的每一列求平均值
```

In [42]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.apply(np.mean)
```

Out[42]:

```python
A    0.454125
B    0.623123
C    0.532732
D    0.599910
E    0.381878
dtype: float64
df.apply(np.max,axis=1) # 对数据框df的每一行求最大值
```

In [43]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.apply(np.max, axis=1)
```

Out[43]:

```python
0    0.999668
1    0.962350
2    0.872729
3    0.609157
4    0.916815
5    0.984198
6    0.938242
7    0.905574
8    0.920740
9    0.854575
dtype: float64
```

## 数据的连接(`join`)与组合(`combine`)

```python
df1.append(df2) # 在数据框df2的末尾添加数据框df1，其中df1和df2的列数应该相等
```

In [44]:

```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df1.append(df2)
```

Out[44]:

|      |    A |    B |    C |    D |
| ---: | ---: | ---: | ---: | ---: |
|    0 |   A0 |   B0 |   C0 |   D0 |
|    1 |   A1 |   B1 |   C1 |   D1 |
|    2 |   A2 |   B2 |   C2 |   D2 |
|    3 |   A3 |   B3 |   C3 |   D3 |
|    4 |   A4 |   B4 |   C4 |   D4 |
|    5 |   A5 |   B5 |   C5 |   D5 |
|    6 |   A6 |   B6 |   C6 |   D6 |
|    7 |   A7 |   B7 |   C7 |   D7 |

```python
pd.concat([df1, df2],axis=1) # 在数据框df1的列最后添加数据框df2,其中df1和df2的行数应该相等
```

In [45]:

```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
pd.concat([df1, df2], axis=1)
```

Out[45]:

|      |    A |    B |    C |    D |    A |    B |    C |    D |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |   A0 |   B0 |   C0 |   D0 |  NaN |  NaN |  NaN |  NaN |
|    1 |   A1 |   B1 |   C1 |   D1 |  NaN |  NaN |  NaN |  NaN |
|    2 |   A2 |   B2 |   C2 |   D2 |  NaN |  NaN |  NaN |  NaN |
|    3 |   A3 |   B3 |   C3 |   D3 |  NaN |  NaN |  NaN |  NaN |
|    4 |  NaN |  NaN |  NaN |  NaN |   A4 |   B4 |   C4 |   D4 |
|    5 |  NaN |  NaN |  NaN |  NaN |   A5 |   B5 |   C5 |   D5 |
|    6 |  NaN |  NaN |  NaN |  NaN |   A6 |   B6 |   C6 |   D6 |
|    7 |  NaN |  NaN |  NaN |  NaN |   A7 |   B7 |   C7 |   D7 |

```python
df1.join(df2,on=col1,how='inner') # 对数据框df1和df2做内连接，其中连接的列为col1
```

In [46]:

```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'key': ['K0', 'K1', 'K0', 'K1']})


df2 = pd.DataFrame({'C': ['C0', 'C1'],
                    'D': ['D0', 'D1']},
                   index=['K0', 'K1'])


df1.join(df2, on='key')
```

Out[46]:

|      |    A |    B |  key |    C |    D |
| ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |   A0 |   B0 |   K0 |   C0 |   D0 |
|    1 |   A1 |   B1 |   K1 |   C1 |   D1 |
|    2 |   A2 |   B2 |   K0 |   C0 |   D0 |
|    3 |   A3 |   B3 |   K1 |   C1 |   D1 |

## 数据的统计

```python
df.describe() # 得到数据框df每一列的描述性统计
```

In [47]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.describe()
```

Out[47]:

|       |         A |         B |         C |         D |         E |
| ----: | --------: | --------: | --------: | --------: | --------: |
| count | 10.000000 | 10.000000 | 10.000000 | 10.000000 | 10.000000 |
|  mean |  0.464471 |  0.634424 |  0.570797 |  0.444228 |  0.688528 |
|   std |  0.271674 |  0.300501 |  0.352202 |  0.284852 |  0.169166 |
|   min |  0.044374 |  0.202519 |  0.024244 |  0.081870 |  0.466740 |
|   25% |  0.271183 |  0.396330 |  0.242415 |  0.153360 |  0.609046 |
|   50% |  0.538884 |  0.698498 |  0.669724 |  0.511760 |  0.666220 |
|   75% |  0.637757 |  0.884501 |  0.840758 |  0.623435 |  0.720125 |
|   max |  0.812592 |  0.967966 |  0.992781 |  0.889898 |  0.989515 |

```python
df.mean() # 得到数据框df中每一列的平均值
```

In [48]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.mean()
```

Out[48]:

```python
A    0.489851
B    0.451722
C    0.524296
D    0.345105
E    0.393762
dtype: float64
df.corr() # 得到数据框df中每一列与其他列的相关系数
```

In [49]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.corr()
```

Out[49]:

|      |         A |         B |         C |         D |         E |
| ---: | --------: | --------: | --------: | --------: | --------: |
|    A |  1.000000 |  0.261535 |  0.204209 |  0.144253 | -0.233152 |
|    B |  0.261535 |  1.000000 | -0.113173 | -0.317966 |  0.262074 |
|    C |  0.204209 | -0.113173 |  1.000000 |  0.135071 |  0.183491 |
|    D |  0.144253 | -0.317966 |  0.135071 |  1.000000 | -0.062077 |
|    E | -0.233152 |  0.262074 |  0.183491 | -0.062077 |  1.000000 |

```python
df.count() # 得到数据框df中每一列的非空值个数
```

In [50]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.count()
```

Out[50]:

```python
A    10
B    10
C    10
D    10
E    10
dtype: int64
df.max() # 得到数据框df中每一列的最大值
```

In [51]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.max()
```

Out[51]:

```python
A    0.998762
B    0.956032
C    0.985195
D    0.929673
E    0.943144
dtype: float64
df.min() # 得到数据框df中每一列的最小值
```

In [52]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.min()
```

Out[52]:

```python
A    0.109613
B    0.135043
C    0.104794
D    0.084585
E    0.144223
dtype: float64
df.median() # 得到数据框df中每一列的中位数
```

In [53]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.median()
```

Out[53]:

```python
A    0.420253
B    0.335278
C    0.581242
D    0.503674
E    0.455265
dtype: float64
df.std() # 得到数据框df中每一列的标准差
```

In [54]:

```python
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.std()
```

Out[54]:

```python
A    0.320035
B    0.279819
C    0.325366
D    0.217627
E    0.320668
dtype: float64
```