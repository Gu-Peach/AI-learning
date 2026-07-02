-- 关联查询

-- 示例数据
-- 员工表 t_employee
-- 员工编号 | 姓名 | 部门编号
-- S1001   | 张三 | D1001
-- S1002   | 李四 | D1001
-- S1003   | 如意 | D1002
-- S1004   | 吉祥 | D1003
-- S1005   | 王五 | NULL

-- 部门表 t_department
-- 部门编号 | 部门名称
-- D1001   | 技术部
-- D1002   | 人事部
-- D1003   | 市场部
-- D1004   | 测试部

-- 左连接：保留左表 t_employee 的所有记录，再去右表 t_department 中找匹配的部门信息
select e.eid, e.ename, e.did, d.dname
from t_employee e
left join t_department d
on e.did = d.did;

-- 左连接结果
-- 员工编号 | 姓名 | 部门编号 | 部门名称
-- S1001   | 张三 | D1001   | 技术部
-- S1002   | 李四 | D1001   | 技术部
-- S1003   | 如意 | D1002   | 人事部
-- S1004   | 吉祥 | D1003   | 市场部
-- S1005   | 王五 | NULL    | NULL

-- 右连接：保留右表 t_department 的所有记录，再去左表 t_employee 中找匹配的员工信息
select e.eid, e.ename, e.did, d.dname
from t_employee e
right join t_department d
on e.did = d.did;

-- 右连接结果
-- 员工编号 | 姓名 | 部门编号 | 部门名称
-- S1001   | 张三 | D1001   | 技术部
-- S1002   | 李四 | D1001   | 技术部
-- S1003   | 如意 | D1002   | 人事部
-- S1004   | 吉祥 | D1003   | 市场部
-- NULL    | NULL | NULL    | 测试部
