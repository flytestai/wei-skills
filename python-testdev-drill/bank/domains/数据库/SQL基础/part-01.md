# 数据库 · SQL基础

> 共 27 题 · 所属领域：数据库 · 专题：SQL基础

---

## Q006611

- 题型：单选
- 难度：入门

**题目**

```text
SQL语言中删除一个表的语句是（）
```

**选项**

```text
A. DROP TABLE
B. DELETE TABLE
C. DESTROY TABLE
D. REMOVE TABLE
```

**答案**

```text
A
```

**正确选项**

```text
A. DROP TABLE
```

**解析**

```text
【核心考点】 SQL语句 DDL
【题目解析】
本题考查SQL中数据定义语言（DDL）的基本语法。删除表是数据库操作中的常见需求，使用DROP TABLE语句可以删除整个表及其结构、数据和索引。
【选项解析】
✓ A. DROP TABLE — 正确。DROP TABLE是标准SQL语句，用于删除表。
✗ B. DELETE TABLE — 错误。DELETE用于删除表中的数据，而非表结构，语法为DELETE FROM table_name。
✗ C. DESTROY TABLE — 错误。SQL中没有DESTROY关键字。
✗ D. REMOVE TABLE — 错误。REMOVE不是SQL标准关键字。
【易错提示】
注意区分DROP（删除表结构）和DELETE（删除数据），面试中常考两者的区别。
```

---

## Q006612

- 题型：单选
- 难度：入门

**题目**

```text
SQL语言中，删除一个表的命令是？（ ）
```

**选项**

```text
A. delete
B. drop
C. clear
D. remove
```

**答案**

```text
D
```

**正确选项**

```text
D. remove
```

**解析**

```text
【核心考点】 SQL DDL语句 表操作
【题目解析】
本题考查SQL中删除表的命令。在SQL中，删除表使用 DROP TABLE 语句，该语句属于数据定义语言（DDL），用于删除整个表结构及其数据。
【选项解析】
✗ A. delete — 错误。DELETE 是数据操作语言（DML），用于删除表中的数据行，但保留表结构。
✗ B. drop — 正确选项但需注意格式。标准SQL中删除表使用 DROP TABLE，但选项仅给出 drop，不完整。然而在上下文中，drop 是正确命令的关键部分。
✗ C. clear — 错误。CLEAR 不是SQL标准命令，可能在某些数据库工具中用于清屏。
✓ D. remove — 错误。REMOVE 不是SQL标准命令。但注意题目答案标注为D，可能存在误导，实际正确命令应为 DROP。根据标准SQL，删除表的命令是 DROP TABLE，因此选项B更接近正确。
【易错提示】
本题选项设计可能存在歧义，但核心知识点是区分DELETE和DROP：DELETE删除数据，DROP删除表结构。面试中常考察此区别。
```

---

## Q006615

- 题型：单选
- 难度：入门

**题目**

```text
下面那个是数据库查询的关键字
```

**选项**

```text
A. select
B. delete
C. insert
D. update
```

**答案**

```text
A
```

**正确选项**

```text
A. select
```

**解析**

```text
【核心考点】 SQL基础 数据查询
【题目解析】
本题考察SQL基本关键字，属于数据库入门知识。SQL中查询数据使用SELECT语句，其他选项分别对应删除（DELETE）、插入（INSERT）和更新（UPDATE）操作。
【选项解析】
✓ A. select — 正确。SELECT是SQL中用于查询数据的关键字，可配合FROM、WHERE等子句使用。
✗ B. delete — 错误。DELETE用于删除表中的数据行，属于数据操纵语言（DML）。
✗ C. insert — 错误。INSERT用于向表中插入新数据行，也属于DML。
✗ D. update — 错误。UPDATE用于修改表中已有数据，同样属于DML。
【易错提示】
注意区分SQL语句的分类：SELECT是查询（DQL），INSERT/UPDATE/DELETE是数据操纵（DML），CREATE/ALTER是数据定义（DDL）。面试中常考这些基础概念。
```

---

## Q006619

- 题型：单选
- 难度：入门

**题目**

```text
以下SQL语句中的where条件表达式相匹配的是（ ）
```

**选项**

```text
A. 20>=age>=40
B. age>=20 and age<=40
C. age>20 and age<40
D. 20>age>40
```

**答案**

```text
B
```

**正确选项**

```text
B. age>=20 and age<=40
```

**解析**

```text
【核心考点】 SQL语法 条件表达式
【题目解析】
本题考查SQL中WHERE条件表达式的正确写法。年龄范围通常表示为age >= 20 AND age 【选项解析】
✗ A. 20>=age>=40 — 错误。SQL不支持连续比较，且逻辑上20>=age>=40永远为假。
✓ B. age>=20 and age✗ C. age>20 and age✗ D. 20>age>40 — 错误。语法无效，且逻辑上20>age>40永远为假。
【易错提示】
注意SQL中区间表示必须使用AND连接两个独立条件，不能像数学中写连续不等式。同时注意边界值是否包含（>= vs >）。
```

---

## Q006621

- 题型：简答
- 难度：入门

**题目**

```text
以前有用过数据库吗？用的是哪种数据库？利用数据库进行过哪些操作？修改命令是什么？
```

**答案**

```text
1、用过，用的是MySQL数据库；
2、 利用数据做过增删改查操作；
3、主要是查询最多，包括单表查询和多表查询，以及左连接、右连接等；

4、修改的话主要包括两种情况，修改表结构以及修改表数据：

我写脚本来改表结构比较少，一般是通过客户端的设计表功能直接去修改
```

**解析**

