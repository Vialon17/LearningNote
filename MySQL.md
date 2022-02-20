# MySQl Learning Note

**It's so funny that I have to `Reinvent the Wheel`, lol~**

*But you couldn't oppose it because it can improve ur comprehension of the target*🤣 🤣 🤣

## About MySQL

The __SQL__:

Structured Query Language, is a common programming language which offen is used in __RDSMS([Relational Database Management System](https://en.wikipedia.org/wiki/Relational_data_stream_management_system))__ and __RDBMS__ to control the relational database system. And it's known as a basic component for Backend developers and many other IT engineers.

About the history of SQL, you can visit the [WiKi Page]((https://wikipedia.org/wiki/SQL)) for more information.

The __MySQL__:

which is know as the most popular SQL tripartite in recent 20 years, has been used in most internet companies all over the world, it began as an opening source software at first but was been bought by [The Oracle Company](https://www.oracle.com/index.html) finally in 2009. It has become a component of the four masterpieces which is called [LAMP](https://wikipedia.org/wiki/LAMP) of opening source softwares.

And here is its [Wiki page](https://wikipedia.org/wiki/MySQL) that you can find more information about it.

----

## SQL Syntax

There have four basic parts in this chapter: Add, delete, set, select and it's easy for you to understand its means if your English is good. _BTW, it's very useful for your computer science learning if you try improving your English._

### Basic Syntax

* __Before Beginning__
  
     * __Install the SQL service__
     Download the suitable version of [MySQL software](https://dev.mysql.com/downloads/mysql/).
     You should config the configuration file at first and take care of the client port and service port settings.
     Then just keep going with this [tutorial](https://www.runoob.com/mysql/mysql-install.html) and finish your installation.

     * __Config the environment variables__
     Use the `Win + R'` shortcut to run `sysdm.cpl` to find the computer's environment variables setting, which hids in the advanced option.
     Add the path of MySQL service into the user variables' path dict to run the MySQL in shell.
     Use the command `mysqld install` in shell with adminstrator to install the service so that you can set the status in `services.msc` and start it with Wndows.
    
* __Add and Insert__
    
    * __Create some datebase about...__
  
        *There usually use the simple English words to express the SQL syntax as well as the other programming language:*

      > `create database db_name` -> To create DB library;
      >
      > `use db_name` -> SWitch the cursor to dbname;
      >
      > `create table table_name(column1_name column1_type, column2_name colume2_type, etc)` -> To create an table named tablename in the database library you selected, which includes column1 and column2;
      >
      > After creating some empty table, the next thing we should solve is insert data into the target table,
      >
      > `insert into table_name(column1, colume2, etc) values(column1, colume2, etc), (column1, colume2, etc)` -> To add data into the target column of the table. *Attention: the numbers of the data should keep equality with the number of the columns.*
        
        
