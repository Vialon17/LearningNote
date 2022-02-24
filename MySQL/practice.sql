---------创建数据库、表、插入数据----------------------
CREATE DATABASE temp;
-- 建表
-- 学生表
CREATE TABLE Student(
  s_id VARCHAR(20) COMMENT '学生编号',
  s_name VARCHAR(20) NOT NULL DEFAULT '' COMMENT '学生姓名',
  s_birth VARCHAR(20) NOT NULL DEFAULT '' COMMENT '出生年月',
  s_sex VARCHAR(10) NOT NULL DEFAULT '' COMMENT '学生性别',
  PRIMARY KEY(s_id)
) ENGINE = INNODB DEFAULT CHARSET = utf8 COMMENT '学生表';
-- 课程表
CREATE TABLE Course(
  c_id VARCHAR(20) COMMENT '课程编号',
  c_name VARCHAR(20) NOT NULL DEFAULT '' COMMENT '课程名称',
  t_id VARCHAR(20) NOT NULL COMMENT '教师编号',
  PRIMARY KEY(c_id)
) ENGINE = INNODB DEFAULT CHARSET = utf8 COMMENT '课程表';
-- 教师表
CREATE TABLE Teacher(
  t_id VARCHAR(20) COMMENT '教师编号',
  t_name VARCHAR(20) NOT NULL DEFAULT '' COMMENT '教师姓名',
  PRIMARY KEY(t_id)
) ENGINE = INNODB DEFAULT CHARSET = utf8 COMMENT '教师表';
-- 成绩表
CREATE TABLE Score(
  s_id VARCHAR(20) COMMENT '学生编号',
  c_id VARCHAR(20) COMMENT '课程编号',
  s_score INT(3) COMMENT '分数',
  PRIMARY KEY(s_id, c_id)
) ENGINE = INNODB DEFAULT CHARSET = utf8 COMMENT '成绩表';
-- 插入学生表测试数据
INSERT INTO
  Student
VALUES('01', '赵雷', '1990-01-01', '男');
INSERT INTO
  Student
VALUES('02', '钱电', '1990-12-21', '男');
INSERT INTO
  Student
VALUES('03', '孙风', '1990-05-20', '男');
INSERT INTO
  Student
VALUES('04', '李云', '1990-08-06', '男');
INSERT INTO
  Student
VALUES('05', '周梅', '1991-12-01', '女');
INSERT INTO
  Student
VALUES('06', '吴兰', '1992-03-01', '女');
INSERT INTO
  Student
VALUES('07', '郑竹', '1989-07-01', '女');
INSERT INTO
  Student
VALUES('08', '王菊', '1990-01-20', '女');
-- 课程表测试数据
INSERT INTO
  Course
VALUES('01', '语文', '02');
INSERT INTO
  Course
VALUES('02', '数学', '01');
INSERT INTO
  Course
VALUES('03', '英语', '03');
-- 教师表测试数据
INSERT INTO
  Teacher
VALUES('01', '张三');
INSERT INTO
  Teacher
VALUES('02', '李四');
INSERT INTO
  Teacher
VALUES('03', '王五');
-- 成绩表测试数据
INSERT INTO
  Score
VALUES('01', '01', 80);
INSERT INTO
  Score
VALUES('01', '02', 90);
INSERT INTO
  Score
VALUES('01', '03', 99);
INSERT INTO
  Score
VALUES('02', '01', 70);
INSERT INTO
  Score
VALUES('02', '02', 60);
INSERT INTO
  Score
VALUES('02', '03', 80);
INSERT INTO
  Score
VALUES('03', '01', 80);
INSERT INTO
  Score
VALUES('03', '02', 80);
INSERT INTO
  Score
VALUES('03', '03', 80);
INSERT INTO
  Score
VALUES('04', '01', 50);
INSERT INTO
  Score
VALUES('04', '02', 30);
INSERT INTO
  Score
VALUES('04', '03', 20);
INSERT INTO
  Score
VALUES('05', '01', 76);
INSERT INTO
  Score
VALUES('05', '02', 87);
INSERT INTO
  Score
VALUES('06', '01', 31);
INSERT INTO
  Score
VALUES('06', '03', 34);
INSERT INTO
  Score
VALUES('07', '02', 89);
INSERT INTO
  Score
VALUES('07', '03', 98);
--------------------------------------------------
  -- 1、查询"01"课程比"02"课程成绩高的学生的信息及课程分数
  desc score
select
  *
from
  score
  join score temp on score.s_id = temp.s_id
  and score.s_score > temp.s_score
  LEFT JOIN student ON student.s_id = score.s_id
