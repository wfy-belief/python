## 待更新

## 列表和三目运算符

<iframe 
src="https://player.bilibili.com/player.html?cid=209905451&aid=838821380&page=1&as_wide=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="640" height="430" > </iframe>
-

```python
L1 = [1, 2, 3]
L2 = [4, 5, 6]
if 7 in L1:
    print(L1 + L2)
else:
    print(L1)

# 三目运算符
print(L1 + L2) if 1 in L1 else print(L1)

# 切片[start:end: jiange]

print(L1[::])
print(L1[::-1])
print(L1[0:2:])
print(L1[0:2:-1])
print(L1[1::-1])

# print(L1.reverse(), L1)
value = -1
if value in L1:
    print(L1.index(value))
print(222222)

# max
print(max(L1))
print(min(L1))
print(sum(L1))
print(len(L1))
print(sum(L1) / len(L1))

print(L1.count(-1))

# python 栈 和 队列 的知识
```

## 栈和队列

<iframe 
src="//player.bilibili.com/player.html?aid=838821380&bvid=BV1Kg4y1i737&cid=209905245&page=2&as_wide=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="640" height="430" > </iframe>

```python
# 栈 后进先出
stack = list()
print(stack)

# 栈空
if not stack:
    print('栈空')
if stack:
    print('栈非空')

# 进栈
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# 出栈
stack.pop()

print(stack)

# 队列 先进先出 queue
queue = [1,2,3]

# queue.append()

# 出队
queue.pop(0)
print(queue)

queue = []
# if not stack:
if queue:
    queue.pop(0)
print(queue)
```

## 高级排序

<iframe 
src="//player.bilibili.com/player.html?aid=838821380&bvid=BV1Kg4y1i737&cid=210224189&page=3&as_wide=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="640" height="430" > </iframe>

```python
# python 高级排序
# 1.[]
# 2.[(a, b), (a, b)]
# 3.[{'key1':value1, 'key2':'value2'}, {'key1':value1, 'key2':'value2'}]
# 4.{"key":[]} [(int, [xxx], {}), (int, [xxx], {})]
l = [5, 2, 1, 6, 4, 7, 3]
# l.sort()
# print(l)
l.sort(reverse=True)
print(l)

a = [(3, 1), (2, 3), (1, 2), (1, 0), (1, 3)]
# a.sort(reverse=True)
# print(a)
# key1 ↑ key2 ↓
a.sort(key=lambda x: (x[0], -x[1]))
print(a)

a = [{'key1': 3, 'key2': 1},
     {'key1': 2, 'key2': 3},
     {'key1': 1, 'key2': 2},
     {'key1': 1, 'key2': 0},
     {'key1': 1, 'key2': 3}]

a.sort(key=lambda x: (x['key1'], -x['key2']))
print(a)

```

## 原来你是这样的循环
<iframe 
src="//player.bilibili.com/player.html?aid=838821380&bvid=BV1Kg4y1i737&cid=210569015&page=4&as_wide=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="640" height="430" > </iframe>

```python
# for
# while
'''
for i in range(10):
    print(i)

Left, Right = 6, 10
for i in range(Left, Right):
    print(i)
'''
'''
for i in range(10):
    i += 3
    print(i)
'''
'''
for i in range(3):
    print(6)

for _ in range(3):
    print(6)
'''
'''
value = 3
flag = 0
for i in range(10):
    # 终止条件
    if i == value:
        flag = 1
        break

if flag:
    xxx
else:
    xxx'''

value = 11
flag = 0
for i in range(10):
    # 终止条件
    if i == value:
        print("success")
        break
else:
    print("f")
# su shu 
for i in range(3, 20):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            print("f")
            break
    else:
        print("it is su shu", i)

# while

while xx:
    xxx

i = -1

while i < 0:
    i += 1

while xx:


    pass
else:
    pass

for obj in OBJ ->: list set turlp dict  .... str
```

## 集合交并补 

<iframe 
src="//player.bilibili.com/player.html?aid=838821380&bvid=BV1Kg4y1i737&cid=210971983&page=5&as_wide=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="640" height="430" > </iframe>


```python
# for
# while
'''
for i in range(10):
    print(i)

Left, Right = 6, 10
for i in range(Left, Right):
    print(i)
'''
'''
for i in range(10):
    i += 3
    print(i)
'''
'''
for i in range(3):
    print(6)

for _ in range(3):
    print(6)
'''
'''
value = 3
flag = 0
for i in range(10):
    # 终止条件
    if i == value:
        flag = 1
        break

if flag:
    xxx
else:
    xxx'''

value = 11
flag = 0
for i in range(10):
    # 终止条件
    if i == value:
        print("success")
        break
else:
    print("f")
# su shu 
for i in range(3, 20):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            print("f")
            break
    else:
        print("it is su shu", i)

# while

while xx:
    xxx

i = -1

while i < 0:
    i += 1

while xx:


    pass
else:
    pass

for obj in OBJ ->: list set turlp dict  .... str
```