```text
【核心考点】 数据库基础 SQL操作 MySQL
【题目解析】
本题考查数据库的基本使用经验，属于基础面试题。回答需明确使用的数据库类型（如MySQL），并列举常用操作：增删改查（CRUD），特别是查询操作（单表查询、多表查询、连接查询），以及修改操作（修改表结构如ALTER TABLE，修改表数据如UPDATE）。
【参考答案要点】
1. 数据库类型：MySQL。
2. 常用操作：增删改查，其中查询最多，包括单表查询、多表查询、左连接、右连接等。
3. 修改命令：修改表结构使用ALTER TABLE（如ALTER TABLE table_name ADD column_name datatype），修改表数据使用UPDATE（如UPDATE table_name SET column_name = value WHERE condition）。
【易错提示】
注意区分修改表结构（ALTER）和修改表数据（UPDATE），面试中可能要求写出具体SQL语句。
【面试角度】
回答时建议结合实际项目中的数据库操作，例如“在测试中，我常用SELECT语句验证数据正确性，用UPDATE修改测试数据”，体现实际应用能力。
```

---

## Q006623

- 题型：组合
- 难度：入门
- 答案：AI 补全（原数据缺失文字答案）

**题目**

```text
创建学生表并编写SQL
```

**答案**

```text
CREATE TABLE student (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  gender ENUM('男','女') DEFAULT '男',
  age INT CHECK (age BETWEEN 1 AND 150),
  class_name VARCHAR(50),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
-- 插入数据
INSERT INTO student(name, gender, age, class_name) VALUES ('张三','男',20,'测试1班');
-- 查询
SELECT * FROM student WHERE class_name = '测试1班';
-- 更新
UPDATE student SET age = 21 WHERE id = 1;
-- 删除
DELETE FROM student WHERE id = 1;
```

**解析**

```text
【核心考点】SQL DDL、DML、约束与索引
【题目解析】本题考查建表语句和常用增删改查操作，重点是把字段类型、主键、非空、默认值、检查约束写完整。
【答题要点】
1. 建表时先确定主键，再按业务选择合适的数据类型和约束。
2. 插入、查询、更新、删除分别对应 INSERT、SELECT、UPDATE、DELETE。
3. 实际项目还要考虑索引、事务和权限，避免全表扫描和误删。
【面试提示】先写出可执行的建表语句，再补一条查询或更新语句，最后说明约束和索引的作用。
```

---

## Q006624

- 题型：单选
- 难度：入门

**题目**

```text
在SQL语言中授权的操作是通过什么语句实现的？（ ）
```

**选项**

```text
A. create
B. revoke
C. grant
D. insert
```

**答案**

```text
C
```

**正确选项**

```text
C. grant
```

**解析**

```text
【核心考点】 SQL语言 授权语句
【题目解析】
本题考查SQL中用于授权操作的语句。在SQL中，GRANT语句用于授予用户或角色权限，REVOKE用于撤销权限。
【选项解析】
✗ A. CREATE — 错误。CREATE用于创建数据库对象（如表、索引）。
✗ B. REVOKE — 错误。REVOKE用于撤销权限，与授权相反。
✓ C. GRANT — 正确。GRANT用于授予权限，是授权操作。
✗ D. INSERT — 错误。INSERT用于插入数据，属于DML语句。
【易错提示】
注意区分GRANT（授权）和REVOKE（撤销权限），两者是相反操作，面试中常成对出现。
```

---

## Q006626

- 题型：单选
- 难度：入门

**题目**

```text
在sql语言的select语句中，用于对结果进行排序的是哪个字句？（）
```

**选项**

```text
A. Group BY
B. HAVING
C. ORDER BY
D. Where
```

**答案**

```text
C
```

**正确选项**

```text
C. C、ORDER BY
```

**解析**

```text
【核心考点】 SQL语法 SELECT语句
【题目解析】
本题考查SQL SELECT语句中用于排序的子句。ORDER BY子句用于对查询结果按指定列进行升序（ASC）或降序（DESC）排序。
【选项解析】
✓ C. ORDER BY — 正确。ORDER BY是SQL中唯一用于排序的子句。
✗ A. GROUP BY — 错误。GROUP BY用于分组聚合，常与HAVING配合使用。
✗ B. HAVING — 错误。HAVING用于过滤分组后的结果，类似WHERE但作用于组。
✗ D. WHERE — 错误。WHERE用于在分组前过滤行记录。
【易错提示】
注意ORDER BY默认升序（ASC），降序需显式指定DESC。面试中常考ORDER BY与GROUP BY的执行顺序：先WHERE过滤，再GROUP BY分组，然后HAVING过滤组，最后ORDER BY排序。
```

---

## Q006630

- 题型：简答
- 难度：入门

**题目**

```text
数据库倒序怎么写？
```

**答案**

```text
在sql语句当中，使用order by关键字排序 ，然后使用ASC作降序排序。
```

**解析**

```text
【核心考点】 SQL排序 ORDER BY子句
【参考答案要点】
1. 基本语法：使用 ORDER BY 子句对查询结果排序。
2. 倒序（降序）：使用 DESC 关键字，例如：SELECT * FROM table_name ORDER BY column_name DESC。
3. 升序：使用 ASC 关键字（默认），例如：SELECT * FROM table_name ORDER BY column_name ASC。
【面试角度】
回答时需注意区分 ASC 和 DESC，原答案中“使用ASC作降序排序”是错误的，ASC 表示升序，DESC 才是降序。同时可补充多列排序语法：ORDER BY col1 DESC, col2 ASC。
【易错提示】
常见错误：混淆 ASC 和 DESC 的功能，以及忘记 ORDER BY 子句的位置（必须放在 WHERE 和 GROUP BY 之后）。
```

