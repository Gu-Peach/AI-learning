-- MySQL中的函数必须有返回值，参数可以有可以没有。
-- MySQL中函数分为：
-- （1）系统预定义函数：MySQL数据库管理软件提供的函数，直接用就可以，任何数据库都可以用公共的函数。
-- 单行函数：表示会对表中的每一行记录分别计算，有n行得到还是n行结果。如数学函数、字符串函数、日期时间函数、条件判断函数、窗口函数等。
-- 分组函数：或者又称为聚合函数，多行函数，表示会对表中的多行记录一起做一个“运算”，得到一个结果。如求平均值的avg，求最大值的max，求最小值的min，求总和sum，求个数的count等。
-- （2）用户自定义函数：由开发人员自己定义的，通过CREATE FUNCTION语句定义，是属于某个数据库的对象。

-- 1.单行函数
-- 1.1 常用数学函数
-- 函数	说明
-- abs(x)	绝对值
-- ceil(x)	向上取整
-- floor(x)	向下取整
-- mod(x,y)	x模y
-- rand()	返回0~1的随机值
-- round(x,y)	返回参数x的四舍五入的有y位的小数的值
-- truncate(x,y)	返回数字x截断为y位小数的结果
-- format(x,y)	强制保留小数点后y位，整数部分超过三位的时候以逗号分割，并且返回的结果是文本类型
-- sqrt(x)	x的平方根
-- pow(x,y)	x的y次方
-- case
use atguigu;
-- 在t_employee表中查询员工无故旷工一天扣多少钱
-- 分别使用ceil,floor,round,truncate函数
-- 假设本月工作日总天数是22天
-- 旷工一天扣的钱=salary/22
select
  ename,
  salary/22,
  ceil(salary/22),
  floor(salary/22),
  round(salary/22,2),
  truncate(salary/22,2)
from t_employee;
-- 查询公司平均薪资，并对平均薪资分别
-- 分别使用ceil,floor,round,truncate函数
select
  avg(salary),
  ceil(avg(salary)),
  floor(avg(salary)),
  round(avg(salary),2),
  truncate(avg(salary),2)
from t_employee;


-- 1.2 常用字符串函数
-- concat(s1,s2,…)	拼接字符串
-- concat_ws(a,s1,s2,…)	在字符串间加上a拼接字符串
-- char_length(s)	s的字符数
-- length(s)	s的字节数，与字符集有关
-- locate(s,str) 或 instr(str,s)	返回s在str中的开始位置
-- upper(s) 或 ucase(s)	所有字母转大写
-- lower(s) 或 lcase(s)	所有字母转小写
-- left(s,n)	返回最左边的n个字符
-- right(s,n)	返回最右边的n个字符
-- lpad(str,len,pad)	用pad从左边填充str直到长度达到len
-- rpad(str,len,pad)	用pad从右边填充str直到长度达到len
-- ltrim(s)	去掉s左侧空格
-- rtrim(s)	去掉s右侧空格
-- trim(s)	去掉s两侧空格
-- trim([both] s from str)	去掉str两侧的s
-- trim([leading] s from str)	去掉str左侧的s
-- trim([trailing] s from str)	去掉str右侧的s
-- insert(str,index,len,instr)	str从index位置开始的len个字符替换为instr
-- replace(str,a,b)	str中的a全部替换为b
-- repeat(s,n)	返回s重复n次的结果
-- reverse(s)	反转字符串
-- strcmp(s1,s2)	比较s1,s2
-- substring(str,index,len)	str从index位置截取len个字符
-- substring_index(str,分隔符,count)	如果count是正数，那么从左往右数，截取第n个分隔符的左边的全部内容。例如，substring_index("www.atguigu.com",".",1)是"www"。如果count是负数，那么从右边开始数，截取第n个分隔符右边的所有内容。例如，substring_index("www.atguigu.com",".",-1)是"com"。
use atguigu;
-- 在t_employee表中查询员工姓名ename和电话tel
-- 并使用concat函数，concat_ws函数
select concat(ename,tel),concat_ws('-',ename,tel) from t_employee;
-- 在t_employee表中查询薪资高于15000的男员工姓名
-- 并把姓名处理成 张xx 的样式
-- left(s,n)函数表示取字符串s最左边的n个字符
-- 而rpad(str,len,pad)函数表示在字符串str的右边填充pad使得字符串长度达到len
select rpad(left(ename,1),3,'x'),salary
from t_employee
where salary>15000 and gender='男';
-- 在t_employee表中查询薪资高于10000的男员工姓名，姓名包含的字符数和占用的字节数
select ename,char_length(ename) as 占用字符数,length(ename) as 占用字节数量
from t_employee
where salary>10000 and gender='男';
-- 在t_employee表中查询薪资高于10000的男员工姓名和邮箱email
-- 并把邮箱名 @ 字符之前的字符串截取出来
-- MySQL中substring函数截取字符串，位置从1开始
select ename,email,substring(email,1,position('@' in email)-1)
from t_employee
where salary>10000 and gender='男';
-- trim()默认是去掉前后空白符
select trim('  hello  world  ');
select concat('[',trim('  hello  world  '),']');
-- 去掉前后的 &
select trim(both '&' from '&&&&hello  world&&&&');
select trim(leading '&' from '&&&&hello  world&&&&');
select trim(trailing '&' from '&&&&hello  world&&&&');



