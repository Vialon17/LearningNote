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

which is know as the most popular SQL tripartite in recent 20 years, has been used in most internet companies all over the world, it began as an opening source software at first but was been bought by [The Oracle Company](https://www.oracle.com/index.html) finally in 2009. It has become a component of the four masterpieces which is called [LAMP](https://wikipedia.org/wiki/LAMP) of opening source softwares.

And here is its [Wiki page](https://wikipedia.org/wiki/MySQL) that you can find more information about it.

----

## SQL Syntax

There have four basic parts in this chapter: Add, delete, set, select and it's easy for you to understand its means if your English is good. _BTW, it's very useful for your computer science learning if you try improving your English._

### CRUD(create read update delete)

* __Before Beginning__[^1]
  
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
    
* __Create and Insert__
    
    __Create some datebase about...__

    _There usually use the simple English words to express the SQL syntax as well as the other programming language:_

    > `create database db_name` -> To create DB library;
    >
    > `use db_name` -> SWitch the cursor to dbname;
    >
    > `create table table_name(column1_name column1_type, column2_name colume2_type, etc)` -> To create an table named tablename in the database library you selected, which includes column1 and column2;
    >
    > After creating some empty table, the next thing we should solve is insert data into the target table,
    >
    > `insert into table_name(column1, colume2, etc) values(column1, colume2, etc), (column1, colume2, etc)` -> To add data into the target column of the table. *Attention: the numbers of the data should keep equality with the number of the columns.*

    so we have inserted some data into a table.

* __Read and Query__
  
[^1]: u should import the practice SQL data into ur database, here we have three database to practice and it's easy to find some practice questions in mang websites.