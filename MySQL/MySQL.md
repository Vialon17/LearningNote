# MySQl Learning Note

**It's so funny that I have to `Reinvent the Wheel`, lol~**

*But you couldn't oppose it because it can improve ur comprehension of the target*🤣 🤣 🤣

## About MySQL

There usually have two type of databases: `SQL(Sequel)` and `noSQL` in computer system, here has a table showing the difference:
  | **Relational Databases(SQL)** | **Non-Relational Databases(No-SQL)** |
  |:----:|:---:|
  | Organize data into one or more tables | Organize data is anythong but a traditional table |
  | Each table has columns and rows | Key-Value Stores; Documents, Graphs |
  | A unique key identifies each row | Key-Value stores |

The NO-SQL database manage system seems like a document manage system, it's usually be used in Big Data analysis which needs massive data in which the SQL shows poor performance. Compared with the non-SQL, SQL is not friendly with opening source, that means u need pay some money to rent the software(e.g: [SqlYoung](https://webyog.com/product/sqlyog/)), but SQL is very popular in dialy traditional data analysis like the finance, shopping data, warehouse data and so no.

So if ur data is stuctured and has relation with each other, it's a best choice to use the SQL database, and if distributed and fragmentization is the main feature of the data, may the non-SQL performs well. But in fact, we usually combine the two brothers in dialy work.

The __SQL__:

