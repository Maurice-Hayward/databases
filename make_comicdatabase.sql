/* clean up old tables;
   gotta drop the old stuff with foreign keys
   cuz of constraints
*/

delete from event;
drop table event;

delete from character;
drop table character;

delete from creator;
drop table creator;

delete from comic;
drop table comic;

create table comic
   (id			varchar(15)	not null unique,
    title		varchar(30)	not null.
    issue_num		int		not null,
    issue_date		varchar(20)	not null,
    series_title	varchar(30)	not null,
    series_id		varchar(15)	not null,
    release_price	float(53)	not null,
    primary key(id));

create table creator
   (id			varchar(15)	not null unique,
    name		varchar(15)	not null,
    primary key(id));

create table character
   (id			varchar(15)	not null unique,
    name		varchar(15)	not null,
    description		varchar(100)	not null,
    species		varchar(15)	not null,
    first_appearance	varchar(15)	not null,
    primary key(id),
    foreign key(first_appearance) references comic(issue_date))
GO
create table alias
   (alias_name		varchar(15)	not null unique,
    primary key(alias_name),
    char_id		varchar(15) 	not null references character(id) on delete cascade)
GO
create table ability
   (ability_name	varchar(15)	not null unique,
    primary key (ability_name),
    char_id		varchar(15)	not null references character(id) on delete cascade);

create table event
   (id			varchar(15)	not null unique,
    title		varchar(30)	not null,
    description		varchar(100)	not null,
    first_issue		varchar(15)	not null,
    last_issue		varchar(15)	not null,
    event_seq		varchar(15)	not null,
    foreign key (first_issue) references comic,
    foreign key (last_issue) references comic,
    foreign key (event_seq) references event,
    primary key (id));