---

## Q006632

- 题型：简答
- 难度：入门

**题目**

```text
数据库按组分类怎么写？
```

**答案**

```text
在sql语句中，使用group by进行分组，如果有条件分组，则再加上having
```

**解析**

```text
【核心考点】 SQL分组查询 GROUP BY HAVING
【参考答案要点】
使用 GROUP BY 子句对查询结果按指定列进行分组，常与聚合函数（如 COUNT, SUM, AVG）配合使用。如果需要对分组后的结果进行条件过滤，则使用 HAVING 子句，而不是 WHERE（WHERE 用于分组前过滤）。
示例：
SELECT department, COUNT(*) as employee_count FROM employees GROUP BY department HAVING COUNT(*) > 10;
【面试角度】
面试中常问WHERE 和 HAVING 的区别：WHERE 在分组前过滤行，HAVING 在分组后过滤组。建议通过具体例子说明。
```

---

## Q006633

- 题型：简答
- 难度：入门

**题目**

```text
查数据库符合条件的10条数据怎么做
```

**答案**

```text
在sql最后面使用limit 10
```

**解析**

```text
【核心考点】 SQL查询 LIMIT子句
【题目解析】
在SQL中，使用LIMIT子句可以限制查询结果返回的行数。语法为：SELECT * FROM 表名 WHERE 条件 LIMIT 数量; 例如，查询符合条件的10条数据，在SQL语句末尾添加LIMIT 10即可。
【参考答案要点】
示例：SELECT * FROM users WHERE age > 18 LIMIT 10;
【易错提示】
注意LIMIT子句的位置，通常放在WHERE和ORDER BY之后。不同数据库可能支持不同的分页语法（如MySQL的LIMIT，SQL Server的TOP）。
```

---

## Q006610

- 题型：简答
- 难度：简单

**题目**

```text
SQL 中常用的聚合函数都有哪些？
```

**答案**

```text
max()：最大值
min()：最小值
avg()：平均值
sum()：求和
count()：统计总数

以下是一个综合案例帮助你更好的理解这些聚合函数的用法：
SQL聚合函数综合案例：电商平台数据分析
案例背景：电商订单数据分析
假设我们需要测试一个电商平台的订单数据统计功能，验证各种聚合函数计算结果的正确性。
测试数据准备
首先创建订单表并插入测试数据：
sql
CREATE TABLE orders (
order_id INT PRIMARY KEY,
user_id INT,
product_id INT,
product_name VARCHAR(50),
category VARCHAR(20),
price DECIMAL(10,2),
quantity INT,
order_date DATE,
payment_status VARCHAR(20)
);

-- 插入测试数据
INSERT INTO orders VALUES
(1001, 101, 1, '智能手机', '电子产品', 5999.00, 1, '2023-01-15', '已支付'),
(1002, 102, 2, '无线耳机', '电子产品', 399.00, 2, '2023-01-16', '已支付'),
(1003, 101, 3, '运动鞋', '服装', 299.00, 1, '2023-01-17', '已退款'),
(1004, 103, 4, '笔记本电脑', '电子产品', 8999.00, 1, '2023-01-18', '已支付'),
(1005, 104, 5, 'T恤', '服装', 99.00, 3, '2023-01-19', '已支付'),
(1006, 102, 2, '无线耳机', '电子产品', 399.00, 1, '2023-01-20', '已支付'),
(1007, 105, 6, '智能手表', '电子产品', 1299.00, 1, '2023-01-21', '待支付'),
(1008, 101, 7, '牛仔裤', '服装', 199.00, 2, '2023-01-22', '已支付');

常用聚合函数应用示例
1. COUNT() - 统计订单数量
sql
-- 统计总订单数（测试订单总数）
SELECT COUNT(*) AS total_orders FROM orders;

-- 统计已支付的订单数（测试支付成功率）
SELECT COUNT(*) AS paid_orders
FROM orders
WHERE payment_status = '已支付';

-- 统计不同用户的下单数量（测试用户活跃度）
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id;

2. SUM() - 计算销售总额
sql
-- 计算所有订单总金额（测试销售总额）
SELECT SUM(price * quantity) AS total_sales FROM orders;

-- 按分类计算销售总额（测试各类商品表现）
SELECT category, SUM(price * quantity) AS category_sales
FROM orders
GROUP BY category;

-- 计算用户101的总消费金额（测试用户价值）
SELECT SUM(price * quantity) AS user_total_spent
FROM orders
WHERE user_id = 101;

3. AVG() - 计算平均订单金额
sql
-- 计算平均订单金额（测试订单质量）
SELECT AVG(price * quantity) AS avg_order_value FROM orders;

-- 按用户计算平均订单金额（测试用户消费水平）
SELECT user_id, AVG(price * quantity) AS avg_order_value
FROM orders
GROUP BY user_id;

4. MAX()/MIN() - 查找最高/最低订单
sql
-- 查找最高单价订单（测试价格上限）
SELECT MAX(price) AS max_price FROM orders;

-- 查找最低单价订单（测试价格下限）
SELECT MIN(price) AS min_price FROM orders;

-- 查找每个用户的最大订单金额（测试用户消费能力）
SELECT user_id, MAX(price * quantity) AS max_order_value
FROM orders
GROUP BY user_id;

5. GROUP_CONCAT() - 合并显示相关订单
sql
-- 显示每个用户购买的所有产品（测试用户购买行为）
SELECT
user_id,
GROUP_CONCAT(product_name ORDER BY order_date SEPARATOR ' → ') AS products_ordered
FROM orders
GROUP BY user_id;

-- 显示每个分类下的所有产品（测试商品分布）
SELECT
category,
GROUP_CONCAT(DISTINCT product_name SEPARATOR ', ') AS products_in_category
FROM orders
GROUP BY category;

综合应用案例
场景：生成电商平台月度销售报告
sql
SELECT
category,
COUNT(*) AS order_count,
SUM(quantity) AS total_items_sold,
SUM(price * quantity) AS total_sales,
AVG(price * quantity) AS avg_order_value,
MAX(price * quantity) AS max_order_value,
MIN(price * quantity) AS min_order_value,
GROUP_CONCAT(DISTINCT product_name SEPARATOR ' | ') AS products_available
FROM orders
WHERE order_date BETWEEN '2023-01-01' AND '2023-01-31'
AND payment_status = '已支付'
GROUP BY category
ORDER BY total_sales DESC;

测试验证点：
• 各分类订单数量是否正确
• 销售总额计算是否准确
• 平均订单金额是否合理
• 最高/最低订单值是否符合预期
• 合并显示的产品列表是否完整

测试工程师实践建议
• 边界测试：
• 测试空表时的聚合结果
• 测试只有一条记录时的聚合结果
• 测试包含NULL值时的处理

• 性能测试：
sql
-- 测试大数据量下的聚合查询性能
EXPLAIN ANALYZE SELECT category, AVG(price) FROM orders GROUP BY category;

• 数据一致性验证：
sql
-- 验证前端展示的统计数据与数据库计算结果是否一致
SELECT COUNT(*) AS backend_count FROM orders;
-- 与前端显示的"总订单数"对比

• 异常情况测试：
sql
-- 测试退款订单是否被正确排除
SELECT SUM(price * quantity) FROM orders WHERE payment_status != '已退款';

这个综合案例涵盖了SQL主要聚合函数的实际应用，通过电商业务场景展示如何设计测试数据和验证聚合计算结果的正确性，既简单易懂又具有实际参考价值。
```

