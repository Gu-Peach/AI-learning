-- ## 关联查询：两个或更多个表一起查询。
-- ## 前提条件：这些一起查询的表之间是有关系的（一对一、一对多），它们之间一定是有关联字段，这个关联字段可能建立了外键，也可能没有建立外键。


-- （1）凡是联合查询的两个表，必须有“关联字段”
-- 关联字段是逻辑意义一样，数据类型一样，名字可以一样也可以不一样的两个字段。比如：t_employee（A表）中did和t_department（B表）中的did。
-- 关联字段其实就是“可以”建外键的字段。当然联合查询不要求一定建外键。
-- （2）关联查询必须写关联条件，关联条件的个数 = n – 1，n是联合查询的表的数量
-- 2个表一起联合查询，关联条件数量是1，
-- 3个表一起联合查询，关联条件数量是2，
-- 4个表一起联合查询，关联条件数量是3， 
-- 否则就会出现笛卡尔积现象。
-- （3）关联条件可以用on子句编写，也可以写到where中
-- 但是建议用on单独编写，这样可读性更好。
-- 每一个join后面都要加on子句。
-- A inner|left|right join B on 关联条件
-- A inner|left|right join B on 关联条件 inner|left|right join C on 关联条件

-- ## 1.内连接
-- ![内连接](./images/1.png)
员工编号 | 姓名 | 部门编号      
S1001   | 张三 | D1001
S1002   | 李四 | D1001
S1003   | 如意 | D1002
S1004   | 吉祥 | D1003
S1005   | 王五 | NULL

部门编号 | 部门名称
D1001   | 技术部
D1002   | 人事部
D1003   | 市场部
D1004   | 测试部
use atguigu;
-- t_employee 看成A表
-- t_department 看成B表
-- 此时t_employee（A表）中的李红和周洲的did是NULL，没有对应部门
-- t_department（B表）中的测试部，没有对应员工

-- 内连接结果：
-- A∩B

-- 查询所有员工的姓名，部门编号，部门名称
-- 排除没有部门的员工
-- 排除没有员工的部门
-- 员工的姓名在t_employee（A表）
-- 部门的编号在t_employee（A表）和t_department（B表）都有
-- 部门名称在t_department（B表）
-- 所以需要联合两个表一起查询
select ename,did,dname
from t_employee inner join t_department;
-- 上述sql报错
-- did在两个表中都有，名字相同，不知道取哪个表中字段
-- 有可能存在两个表都有did，但是did的意义不同的情况
-- 为了避免这种情况，需要在编写sql的时候，明确指出是用哪个表的did
select ename,t_department.did,dname
from t_employee inner join t_department;
-- 上述sql语法对，结果不对
-- 出现 笛卡尔积 现象， A表记录*B表记录，因为缺乏条件，所以可能会出现以下结果
-- ename | t_department.did | dname
-- 张三  | D1001            | 技术部
-- 张三  | D1002            | 人事部
-- 张三  | D1003            | 市场部
-- 张三  | D1004            | 测试部

-- 李四  | D1001            | 技术部
-- 李四  | D1002            | 人事部
-- 李四  | D1003            | 市场部
-- 李四  | D1004            | 测试部

-- 如意  | D1001            | 技术部
-- 如意  | D1002            | 人事部
-- 如意  | D1003            | 市场部
-- 如意  | D1004            | 测试部

-- 吉祥  | D1001            | 技术部
-- 吉祥  | D1002            | 人事部
-- 吉祥  | D1003            | 市场部
-- 吉祥  | D1004            | 测试部

-- 王五  | D1001            | 技术部
-- 王五  | D1002            | 人事部
-- 王五  | D1003            | 市场部
-- 王五  | D1004            | 测试部
select ename,t_department.did,dname
from t_employee inner join t_department
on t_employee.did = t_department.did;

select *
from t_employee inner join t_department
on t_employee.did = t_department.did;

-- 查询部门编号为1的女员工的姓名、部门编号、部门名称、薪资等情况
select ename,gender,t_department.did,dname,salary
from t_employee inner join t_department 
on t_employee.did = t_department.did
where t_department.did = 1 and gender = '女';

-- 查询部门编号为1的员工姓名、部门编号、部门名称、薪资、职位编号、职位名称等情况
select ename,gender,t_department.did,dname,salary,job_id,jname
from t_employee
inner join t_department on t_employee.did = t_department.did
inner join t_job on t_employee.job_id = t_job.jid
where t_department.did = 1;

-- 2.左连接
use atguigu;
-- t_employee 看成A表
-- t_department 看成B表
-- 此时t_employee（A表）中的李红和周洲的did是NULL，没有对应部门
-- t_department（B表）中的测试部，没有对应员工