where
  score.c_id = '01'
  and temp.c_id != '03'
select
  *
from
  score
where
  c_id != '03';

-- 1、查询"01"课程比"02"课程成绩高的学生的信息及课程分数

-- 2、查询"01"课程比"02"课程成绩低的学生的信息及课程分数
SELECT
  *
FROM
  score
  JOIN score temp ON score.s_id = temp.s_id
  AND score.s_score > temp.s_score
  LEFT JOIN student ON student.s_id = score.s_id
WHERE
  score.c_id = '02'
  AND temp.c_id != '03' -- 3、查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
select
  student.*,
  avg(s_score)
from
  score
  left join student on score.s_id = student.s_id
group by
  score.s_id
having
  AVG(s_score) >= 60 -- 4、查询平均成绩小于60分的同学的学生编号和学生姓名和平均成绩
  -- (包括有成绩的和无成绩的)
select
  student.s_id,
  avg(s_score) avg_temp
from
  student
  left join score on student.s_id = score.s_id
group by
  student.s_id
having
  if(isnull(avg_temp), 0, avg_temp) < 60 -- 5、查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩,并从高到低排序
select
  student.s_id,
  s_name,
  count(s_score),
  sum(s_score)
from
  student
  left join score on student.s_id = score.s_id
group by
  student.s_id -- 6、查询"李"姓老师的数量
select
  count(1)
from
  teacher
where
  t_name like '李%' -- 7、查询学过"张三"老师授课的同学的信息
select
  *
from
  student
where
  s_id in(
    select
      s_id
    from
      score
    where
      c_id in(
        select
          c_id
        from
          course
        where
          t_id in (
            select
              t_id
            from
              teacher
            where
              t_name = '张三'
          )
      )
  ) -- 8、查询没学过"张三"老师授课的同学的信息
SELECT
  *
FROM
  student
WHERE
  s_id not IN(
    SELECT
      s_id
    FROM
      score
    WHERE
      c_id IN(
        SELECT
          c_id
        FROM
          course
        WHERE
          t_id IN (
            SELECT
              t_id
            FROM
              teacher
            WHERE
              t_name = '张三'
          )
      )
  ) -- 9、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息,及两门课程成绩
SELECT
  student.*,
  s_score
FROM
  score
  JOIN student ON student.s_id = score.s_id
where
  score.s_id in (
    select
      student.s_id
    from
      score
      join student on student.s_id = score.s_id
    where
      c_id in ('01', '02')
    group by
      student.s_id
    having
      count(c_id) >= 2
  )
SELECT
  E.ENAME,
  E.HIREDATE - LAG(E.HIREDATE, 1) OVER(
    ORDER BY
      E.HIREDATE ASC
  )
FROM
  EMP E
SELECT
  student.*,
  sc.s_score,
  sc.c_id,
  score.s_id,
  score.s_id
FROM
  score
  JOIN score sc on score.s_id = sc.s_id
  and score.c_id != sc.c_id
  right join student on student.s_id = score.s_id
where
  score.c_id in ('01', '02')
  and sc.c_id IN ('01', '02') -- 10、查询学过编号为"01"但是没有学过编号为"02"的课程的同学的信息
select
  *
from
  student
where
  s_id in (
    select
      s_id
    from
      score
    where
      C_id = '01'
  )
  and s_id not in (
    SELECT
      s_id
    FROM
      score
    WHERE
      C_id = '02'
  ) -- 11、查询没有学全所有课程的同学的信息
select
  student.*
from
  score
  join student on student.`s_id` = score.`s_id`
group by
  s_id
having
  count(c_id) < (
    select
      count(c_id)
    from
      course
  ) -- 12、查询至少有一门课与学号为"01"的同学所学相同的同学的信息
SELECT
  student.*
FROM
  score
  JOIN student ON student.`s_id` = score.`s_id`
where
  student.s_id != '01'
  and c_id in (
    select
      c_id
    from
      score
    where
      s_id = '01'
  ) -- 13、查询和"01"号的同学学习的课程完全相同的其他同学的信息
SELECT
  student.*
FROM
  score
  JOIN student ON student.`s_id` = score.`s_id`
WHERE
  student.s_id != '01'
  AND c_id IN (
    SELECT
      c_id
    FROM
      score
    WHERE
      s_id = '01'
  )
select
  *
from
  (
    SELECT
      s_id,
      c_id
    FROM
      score
    WHERE
      s_id != '01'
  ) temp1
  join (
    SELECT
      c_id
    FROM
      score
    WHERE
      s_id = '01'
  ) temp2 on temp2.c_id = temp1.c_id
