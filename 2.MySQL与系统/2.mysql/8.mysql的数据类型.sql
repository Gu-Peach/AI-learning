-- 1.数值类型（整数，浮点数，BIT）

-- 2.字符串类型
-- 2.1 定长字符串CHAR(M)与变长字符串VARCHAR(M)
drop table if exists t_char;
create table t_char (
  c1 char,
  c2 char(3)
);
insert into t_char values('男','女'); -- 成功
insert into t_char values('尚硅谷','尚硅谷'); -- 失败
insert into t_char values('男','尚硅谷'); -- 成功
select * from t_char;

drop table if exists t_char;
create table t_char (
  c1 varchar -- 错误
);
create table t_char (
  c1 varchar(3) -- 最多不超过3个字符
);
insert into t_char values('尚硅谷');
insert into t_char values('尚硅谷真好'); -- 失败
drop table if exists t_char;
create table t_char (
  name varchar(65535)
);
-- 错误，字符串过长

-- 2.2 枚举ENUM(值1,值2,值3)与集合SET(值1,值2,值3)
-- ENUM类型的字段在赋值时，只能在指定的枚举列表中取值，而且一次只能取一个。枚举列表最多可以有65535个成员。ENUM值在内部用整数表示，每个枚举值均有一个索引值， MySQL存储的就是这个索引编号。
-- SET类型的字段在赋值时，可从定义的值列表中选择1个或多个值的组合。SET列最多可以有64个成员。SET值在内部也用整数表示，分别是1，2，4，8……，都是2的n次方值，因为这些整数值对应的二进制都是只有1位是1，其余是0。
-- 对于枚举和集合的插入可以通过编号来选择，第一个的1，2，对应enum中的男女，第二个的编号对于集合中的编号组合》
drop table if exists t_enum;
create table t_enum (
  gender enum('男','女'),
  hobby set('睡觉','打游戏','运动','写代码')
);
desc t_enum;
insert into t_enum values('男','睡觉,打游戏'); -- 成功
insert into t_enum values('男,女','睡觉,打游戏'); -- 失败
insert into t_enum values('妖','睡觉,打游戏'); -- 失败
insert into t_enum values('男','睡觉,打游戏,吃饭'); -- 失败
select * from t_enum;
insert into t_enum values(2, 2);
select * from t_enum;
insert into t_enum values(1, 5); 
-- 5(0101)是1(0001)、4(0100)的组合
select * from t_enum;
insert into t_enum values(1, 7); 
-- 7(0111)是1(0001)、2(0010)、4(0100)的组合
select * from t_enum;
insert into t_enum values(2, 15);
select * from t_enum;

-- 2.3 文本类型TEXT(M)与BLOB(M)
-- 2.4 二进制类型

-- 3.日期和时间类型
-- 4.其他类型（json，空间数据类型）
-- 空间数据类型是用来存储“地理/几何位置数据”的，比如点、线、面这些地图信息
-- 常见的空间类型包括：

-- POINT：一个点，比如某个门店的位置
-- LINESTRING：一条线，比如道路
-- POLYGON：一个多边形，比如行政区范围
-- GEOMETRY：通用父类型
-- MULTIPOINT、MULTILINESTRING、MULTIPOLYGON、GEOMETRYCOLLECTION：多个点、线、面或混合集合