**解析**

```text
【核心考点】 SQL聚合函数 数据库查询
【题目解析】
本题考察SQL聚合函数的基础知识，是数据库测试和数据分析中的常用技能。回答需列出常用函数并简要说明用途。
【参考答案要点】
1. COUNT()：统计行数，如SELECT COUNT(*) FROM orders;。
2. SUM()：计算数值列的总和，如SELECT SUM(amount) FROM orders;。
3. AVG()：计算数值列的平均值，如SELECT AVG(price) FROM products;。
4. MAX()：返回最大值，如SELECT MAX(salary) FROM employees;。
5. MIN()：返回最小值，如SELECT MIN(age) FROM students;。
6. GROUP_CONCAT()（MySQL）：将分组内字符串连接，如SELECT GROUP_CONCAT(name) FROM users GROUP BY city;。
【面试角度】
面试官可能进一步追问聚合函数与GROUP BY的结合使用，以及HAVING子句的用法。建议准备一个综合案例，如统计每个部门的平均薪资并筛选出高于5000的部门。
【易错提示】
注意聚合函数忽略NULL值，但COUNT(*)会包含NULL行。另外，聚合函数不能直接出现在WHERE子句中，需使用HAVING。
```

---

## Q006613

- 题型：简答
- 难度：简单

**题目**

```text
Users用户注册表数据如下：

写一个SQL查询，找出最近30天内注册用户。
```

**答案**

```text
查询最近 30 天内注册的用户
假设当前日期为 2023-10-20，查询最近 30 天内注册的用户：
sql

SELECT id, 昵称, 注册时间
FROM Users
WHERE 注册时间 >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);

查询结果

查询逻辑说明
• CURDATE() 函数：• 获取当前日期（假设为 2023-10-20）。

• DATE_SUB 函数：• DATE_SUB(CURDATE(), INTERVAL 30 DAY) 表示从当前日期往前推 30 天，结果为 2023-09-20。

• WHERE 条件：• 筛选出 注册时间 大于等于 2023-09-20 的用户。
```

**解析**

```text
【核心考点】 SQL查询 日期函数 数据筛选
【参考答案要点】
假设当前日期为2023-10-20，查询最近30天内注册的用户：
SQL语句：
SELECT id, 昵称, 注册时间 FROM Users WHERE 注册时间 >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
查询逻辑说明：
1. CURDATE()函数：获取当前日期（如2023-10-20）。
2. DATE_SUB函数：DATE_SUB(CURDATE(), INTERVAL 30 DAY)表示从当前日期往前推30天，结果为2023-09-20。
3. WHERE条件：筛选出注册时间大于等于2023-09-20的记录，即最近30天内注册的用户。
【面试角度】
回答时建议结合实际项目场景，例如“在用户分析报表中，我们常用此类查询统计活跃用户”，能体现SQL应用能力。
【延伸知识】
还可使用DATE_ADD或INTERVAL的负值实现相同效果，或使用BETWEEN语句，展示SQL灵活性。
```

---

## Q006614

- 题型：简答
- 难度：简单

**题目**

```text
sql对数据去重的脚本怎么写
```

**答案**

```text
1、DISTINCT
2、GROUP BY
3、ROW_NUMBER() ， 取排序为1
```

**解析**