select
  *
from
  student
where
  s_id in (
    SELECT
      s_id
    FROM
      (
        SELECT
          s_id,
          c_id
        FROM
          score
        WHERE
          s_id != '01'
      ) temp1
      right JOIN (
        SELECT
          c_id
        FROM
          score
        WHERE
          s_id = '01'
      ) temp2 ON temp2.c_id = temp1.c_id
    group by
      s_id
    having
      count(temp1.c_id) = (
        SELECT
          count(c_id)
        FROM
          score
        WHERE
          s_id = '01'
      )
  ) -- 15、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
select
  s_name,
  temp.*
from
  student
  right join (
    select
      s_id,
      avg(s_score)
    from
      score
    group by
      s_id
    having
      count(if(s_score < 60, 1, null)) >= 2
  ) temp on student.s_id = temp.s_id -- 16、检索"01"课程分数小于60，按分数降序排列的学生信息及01分数
select
  student.*,
  s_score
from
  student
  right join (
    select
      s_id,
      s_score
    from
      score
    where
      c_id = '01'
      and s_score < '60'
  ) temp on student.s_id = temp.s_id
order by
  s_score desc -- 17、按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
select
  score.*,
  avg1
from
  score
  left join (
    select
      s_id,
      avg(s_score) avg1
    from
      score
    group by
      s_id
  ) temp on temp.s_id = score.s_id;
-- 18.查询各科成绩最高分、最低分和平均分：以如下形式显示：课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
  -- 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
select
  score.c_id,
  max(s_score),
  min(s_score),
  avg(s_score),
  concat(
    round(
      count(if(s_score >= 60, s_score, null)) / count(s_score) * 100,
      2
    ),
    '%'
  )
from
  score
  left join course on course.c_id = score.c_id
GROUP BY
  score.c_id;
-- 20、查询学生的总成绩并进行排名
select empno, emp.ename, rank1 from emp left join  
(select ename, rank() over(partition by deptno order by sal) rank1 from emp) temp on emp.ename = temp.ename where rank1 = 2
;

select score.s_id, sum(s_score) from score right join student on score.s_id = student.s_id group by s_id order by sum(s_score) desc;
-- 21、查询不同老师所教不同课程平均分从高到低显示

select t_name, c_name, avg1 from teacher left join course on teacher.t_id = course.t_id 
left join (select c_id, round(avg(s_score),2) avg1 from score group by c_id) temp on temp.c_id = course.c_id;
  -- 22、查询所有课程的成绩第2名到第3名的学生信息及该课程成绩

select * from student where s_id in (select * from (select s_id from score group by s_id order by sum(s_score) limit 2,2) temp);
  -- 23、统计各科成绩各分数段人数：课程编号,课程名称,[100-85],[85-70],[70-60],[0-60]及所占百分比

select 
  *,
  (case 
                  when (s_score between 85 and 100) then 4
                  when (s_score between 70 and 84) then 3
                  when (s_score between 60 and 69) then 2
                  when (s_score between 0 and 59) then 1
                  else null end
  ) temp
from score order by temp;

--1 max sal'a name in every deptno,
select emp.* from emp join (select ename, rank()over(partition by deptno order by sal desc) rank1 from emp order by rank1) temp on emp.ename = temp.ename where temp.rank1 = 1;
--2 up average in every deptno
select emp.*, avg1 from emp right join (select ename, round(avg(sal)over(partition by deptno),2) avg1 from emp) temp on temp.ename = emp.ename where emp.sal > temp.avg1;
--3 average sal grade in every deptno
select emp.* from emp left join 
(select ename, round(avg(sal)over(),2) avg1 from emp) temp on emp.ename = temp.ename where emp.sal>avg1;
--4 avg max by amptno
select emp.deptno, dept.dname, round(avg(sal)over(partition by deptno),2) avg1 from emp left join dept on emp.deptno = dept.deptno limit 1;
--5 avg max grade
select * from 
(select distinct *, dense_rank()over(order by grade desc) rank1 from 
(select emp.deptno, dept.dname, round(avg(sal) over(partition by deptno), 2) avg1 from emp 
left join dept on emp.deptno = dept.deptno) temp left join salgrade on avg1 between losal
and hisal) temp1 where rank1 = 1;
-- 24、查询学生平均成绩及其名次
select *, dense_rank()over(order by avg1 desc) from 
(select s_id, round(avg(s_score),2) avg1 from score group by s_id) temp;
  -- 24.1添加名次rank,（相同分数的相同名次，并列排名）