-- 9.1.4常用加密函数
-- 函数	说明
-- password(str)	返回字符串str的加密版本，41位长的字符串（MySQL8不再支持）
-- md5(str)	返回字符串str的md5值，也是一种加密方式
-- sha(str)	返回字符串str的sha算法加密字符串，40位十六进制值的密码字符串
-- sha2(str,hash_length)	返回字符串str的sha算法加密字符串，密码字符串的长度是hash_length/4。hash_length可以是224、256、384、512、0，其中0等同于256
-- 示例：
-- use atguigu;
-- 当用户需要对数据进行加密时
-- 比如做登录功能时，给用户的密码加密等
select md5('123456'),sha('123456'),sha2('123456',0);
select 
  char_length(md5('123456')),
  char_length(sha('123456')),
  char_length(sha2('123456',0));
drop table if exists t_user;
create table t_user(
  id int primary key auto_increment,
  username varchar(20),
  password varchar(100)
);
insert into t_user values(null,"chai",md5("123456"));
select * from t_user where username="chai" and password="123456";
select * from t_user where username="chai" and password=md5("123456");
drop table if exists t_user;
9.1.5常用系统信息函数
函数	说明
database()	当前数据库名
version()	当前数据库版本
user()	当前登录用户名
9.1.6条件判断函数
函数	说明
if(a,x,y)	如果a为真，返回x，否则返回y
ifnull(x,y)	如果x不为空，返回x，否则返回y
case
when 条件1 then result1
when 条件2 then result2
else resultn
end	依次判断条件，哪个条件满足了，就返回对应的result,所有条件都不满足就返回else的result。如果没有单独的else子句，当所有when后面的条件都不满足时则返回NULL
case 表达式
when 常量值1 then 值1
when 常量值2 then 值2
else 值n
end	判断表达式与哪个常量值匹配，找到匹配的就返回对应值，都不匹配就返回else的值。如果没有单独的else子句，当所有when后面的常量值都不匹配时则返回NULL
示例：
use atguigu;
-- 条件判断函数不是筛选记录的函数
-- 而是根据条件不同显示不同的结果的函数
-- 如果薪资大于20000，显示高薪，否则显示正常
select ename,salary,if(salary>20000,'高薪','正常')
from t_employee;
-- 计算实发工资。实发工资 = 薪资 + 薪资 * 奖金比例
select
  ename,
  salary,
  commission_pct,
  salary + salary * commission_pct as 实发工资
from t_employee;
-- 如果commission_pct是，计算完结果是NULL
select
  ename,
  salary,
  commission_pct,
  salary + salary * ifnull(commission_pct,0) as 实发工资
from t_employee;
-- 查询员工编号，姓名，薪资，等级，等级根据薪资判断
-- 如果薪资大于20000，显示 羡慕级别
-- 如果薪资15000-20000，显示 努力级别
-- 如果薪资10000-15000，显示 平均级别
-- 如果薪资10000以下，显示 保底级别
select eid,ename,salary,
case
  when salary>20000 then '羡慕级别'
  when salary>15000 then '努力级别'
  when salary>10000 then '平均级别'
  else '保底级别'
end as "等级"
from t_employee; 
-- 在t_employee表中查询入职7年以上的员工姓名、工作地点、轮岗的工作地点数量情况
-- 计算工作地点的数量可以转换为求work_place中逗号的数量+1
-- work_place中逗号的数量 = work_place的总字符数 - work_place去掉逗号的字符数
-- 使用replace函数去掉work_place中逗号
select work_place,
char_length(work_place)-char_length(replace(work_place,",",""))+1 as 工作地点数量
from t_employee;

select ename,work_place,
case char_length(work_place)-char_length(replace(work_place,",",""))+1
  when 1 then '只在一个地方工作'
  when 2 then '在两个地方来回奔波'
  when 3 then '在三个地方流动'
  else '频繁出差'
end as "工作地点数量情况"
from t_employee
where datediff(curdate(),hiredate)>365*7;



-- 2.分组函数
-- 常用的分组函数：
-- 函数	说明
-- avg(x)	平均值
-- sum(x)	求和
-- max(x)	最大值
-- min(x)	最小值
-- count(x)	计数，统计包含内容的数量
use atguigu;
-- 统计t_employee表的员工的数量
select count(*) from t_employee;
select count(1) from t_employee;
select count(eid) from t_employee;
select count(commission_pct) from t_employee;
/*
count(*)或count(常量值)：都是统计实际的行数
count(字段/表达式)：统计时忽略NULL值
*/
-- 找出t_employee表中最高的薪资值
select max(salary) from t_employee;
-- 找出t_employee表中最低的薪资值
select min(salary) from t_employee;
-- 统计t_employee表中平均薪资值
select avg(salary) from t_employee;
-- 统计所有人的薪资总和
select sum(salary) from t_employee;
select sum(salary+salary*ifnull(commission_pct,0)) from t_employee;
-- 找出年龄最小、最大的员工的出生日期
select min(birthday),max(birthday) from t_employee;
-- 查询最新入职的员工的入职日期
select max(hiredate) from t_employee;