Structured Query Language, is a common programming language which offen is used in __RDSMS([Relational Database Management System](https://en.wikipedia.org/wiki/Relational_data_stream_management_system))__ and __RDBMS__ to control the relational database system. And it's known as a basic component for Backend developers and many other IT engineers.

About the history of SQL, you can visit the [WiKi Page]((https://wikipedia.org/wiki/SQL)) for more information.

The __MySQL__:

which is know as the most popular SQL tripartite in recent 20 years, has been used in most internet companies all over the world, it began as an opening source software at first but was been bought by [The Oracle Company](https://www.oracle.com/index.html) finally in 2009. It has become a component of the four masterpieces which is called [LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle)) of opening source softwares.

And here is its [Wiki page](https://wikipedia.org/wiki/MySQL) that you can find more information about it.

----

## SQL Syntax

There have four basic parts in this chapter: Add, delete, set, select and it's easy for you to understand its means if your English is good. _BTW, it's very useful for your computer science learning if you try improving your English._

### CRUD(create read update delete)

#### __Before Beginning__[^1]
  
  * __Install the SQL service__
  Download the suitable version of [MySQL software](https://dev.mysql.com/downloads/mysql/).
  You should config the configuration file at first and take care of the client port and service port settings.
  Then just keep going with this [tutorial](https://www.runoob.com/mysql/mysql-install.html) and finish your installation.

  * __Config the environment variables__
  Use the `Win + R'` shortcut to run `sysdm.cpl` to find the computer's environment variables setting, which hids in the advanced option.
  Add the path of MySQL service into the user variables' path dict to run the MySQL in shell.
  Use the command `mysqld install` in shell with adminstrator to install the service so that you can set the status in `services.msc` and start it with Wndows.

  * __Connect the SQL Service__
  * After creating the SQL service and completing the configuration, there we need to connect the database system. U should use the command `mysqld --initialize` to initialize the SQL service and the `terminal` will give u the root administrator's initial password, input the command `mysql -h localhost -P port -u root -p` to connect the local SQl service and if it completed, there will show `mysql>` in the terminal and u can continue ur command with it.  
  _Notice: u should change the root user's password using the command `alter user set authentication_string=password("123456") where user='root';` at first!_
    
#### __Create and Insert__
    
  __Create some datebase about...__

  _There usually use the simple English words to express the SQL syntax as well as the other programming language:_

  `create database db_name;` -> To create DB library;

  `use db_name;` -> SWitch the cursor to dbname;

  `create table table_name(column1_name column1_type, column2_name colume2_type, etc);` -> To create an table named tablename in the database library you selected, which includes column1 and column2;

  After creating some empty table, the next thing we should solve is insert data into the target table,

  `insert into table_name(column1, colume2, etc) values(column1, colume2, etc), (column1, colume2, etc);` -> To add data into the target column of the table. *Attention: the numbers of the data should keep equality with the number of the columns.*

  so we have inserted some data into a table.

#### __Read and Query__
  
  Query is the basic part in daily data analysis work, it can help u filter data, integrate data and analyse the necessary data.

  __Basic syntax:__

  ```sql
      select <col.name> from <table.name> # (left join <table.name> on <requirement>) 
      where <requirement1> group by <col.name> 
      having <requirement2> 
      order by <col.name> limit <number, page>;
  ```

  It seems a little complex, but u can divide this command into three groups by the program execution order:
  
  1. Data Source -> `from <table.name> (left/right join <table.name> on <requirement>);`, this SQL command means it'll select data from table1 and table2 and present their **Cartesian Product**  and filter the result by the conditional statement(*requirement*).
  
  2. Conditional Statement -> `where <condition1> group by <col.name> having <condition2>;`, this command mainly determines the result. 
   
      > The execution order is 'where' -> 'group by' -> 'having', u should use the aggregate function like 'max(), min(), sum()',

  3. Result Filter -> `select <col.name> ... order by <col.name> limit <num, page>;`, this command determines the result we'll select from the association list, and how to show the result: order and page setting.
  
  __Extension:__
  
  In daily work, it's normal to combine different queries together.
  
  The child quiry will become a part of the father query, it usually plays the role as _result, conditional statement, the combined table._  

  For example:
  
  ```sql
     select *, (select s_name from students) stu_name from students 
     left join (select s_id, s_name, c_id, c_name from sourc) sources 
     on students.s_id = sources.s_id 
     where sources.s_id in (select s_id from teachers);
  ```
  _About the `join`, please read the [combination](#combination) part._
  _This part is an important baisc part of SQl._
  
#### __Update and Delete__

  We use these two commands to realize update/delete data operation.

  __Basic Syntax__

  * Update: `update <table_name> set <col.name1> = <value1>, <col.name2> = <value2> where <conditional_statement>;`
  * Delete Data: `delete from <table_name> where  <conditional_statement>;`  
    Delete Database: `drop database <database_name>;`
    Delect Table: `drop table <table_name>;`

  __Difference between `drop`, `delect` and `truncate`:__

  `Delete` command just do the special data deletion from table, but when the condition is set refer to the whole table, it seems like the `truncate table <table_name>` statement.

  It shows that Delete and Truncate won't delete table itself but this table's content, with the Drop command will delete the table wholly from database.

  **`Delect` command is a DML program statement, which means roll back operation is callable while `drop` and `truncate` are DLL statement without roll-back.**


### Combination

It's inevitable for us to extract data from different tables in a relational database when analysing data in dialy work, so there comes the combination syntax.

The combination rule relies on [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product), the command will return a Cartesian table based on target tables. And the left we need do is filtering out the impurites.

Let's import some tables:

`select * from Character; select * from Stories;`

**Character:**
| s_id | s_name | s_birth | s_gender |
| :---: | :---: | :---: | :---: |
| 01 | Leon | 1977-12-21 | man |
| 02 | Jack | 1992-05-20 | man |
| 03 | Sherry | 1986-07-01 | woman |
| 04 | Wesker | 1960-08-06 | man |
| 05 | Ada | 1974-03-02 | woman |
| 06 | Criss | 1973-01-20 | man |
_(the main characters' data from [Resident Evil](https://game.capcom.com/residentevil/en/), but there lose the birthday data so I draw up them.)_

**Stories**
| story_name | main_character | publish_time | good_review_rates |
| :---: | :---: | :---: | :---: |
| Resident Evil 4 | Leon | 28 Feb, 2014 | 91% |
| Resident Evi 6 | Jack | 22 Mar, 2013 | 80% |
| Resident Evil VII | Eason | 24 Jan, 2017 | 94% |
| Resident Evil Village | Criss | 7 May, 2021 | 95% |

##### Inner Join and Outer Join

**Syntax:**

* __inner join__: `select <col.name> from <table_name> join <table_name> on <conditional_statement>`
* __outer join__: `select <col.name> from <table_name> full join <table_name> on <conditional_statement>`

**Outer Join**, as known as `Full Join`, returns all records when there is a match in any one of the target tables, it'll fill the inexistent element with `Null`, in additional;

`select * from Character full join Stories on Character.s_name = Stories.main_character;`
| s_id | s_name | s_birth | s_gender | story_name | main_character | publish_time | good_review_rates |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 01 | Leon | 1977-12-21 | man | Resident Evil 4 | Leon | 28 Feb, 2014 | 91% |
| 02 | Jack | 1992-05-20 | man | Resident Evi 6 | Jack | 22 Mar, 2013 | 80% |
| 03 | Sherry | 1986-07-01 | woman |_Null_ | _Null_ | _Null_ | _Null_ |
| ... | ... | ... | ... | ... | ... | ... | ... |
|_Null_ | _Null_ | _Null_ | _Null_ | Resident Evil VII | Eason | 24 Jan, 2017 | 94% |

_(I just list the table's head part here, but please pay attention to the **Null**.)_

**Inner Join**, the default join type, will return the records when all target tables match the rules;

`select * from Character join Stories on Character.s_name = Stories.main_character;`
| s_id | s_name | s_birth | s_gender | story_name | main_character | publish_time | good_review_rates |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 01 | Leon | 1977-12-21 | man | Resident Evil 4 | Leon | 28 Feb, 2014 | 91% |
| 02 | Jack | 1992-05-20 | man | Resident Evi 6 | Jack | 22 Mar, 2013 | 80% |
| 06 | Criss | 1973-01-20 | man | Resident Evil Village | Criss | 7 May, 2021 | 95% |


In fact, we can image the tables as gathers in math.
| | |
|:--:|:--:|
|![](https://www.runoob.com/wp-content/uploads/2013/09/img_innerjoin.gif)|![](https://www.runoob.com/wp-content/uploads/2013/09/img_fulljoin.gif)


-----
[^1]: u should import the practice SQL data into ur database, here we have three database to practice and it's easy to find some practice questions in mang websites.