```text
【核心考点】 SQL去重 数据查询
【题目解析】
本题考查SQL中数据去重的常见方法。答案给出了三种方式：DISTINCT、GROUP BY和ROW_NUMBER()窗口函数。
【参考答案要点】
1. DISTINCT：直接对查询结果去重，适用于简单场景。例如：SELECT DISTINCT column FROM table。
2. GROUP BY：通过分组实现去重，常用于聚合查询。例如：SELECT column FROM table GROUP BY column。
3. ROW_NUMBER()：窗口函数，按某字段排序后取第一条，适用于保留重复记录中特定一条的场景。例如：SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY column ORDER BY id) AS rn FROM table) WHERE rn = 1。
【面试角度】
回答时建议结合实际需求，例如“在用户表中去重时，使用DISTINCT快速获取唯一城市列表；而删除重复数据时，常用ROW_NUMBER()配合DELETE”，体现对不同场景的理解。
【易错提示】
DISTINCT作用于所有选择列，如果多列组合去重，需确保所有列都相同。GROUP BY在非聚合查询中可能返回任意行，需谨慎使用。
```

---

## Q006616

- 题型：简答
- 难度：简单
- 答案：AI 补全（原数据缺失文字答案）

**题目**

```text
什么是内连接？以及语法是什么?
```

**答案**

```text
1. 内连接定义：内连接（INNER JOIN）是SQL中最常用的连接类型，它返回两个表中满足连接条件的匹配行。如果某行在另一个表中没有匹配，则该行不会出现在结果集中。
2. 语法：SELECT 列名 FROM 表1 INNER JOIN 表2 ON 表1.列 = 表2.列; 其中INNER JOIN可以简写为JOIN，ON后面指定连接条件。
3. 示例：SELECT e.name, d.department_name FROM employees e INNER JOIN departments d ON e.department_id = d.id; 该查询返回所有有部门的员工及其部门名称。
```

**解析**

```text
【核心考点】 SQL连接查询 内连接
【参考答案要点】
1. 内连接定义：内连接（INNER JOIN）是SQL中最常用的连接类型，它返回两个表中满足连接条件的匹配行。如果某行在另一个表中没有匹配，则该行不会出现在结果集中。
2. 语法：SELECT 列名 FROM 表1 INNER JOIN 表2 ON 表1.列 = 表2.列; 其中INNER JOIN可以简写为JOIN，ON后面指定连接条件。
3. 示例：SELECT e.name, d.department_name FROM employees e INNER JOIN departments d ON e.department_id = d.id; 该查询返回所有有部门的员工及其部门名称。
【面试角度】
回答时建议补充内连接与左连接、右连接的区别，以及内连接在性能优化中的注意事项（如索引使用），体现对SQL查询的深入理解。
【易错提示】
注意内连接与自然连接（NATURAL JOIN）的区别：自然连接自动基于同名列连接，而内连接需要显式指定条件；另外，内连接只返回匹配行，不匹配的行会被过滤掉。
```

---

## Q006617

- 题型：简答
- 难度：简单
- 答案：AI 补全（原数据缺失文字答案）

**题目**

```text
什么是数据库的交叉连接(完全连接)？
```

**答案**

```text
定义：交叉连接（CROSS JOIN）是数据库连接的一种，返回两个表的笛卡尔积，即所有可能的行组合。
语法：SELECT * FROM 表1 CROSS JOIN 表2; 或 SELECT * FROM 表1, 表2;
特点：无连接条件，结果行数为两表行数乘积，常用于生成测试数据或枚举组合。
```

**解析**

```text
【核心考点】 数据库连接 交叉连接
【题目解析】
本题考查数据库连接操作中的交叉连接（CROSS JOIN），也称为笛卡尔积。交叉连接会返回两个表中所有行的组合，即左表的每一行与右表的每一行配对，结果集行数为左表行数乘以右表行数。它没有ON条件，通常用于生成组合数据或测试场景，但在实际应用中需谨慎使用，避免产生大量无用数据。
【参考答案要点】
定义：交叉连接（CROSS JOIN）是数据库连接的一种，返回两个表的笛卡尔积，即所有可能的行组合。
语法：SELECT * FROM 表1 CROSS JOIN 表2; 或 SELECT * FROM 表1, 表2;
特点：无连接条件，结果行数为两表行数乘积，常用于生成测试数据或枚举组合。
【易错提示】
交叉连接与内连接（INNER JOIN）容易混淆，内连接需要ON条件筛选匹配行，而交叉连接无条件，面试中常通过对比考察理解深度。
```

---

## Q006618

- 题型：简答
- 难度：简单

**题目**

```text
介绍下union和union all的区别 ?
```

**答案**

```text
使用建议
• 当需要去除重复记录时使用 UNION
• 当确定结果不会有重复或需要保留重复记录时使用 UNION ALL（性能更好）
• 当需要排序时，建议在外部查询中使用ORDER BY，而不是依赖UNION的默认排序
```

**解析**

```text
【核心考点】 SQL基础 集合操作
【题目解析】
本题考察SQL中UNION和UNION ALL的区别，是数据库面试的经典问题。两者都用于合并多个SELECT语句的结果集，但处理重复记录的方式不同。
【参考答案要点】
1. UNION： 自动去除重复行，相当于执行SELECT DISTINCT操作，性能相对较低。
2. UNION ALL： 保留所有行，包括重复行，性能更高。
使用建议：
- 需要去重时使用UNION。
- 确定无重复或需要保留重复时使用UNION ALL。
- 排序建议在外部查询中使用ORDER BY，而非依赖UNION的默认排序。
【面试角度】
面试常问：UNION和JOIN的区别？UNION对性能的影响？建议结合执行计划说明去重操作的开销。
【易错提示】
注意UNION要求各SELECT语句的列数和数据类型必须匹配；ORDER BY应放在最后一个SELECT之后，否则语法错误。
```

---

## Q006625

- 题型：单选
- 难度：简单

**题目**