select *, dense_rank()over(order by s_score desc) from score;
  -- 25、查询各科成绩前三名的记录
select * from
(select *, dense_rank()over(partition by c_id order by s_score desc) rank1 from score) temp
where temp.rank1 in(1, 2, 3);
  -- 26、查询每门课程被选修的学生数
select c_id, count(s_id) from score group by c_id;
  -- 27、查询出只有两门课程的全部学生的学号和姓名
select student.* from student left join
(select s_id, count(c_id)over(partition by s_id) count1 from score) temp on temp.s_id = student.s_id where count1 = 2;
  -- 28、查询男生、女生人数
select s_sex, count(s_id) from student group by s_sex;
  -- 29、查询名字中含有"风"字的学生信息
select * from student where s_name like '%风%';
  -- 30、查询同名同性学生名单，并统计同名人数
select * from 
(select temp.*, count(num)over(partition by s_name) num_1 from 
(select s_name, dense_rank()over(order by s_name) num from student) temp) temp1 where num_1 > 1;
  -- 31、查询1990年出生的学生名单
select * from student where year(s_birth) = '1990';
  -- 32、查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
select avg(s_score), c_id from score group by c_id order by avg(s_score) desc, c_id;
  -- 33、查询平均成绩大于等于85的所有学生的学号、姓名和平均成绩
select * from student right join
(select s_id, round(avg(s_score),2) from score group by s_id having avg(s_score) > 85) temp on temp.s_id = student.s_id ;
  -- 34、查询课程名称为"数学"，且分数低于60的学生姓名和分数
select s_name, s_score from student left join score on score.s_id = student.s_id where c_id in(select c_id from course where c_name = '数学') and s_score < 60;
  -- 35、查询所有学生的课程及分数情况；
select student.*, c_id, s_score from student left join score on student.s_id = score.s_id;
  -- 36、查询任何一门课程成绩在70分以上的姓名、课程名称和分数；
select student.*, c_id, s_score from student left join score on student.s_id = score.s_id where s_score > 70;
  -- 37、查询不及格的学生id,姓名，及其课程名称，分数
select student.*, c_id, s_score from student left join score on student.s_id = score.s_id where s_score < 60;
  -- 38、查询课程编号为01且课程成绩在80分以上的学生的学号和姓名；
select student.*, c_id, s_score from student left join score on student.s_id = score.s_id where s_score > 80 and c_id = '01';
  -- 39、求每门课程的学生人数
select distinct c_id, count(s_id)over(partition by c_id) from score;

select c_id, count(s_id) from score group by c_id;
  -- 40、查询选修"张三"老师所授课程的学生中，成绩最高的学生信息及其成绩
select student.*, c_id, s_score from student right join score on student.s_id = score.s_id where score.s_id in (select s_id from (select s_id, dense_rank()over(order by s_score desc) temp1 from score left join course on course.c_id = score.c_id where t_id in (select t_id from teacher where t_name = '张三')) temp where temp1 = 1);
  -- 41、查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
select * from check1 join check1 ck on ck.sid != check1.sid;
-- 42、查询每门功课成绩最好的前两名
  -- 43、统计每门课程的学生选修人数（超过5人的课程才统计）。要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
  -- 44、检索至少选修两门课程的学生学号
  -- 45、查询选修了全部课程的学生信息
  -- 46、查询各学生的年龄
  -- 47、查询本周过生日的学生
  -- 48、查询下周过生日的学生
  -- 49、查询本月过生日的学生
  -- 50、查询下月过生日的学生

drop table if exists login;
CREATE TABLE `login` (
`id` int(4) NOT NULL,
`user_id` int(4) NOT NULL,
`client_id` int(4) NOT NULL,
`date` date NOT NULL,
PRIMARY KEY (`id`));

INSERT INTO login VALUES
(1,2,1,'2020-10-12'),
(2,3,2,'2020-10-12'),
(3,1,2,'2020-10-12'),
(4,2,2,'2020-10-13'),
(5,1,2,'2020-10-13'),
(6,3,1,'2020-10-14'),
(7,4,1,'2020-10-14'),
(8,4,1,'2020-10-15');

select *, round(count2/count1, 3) nod from (select user_id, substr(date, -2, 2) sub1, count(user_id)over(partition by date) count1 from login) temp1 right join 
(select user_id temp_id, substr(date, -2, 2) sub2, count(user_id)over(partition by date) count2 from login) temp2 on temp2.sub2 - 1 = temp1.sub1 where temp_id = user_id;

create View temp1 as select * from login