-- 3.窗口函数（OLAP函数）
-- 窗口函数	说明
-- row_number()	顺序排序，每行按照不同的分组逐行编号，例如：1,2,3,4
-- rank()	并列排序，每行按照不同的分组进行编号，同一个分组中排序字段值出现重复值时，并列排序并跳过重复序号，例如：1,1,3
-- dense_rank()	并列稠密排序，每行按照不同的分组进行编号，同一个分组中排序字段值出现重复值时，并列排序不跳过重复序号，例如：1,1,2
-- lag()/lead()	访问窗口中当前行前/后一定偏移量的值
-- first_value()/last_value()	访问窗口中第一个或最后一个值
-- sum()/avg()/count()/max()/min()	求和/平均值/计数/最大值/最小值
-- 语法格式
函数名(参数列表) over(
 [partition by column]
 [order by column]
 [rows between <start> and <end>]
)

-- over关键字用来指定窗口函数的窗口范围。如果over后面是空（），则表示select语句筛选的所有行是一个窗口。over后面的（）支持以下语法来设置窗口范围：
-- window：给窗口指定一个别名
-- partition by：一个窗口范围还可以分为多个区域。按照哪些字段进行分区/分组，窗口函数在不同的分组上分别处理分析
-- order by：按照哪些字段进行排序，窗口函数将按照排序后结果进行分析处理
-- rows/range between <start> and <end>：在计算窗口函数时，指定哪些行/值将被包含在计算范围内，<start>和<end>用于定义窗口范围：
-- unbounded preceding：窗口从分区的第一行开始
-- n preceding：当前行之前的n行
-- current row：当前行
-- n following： 当前行之后的n行
-- unbounded following：窗口到分区的最后一行

use atguigu;
-- 在t_employee表中查询薪资在[8000,10000]之间的员工姓名和薪资并给每一行记录编序号
select row_number() over() as rn,ename,salary
from t_employee
where salary between 8000 and 10000;




-- 计算每一个部门的平均薪资与全公司的平均薪资的差值
select distinct
  did,
  avg(salary) over(partition by did),
  avg(salary) over(),
--   round(数字, 小数位数)：将数字四舍五入到指定的小数位数
  round(avg(salary) over(partition by did)-avg(salary) over(),2) as deviation
from t_employee;


-- 在t_employee表中查询女员工姓名，部门编号，薪资
-- 查询结果按照部门编号分组后在按薪资升序排列
-- 并分别使用row_number()、rank()、dense_rank()三个序号函数给每一行记录编序号
select ename,did,salary,gender,
row_number() over(partition by did order by salary) as "row_num",
rank() over(partition by did order by salary) as "rank_num",
dense_rank() over(partition by did order by salary) as "ds_rank_num"
from t_employee where gender='女';


-- 或使用window给窗口指定别名
select ename,did,salary,
row_number() over w as "row_num",
rank() over w as "rank_num" ,
dense_rank() over w as "ds_rank_num" 
from t_employee where gender='女'
window w as(partition by did order by salary);

-- 在t_employee表中查询每个部门最低3个薪资值的女员工姓名，部门编号，薪资值
select row_number() over() as rn,temp.*
from(select ename,did,salary,
row_number() over w as "row_num",
rank() over w as "rank_num" ,
dense_rank() over w as "ds_rank_num"
from t_employee where gender='女'
window w as(partition by did order by salary))temp
where temp.rank_num<=3;
-- 在t_employee表中查询每个部门薪资排名前3的员工姓名，部门编号，薪资值
select temp.*
from(select ename,did,salary,
dense_rank() over w as "ds_rank_num"
from t_employee
window w as(partition by did order by salary desc))temp
where temp.ds_rank_num<=3;
-- 在t_employee表中查询全公司薪资排名前3的员工姓名，部门编号，薪资值
select temp.*
from(select ename,did,salary,
dense_rank() over w as "ds_rank_num"
from t_employee
window w as(order by salary desc))temp
where temp.ds_rank_num<=3;
-- 查找薪资排名的上一位、下一位、首位、末位
select
  ename,
  salary,
  lag(ename,1,'-') over(order by salary) as '上一位姓名',
  lag(salary,1,0) over(order by salary) as '上一位薪资',
  lead(ename) over(order by salary) as '下一位姓名',
  lead(salary) over(order by salary) as '下一位薪资',
  first_value(salary) over(order by salary) as '首位薪资',
  last_value(ename) over(order by salary rows between unbounded preceding and unbounded following) as '末位姓名'
from t_employee;