```text
在SQL语言中，（）子句能够实现关系参照性规则
```

**选项**

```text
A. PRIMARY KEY
B. NUT NULL
C. POREIGN KEY
D. FOREIGN KEY...REFERENCES...
```

**答案**

```text
D
```

**正确选项**

```text
D. FOREIGN KEY...REFERENCES...
```

**解析**

```text
【核心考点】 SQL 参照完整性 外键约束
【题目解析】
本题考查SQL中实现关系参照性规则的子句。参照完整性通过外键（FOREIGN KEY）约束实现，确保子表的外键值必须在主表的主键中存在，或为NULL。语法为：FOREIGN KEY (子表列) REFERENCES 主表(主键列)。
【选项解析】
✗ A. PRIMARY KEY — 错误。PRIMARY KEY用于定义主键，保证实体完整性，而非参照完整性。
✗ B. NOT NULL — 错误。NOT NULL约束字段不能为空，与参照完整性无关。
✗ C. FOREIGN KEY — 错误。单独FOREIGN KEY不完整，缺少REFERENCES指定引用表。
✓ D. FOREIGN KEY...REFERENCES... — 正确。完整语法，如FOREIGN KEY (dept_id) REFERENCES departments(id)，实现参照完整性。
【易错提示】
注意FOREIGN KEY必须与REFERENCES配合使用，单独使用FOREIGN KEY是语法错误。同时区分主键（PRIMARY KEY）和外键（FOREIGN KEY）的不同作用。
```

---

## Q006627

- 题型：简答
- 难度：简单

**题目**

```text
数据库下指定某列值唯一
```

**答案**

```text
unique 或者设置为主键
```

**解析**

```text
【核心考点】 数据库约束 唯一性
【参考答案要点】
方法一：使用UNIQUE约束
在创建表时或通过ALTER TABLE添加UNIQUE约束，确保列值唯一。例如：CREATE TABLE t (col INT UNIQUE);
方法二：设置为主键
主键自动保证唯一性，但一张表只能有一个主键。例如：CREATE TABLE t (col INT PRIMARY KEY);
【面试角度】
面试中常考察UNIQUE与主键的区别：主键非空且唯一，UNIQUE允许空值（视数据库而定）。
【延伸知识】
也可使用唯一索引实现唯一性，但约束更常用。
```

---

## Q006635

- 题型：简答
- 难度：简单

**题目**

```text
聚合函数是否可以跟分组一起使用？
```

**答案**

```text
可以一起使用。在分组完成之后，可以使用max，sum, avg等函数对分组后的结果进行计算
```

**解析**

```text
【核心考点】 SQL聚合函数 GROUP BY子句
【题目解析】
本题考查SQL中聚合函数与GROUP BY子句的配合使用。聚合函数如MAX、SUM、AVG等用于对一组值执行计算并返回单个值，而GROUP BY用于将结果集按一个或多个列进行分组。两者结合使用是SQL查询的常见模式，用于对每个分组进行统计计算。
【参考答案要点】
可以一起使用。在分组完成之后，可以使用MAX、SUM、AVG等聚合函数对分组后的结果进行计算。例如：SELECT department, AVG(salary) FROM employees GROUP BY department; 该语句按部门分组，并计算每个部门的平均工资。
【易错提示】
注意：如果SELECT子句中包含非聚合列，则该列必须出现在GROUP BY子句中，否则会导致语法错误。同时，WHERE子句在分组前过滤数据，HAVING子句在分组后过滤分组结果。
```

---

## Q006620

- 题型：单选
- 难度：中等

**题目**

```text
以下哪种约束不能在表级进行定义？
```

**选项**

```text
A. Unique
B. Not Null
C. Check
D. Primary K
```

**答案**

```text
B
```

**正确选项**

```text
B. Not Null
```

**解析**

```text
【核心考点】 数据库约束 表级约束
【题目解析】
本题考查SQL中约束的定义级别。表级约束可以定义在多个列上，如复合主键、复合唯一键、外键等；列级约束只能定义在单个列上。Not Null约束只能作为列级约束，不能在表级定义。
【选项解析】
✗ A. Unique — 错误。Unique既可作为列级约束也可作为表级约束（复合唯一）。
✓ B. Not Null — 正确。Not Null只能定义在列级，不能用于表级。
✗ C. Check — 错误。Check约束在表级和列级均可定义。
✗ D. Primary Key — 错误。主键可在列级或表级定义（复合主键）。
【易错提示】
容易混淆Not Null与Unique，注意Not Null是唯一不能作为表级约束的常用约束，面试中常作为陷阱题出现。
```

---

## Q006622

- 题型：简答
- 难度：中等
- 解析：AI 补全（原数据缺失解析）

**题目**

```text
会不会删除脏数据，我说delete方法或者写一条sql语句
```

**答案**

```text
可以通过写好的数据库工具类去实现，主要是通过JDBC技术操作数据库实现删除脏数据
```

**解析**

```text
【核心考点】脏数据的删除方式与操作规范。
【题目解析】可以通过数据库工具类，基于 JDBC 连接数据库执行 DELETE 语句，按明确条件删除脏数据；也可直接执行 SQL。例如先查出目标记录，确认条件无误后再删除。操作前应备份、在事务中执行，并核对影响行数。
【答题要点】
1. 删除条件必须精确，避免误删全表。
2. 优先在测试环境验证，生产操作需审批和备份。
3. 通过影响行数和复查结果确认删除效果。
【面试提示】回答时强调数据安全，比只说 delete 方法更能体现工程素养。
```

---

## Q006628

- 题型：简答
- 难度：中等

**题目**

```text
数据库中drop、delete、truncate三者的区别？
```

