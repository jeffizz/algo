---
source: https://www.zend.com/resources/php-extensions/php-arrays
---
# INTERNAL PHP ARRAY REPRESENTATION


![](assets/PHP%20Array/file-20260225215547424.png)

Now, let’s look into the internal PHP array representation. The value field of “zval” with IS_ARRAY type keeps a pointer to “zend_array” structure. It’s “inherited” from zend_refcounted”, that defines the format of the first 64-bit word with reference-counter. 

Other fields are specific for zend_array or HashTable. The most important one is “arData”, which is a pointer to a dependent data structure. Actually, they are two data structures allocated as a single memory block. 

Above the address, pointed by “arData”, is the “Hash” part (described above). Below, the same address is, the “Ordered Values” part. The “Hash” part is a turned-down array of 32-bit Bucket offsets, indexed by hash value. This part may be missed for packed arrays, and in this case, the Buckets are accessed directly by numeric indexes. 

The “Ordered Values” part is an array of Buckets. Each Bucket contains embedded zval, string key represented by a pointer to zend_ string (it’s NULL for numeric key), and numeric key (or string hash_value for string key). Reserved space in zvlas is used to organize linked-list of colliding elements. It contains an index of the next element with the same hash_value.

---
## 一、 宏观层面的逻辑链路

当你定义 `$arr = [1, 2];` 时，内存中的引用链条如下：

1. **符号表 (Symbol Table)**：存储变量名（标识符）`"arr"`。
2. **指针**：符号表指向一个 **`zval`** 结构体。
3. **zval (入口)**：类型标记为 `IS_ARRAY`，其 `value` 指向一个 **`zend_array`**。
4. **zend_array (控制面板)**：存储数组元数据（容量、元素数、**`arData` 指针**）。
5. **arData (存储区)**：指向一块连续内存，分为“地下室（映射表）”和“地上（Bucket）”。
6. **Bucket (房间)**：内部**直接嵌入**一个 `zval`，存放最终数据。
    
## 二、 核心结构体拆解

### 1. 存储单元：Bucket

每个 Bucket 约占 32 字节（64 位系统），内部结构如下：
- **`h`**：存储 Key 的原始哈希值（如果是数字索引，直接存数字）。
- **`key`**：如果是字符串键，指向 `zend_string`；如果是数字键，则为 `NULL`。
- **`val`**：**关键优化点！** 这是一个**内联**的 `zval` 结构体，不是指针
### 2. 管理中心：HashTable (zend_array)

这是数组的“大脑”，包含：
- **`nTableSize`**：总容量（始终是 $2^n$）。
- **`nNumOfElem`**：有效元素个数（`count()` 的结果）。
- **`nNumUsed`**：已使用的槽位（包含已删除但未清理的 `IS_UNDEF` 元素）。
- **`nTableMask`**：掩码（通常是 `-nTableSize`），用于哈希寻址。
## 三、 两种运作模式

### 1. Packed Array (紧凑模式)

- **条件**：键名是连续递增的整数（如 `[0, 1, 2]`）。
- **逻辑**：
    - **没有“地下室”**：省去了哈希索引映射表。
    - **极致性能**：访问 `$a[2]` 相当于 C 语言的 `arData[2]`，性能等同于原生数组。
### 2. Hash Array (关联模式)

- **条件**：包含字符串键，或数字键不连续（如 `[0, 10, 100]`）。
- **逻辑**：
    - **启用“地下室”**：在 `arData` 指针的前面（负偏移量方向）开辟映射表。
    - **查找流程**：`Key` $\rightarrow$ `Hash` $\rightarrow$ `映射表` $\rightarrow$ `得到物理偏移量` $\rightarrow$ `去 arData 找 Bucket`。



