#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print('L[0:3] =', L[0:3])

# 如果第一个索引是0，还可以省略：
print('L[:3] =', L[:3])

# 也可以从索引1开始，取出2个元素出来：
print('L[1:3] =', L[1:3])

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print('L[-2:] =', L[-2:])

# 切片操作十分有用。我们先创建一个0-99的数列：
R = list(range(100))

# 可以通过切片轻松取出某一段数列。比如前10个数：
print('R[:10] =', R[:10])

# 后10个数：
print('R[-10:] =', R[-10:])

# 前11-20个数：
print('R[10:20] =', R[10:20])

# 前10个数，每两个取一个：
print('R[:10:2] =', R[:10:2])

# 所有数，每5个取一个：
print('R[::5] =', R[::5])

# 甚至什么都不写，只写[:]就可以原样复制一个list：
print('R[:] =', R[:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