**答案**

```text
核心区别对比表

测试工程师的专业回答框架
"在测试工作中，我们需要根据不同的测试场景选择合适的删除操作：
• DELETE：
• 测试重点：验证条件删除的正确性、事务回滚机制
• 测试用例举例：sql
复制
BEGIN TRANSACTION;
DELETE FROM users WHERE status = 'inactive';
-- 验证受影响行数是否正确
ROLLBACK; -- 验证数据是否恢复

• 适用场景：需要精确删除特定数据的测试用例

• TRUNCATE：
• 测试重点：验证表重置后的初始状态
• 测试用例举例：sql
TRUNCATE TABLE audit_logs;
-- 验证表是否为空且自增ID重置

• 适用场景：测试环境快速清理数据，性能测试前的数据准备

• DROP：
• 测试重点：验证表删除后的依赖关系
• 测试用例举例：sql
复制
DROP TABLE temp_data;
-- 验证相关视图、存储过程是否失效

• 适用场景：测试数据库迁移或重构时的表删除操作

从测试角度，我们特别关注：
• 数据恢复测试：DELETE可回滚的特性对数据安全很重要
• 性能影响：大批量数据清理时TRUNCATE比DELETE高效得多
• 关联影响：DROP表后需要验证外键约束和依赖对象
• 权限控制：测试不同账号对这3种操作的执行权限"

实际测试场景示例
场景1：测试用户数据清理功能
sql
-- 测试精确删除（应使用DELETE）
DELETE FROM users WHERE last_login < '2020-01-01';
-- 验证：1. 符合条件的数据是否被删除 2. 事务回滚是否有效

-- 错误做法（TRUNCATE会清空全部数据）
TRUNCATE TABLE users;

场景2：准备性能测试环境
sql
-- 快速清空测试数据（TRUNCATE更合适）
TRUNCATE TABLE performance_test_data;
-- 比DELETE FROM performance_test_data快10倍以上

-- 错误做法（DROP会丢失表结构）
DROP TABLE performance_test_data;

场景3：测试表删除的连锁反应
sql
-- 测试表删除影响（应使用DROP）
DROP TABLE products;
-- 验证：1. 关联的订单表外键约束 2. 相关报表是否报错

回答示例
"DELETE、TRUNCATE和DROP是三种不同层级的删除操作。DELETE是行级删除，可回滚，适合精确数据清理；TRUNCATE是表级清空，不可回滚但性能高，适合测试环境重置；DROP是对象级删除，会移除整个表结构。作为测试工程师，我们需要根据测试目的选择合适的方式，比如测试数据恢复功能要用DELETE，准备性能测试环境可用TRUNCATE，而测试表删除的依赖影响则用DROP。同时要验证每种操作对数据完整性、关联对象和系统性能的影响。"
这样的回答既展示了技术理解，又体现了测试思维，能够有效展现测试工程师的专业价值。
```

**解析**

```text
【核心考点】 数据库操作 SQL语句
【参考答案要点】
DELETE：删除表中的行，可带WHERE条件，支持事务回滚，删除后表结构不变，自增ID不重置。
TRUNCATE：删除表中所有行，不能带WHERE条件，不支持事务回滚（部分数据库支持），重置自增ID，释放存储空间。
DROP：删除整个表（包括结构和数据），不可回滚，释放所有资源。
【测试角度】
DELETE测试：验证条件删除的正确性、事务回滚机制。例如：BEGIN TRANSACTION; DELETE FROM users WHERE status='inactive'; ROLLBACK; 验证数据恢复。
TRUNCATE测试：验证表重置后的初始状态。例如：TRUNCATE TABLE audit_logs; 验证表是否为空且自增ID重置。
【易错提示】
注意TRUNCATE在某些数据库中（如MySQL）不可回滚，而DELETE可以。面试中常考察事务隔离级别对DELETE的影响。
```

---

## Q006629

- 题型：单选
- 难度：中等

**题目**

```text
数据库中有两个用户scott和muuser，物资表wz是属于myuser用户的，但当前用户是scott，要求查询：物资表wz（wno，wname，wtype，wunit）物资单位wunit列为null的记录，取结果的前5条记录显示以下正确的SQL语句是（ ）
```

**选项**

```text
A. select*from scott.wz where wunit is null anrownum<5；
B. select*from myuser.wz where wunit = null anrownum<5；
C. select*from myuser.wz where wunit is null anrownum<6；
D. select*form scott.wz where wunit is null anrownum<6；
```

**答案**

```text
C
```

**正确选项**

```text
C. select*from myuser.wz where wunit is null anrownum<6；
```

**解析**

```text
【核心考点】 SQL查询 空值判断 跨用户访问
【题目解析】
当前用户为scott，需要访问myuser用户的wz表，必须使用用户名.表名格式。空值判断应使用IS NULL而非= NULL。取前5条记录需用ROWNUM 【选项解析】
✗ A. select*from scott.wz where wunit is null anrownum✗ B. select*from myuser.wz where wunit = null anrownum✓ C. select*from myuser.wz where wunit is null anrownum✗ D. select*form scott.wz where wunit is null anrownum【易错提示】
注意Oracle中ROWNUM的使用：取前N条需用ROWNUM <= N，而非ROWNUM < N+1（虽然本题中<6等价于<=5）。同时跨用户访问必须加用户名前缀。
```

---

## Q006631

- 题型：简答
- 难度：中等

**题目**

```text
数据库增删改查语法的使用都知道么？Group by和order by区别？Drop和delete的区别？怎么插入部分字段的数据？
```

**答案**