-- 左连接结果：
-- A
-- A-A∩B

-- 查询所有员工，包括没有指定部门的员工，他们的姓名、薪资、部门编号、部门名称
select ename,salary,t_department.did,dname
from t_employee left join t_department
on t_employee.did = t_department.did;
-- 查询的结果是A
-- 结果示例：
-- 张三 | 10000 | D1001 | 技术部
-- 李四 | 12000 | D1001 | 技术部
-- 如意 | 11000 | D1002 | 人事部
-- 吉祥 | 13000 | D1003 | 市场部
-- 王五 |  9000 | NULL  | NULL

-- 查询没有部门的员工信息
select ename,salary,t_department.did,dname
from t_employee left join t_department
on t_employee.did = t_department.did
where t_employee.did is null;
-- 查询的结果是A-A∩B
-- 此时的where条件，建议写子表的关联字段is null，这样更准确一点
-- 如果要建外键，它们之间有子表和父表的角色，写子表的关联字段is null
-- 因为父表中这个字段一般是主键，不会为null
-- 结果示例：
-- 王五 | 9000 | NULL | NULL


-- 3.右连接
use atguigu;
-- t_employee 看成A表
-- t_department 看成B表
-- 此时t_employee（A表）中的李红和周洲的did是NULL，没有对应部门
-- t_department（B表）中的测试部，没有对应员工

-- 右连接结果：
-- B
-- B-A∩B

-- 查询所有部门，包括没有对应员工的部门，他们的姓名、薪资、部门编号、部门名称
select ename,salary,t_department.did,dname
from t_employee right join t_department
on t_employee.did = t_department.did;
-- 查询的结果是B
-- 结果示例：
-- 张三 | 10000 | D1001 | 技术部
-- 李四 | 12000 | D1001 | 技术部
-- 如意 | 11000 | D1002 | 人事部
-- 吉祥 | 13000 | D1003 | 市场部
-- NULL |  NULL | D1004 | 测试部

-- 查询没有员工部门的信息
select ename,salary,t_department.did,dname
from t_employee right join t_department
on t_employee.did = t_department.did
where t_employee.did is null;
-- 查询的结果是B-A∩B
-- 结果示例：
-- NULL | NULL | D1004 | 测试部

-- 查询所有员工，包括没有指定部门的员工，他们的姓名、薪资、部门编号、部门名称
select ename,salary,t_department.did,dname
from t_department right join t_employee
on t_employee.did = t_department.did;
-- 查询的结果是B
-- 结果示例：
-- 张三 | 10000 | D1001 | 技术部
-- 李四 | 12000 | D1001 | 技术部
-- 如意 | 11000 | D1002 | 人事部
-- 吉祥 | 13000 | D1003 | 市场部
-- 王五 |  9000 | NULL  | NULL

--查询没有部门的员工信息
select ename,salary,t_department.did,dname
from t_department right join t_employee
on t_employee.did = t_department.did
where t_employee.did is null;
-- 查询的结果是B-A∩B
-- 结果示例：
-- 王五 | 9000 | NULL | NULL



-- union合并查询
use atguigu;
-- t_employee 看成A表
-- t_department 看成B表
-- 此时t_employee（A表）中的李红和周洲的did是NULL，没有对应部门
-- t_department（B表）中的测试部，没有对应员工

-- union结果：
-- A∪B
-- A∪B-A∩B = A-A∩B ∪ B-A∩B
-- union合并时要注意：
-- 两个表要查询的结果字段是一样的
-- union all 表示直接合并结果，保留重复的记录
-- union 表示合并结果时，去重
-- 要实现A∪B的结果，那么必须是合并查询是A表结果和查询是B表结果的select语句
-- 要实现A∪B-A∩B的结果，那么必须是合并查询是A-A∩B结果和查询是B-A∩B的select语句

-- 查询所有员工和所有部门，包括没有指定部门的员工和没有分配员工的部门
select *
from t_employee left join t_department
on t_employee.did=t_department.did
union
select *
from t_employee right join t_department
on t_employee.did=t_department.did;
-- 以下union会报错，两个select语句的列数是不同的
select * from t_employee
union
select * from t_department;

-- 查询那些没有分配部门的员工和没有指定员工的部门，即A表和B表在对方那里找不到对应记录的数据
select *
from t_employee left join t_department
on t_employee.did = t_department.did
where t_employee.did is null
union
select *
from t_employee RIGHT join t_department
on t_employee.did = t_department.did
where t_employee.did is null;