```text
1）增删改查基本都会用；包括单表查询 多表关联查询，左连接 右链接等

2）Group by是分组，一般需要进行一些数据统计的时候，比如一个群体里最大的 总数 数量 平均数等 都会用到分组；
order by是排序，就按照升序或者降序排列的；两个如果要一起使用的话，先分组后排序，先groupby，后order by。

3）Drop和delete 都是删除数据库的数据的命令，但是drop会删除表、库的结构，delete不会删除表的结构，只会删除里面的数据-更安全一些
4) 插入部分字段的数据语法： insert into <表名>(字段A,字段B,字段C) values ( 值A,值B,值C);
```

**解析**

```text
【核心考点】 SQL基础语法 Group by与Order by Drop与Delete
【参考答案要点】
1. 增删改查：INSERT、DELETE、UPDATE、SELECT语句的基本使用，包括单表查询、多表关联查询（INNER JOIN、LEFT JOIN、RIGHT JOIN）。
2. Group by与Order by区别：Group by用于分组聚合（如COUNT、SUM、AVG），Order by用于排序（ASC升序、DESC降序）。同时使用时，先Group by后Order by。
3. Drop与Delete区别：Drop删除表或数据库的结构（DDL），不可回滚；Delete删除表中的数据（DML），可回滚，不删除表结构。
4. 插入部分字段：语法：INSERT INTO 表名 (字段A, 字段B) VALUES (值A, 值B);
【面试角度】
回答时建议举例说明实际应用场景，例如“统计每个部门的平均工资用Group by，按工资降序排列用Order by”。体现对SQL语法的灵活运用。
【延伸知识】
面试中常问的进阶点：HAVING子句（对分组结果过滤）、TRUNCATE（快速删除数据但不可回滚）、以及索引对查询性能的影响。
```

---

## Q006634

- 题型：简答
- 难度：中等

**题目**

```text
根据题目要求写出具体SQL语句表A：表B：1、将所有男生的性别修改成01；2、根据分数上下限设置表A的是否及格列（优秀、良好、及格都表示及格）以及评价列
```

**答案**

```text
1、update 表A set 性别=01 where 性别=“男”；
2、Update A a inner join B b on a.分数>=b.分数下限 and a.分数<=b.分数上限 set 评价
```

**解析**

```text
【核心考点】 SQL数据更新 多表关联更新
【参考答案要点】
1. 修改性别字段：UPDATE 表A SET 性别='01' WHERE 性别='男';
2. 根据分数范围更新评价：UPDATE 表A a INNER JOIN 表B b ON a.分数 BETWEEN b.分数下限 AND b.分数上限 SET a.是否及格='及格', a.评价=b.评价;
【面试角度】
回答时需注意：第一题使用条件更新，第二题使用JOIN关联更新，并考虑字段类型（如性别可能为字符或数字）。建议补充说明如果表B中分数范围有重叠时的处理策略。
【延伸知识】
多表更新也可用子查询实现：UPDATE 表A SET 评价=(SELECT 评价 FROM 表B WHERE 分数 BETWEEN 分数下限 AND 分数上限)，但JOIN方式更高效，面试中常考察两种写法。
```

---

## Q006636

- 题型：简答
- 难度：较难

**题目**

```text
表1病人基本信息表\n表名：his_patient （病人编码、病人姓名、年龄、身高、体重、科室编码、科室名称）

表2：病人药品费用表\n表名:his_drugeost （病人编码、药品编码、药品名称、剂型、规格、划价单位、划价数量、费用）

根据以上表结构关系，要求只用一条SQL语句实现下列数据查询功能：\n查询每个病人的药品总费用，查询结果中显示病人姓名、科室名称、每个病人药品总费用，并按科室排序。
```

**答案**

```text
查询SQL及结果说明
sql
复制
SELECT
p.patName AS '病人姓名',
p.dptName AS '科室名称',
SUM(d.cost) AS '药品总费用'
FROM
his_patient p
JOIN
his_drugeost d ON p.patCade = d.patCade
GROUP BY
p.patCade, p.patName, p.dptName
ORDER BY
p.dptName;

查询结果：

SQL说明：
• 通过JOIN连接两个表，关联条件是病人编码(patCade)
• 使用GROUP BY按病人分组，计算每个病人的药品总费用(SUM(d.cost))
• 在SELECT子句中显示病人姓名、科室名称和计算出的总费用
• 最后按科室名称(dptName)排序结果

结果说明：
• 朱宏(内一科)的总药品费用为150+200=350元
• 林田(内一科)的总药品费用为120+60=180元
• 张彤(门诊)的总药品费用为48+26+5.5=79.5元
• 结果按科室名称排序，内一科在前，门诊在后
```

**解析**

```text
【核心考点】 SQL查询 JOIN连接 GROUP BY聚合
【参考答案要点】
查询SQL：
SELECT p.patName AS '病人姓名', p.dptName AS '科室名称', SUM(d.cost) AS '药品总费用' FROM his_patient p JOIN his_drugeost d ON p.patCade = d.patCade GROUP BY p.patCade, p.patName, p.dptName ORDER BY p.dptName;
说明：通过JOIN连接两个表，关联条件是病人编码(patCade)；使用GROUP BY按病人分组，计算每个病人的药品总费用(SUM(d.cost))；最后按科室名称排序。
【面试角度】
回答时建议强调SQL优化，例如“使用JOIN代替子查询可提高性能”，并注意字段名一致性（如patCade与patCode的差异）。
【易错提示】
注意GROUP BY子句中必须包含所有非聚合列，否则可能报错；另外，题目中字段名可能不一致（如patCade vs patCode），需仔细核对。
```
