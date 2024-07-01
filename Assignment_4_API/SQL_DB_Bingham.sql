CREATE DATABASE Bingham;
USE Bingham;

CREATE TABLE MembersClub(
member_id int not null,
surname varchar(50) not null,
phone_number char(11) not null,
joined_date date not null,
room varchar(50) not null,
CONSTRAINT pk_MembersClub PRIMARY KEY (member_id)
);


INSERT INTO MembersClub
(member_id, surname, phone_number, joined_date, room)
VALUES
(145, "LACOSTE", "07847312950", "2019-05-05", "Library"),
(885, "GUCCI", "07847312955", "2019-06-06", "Restaurant"),
(749, "VERSACE", "07847312888", "2019-01-01", "Library"),
(345, "MALONE", "07847333950", "2019-02-02", "Library"),
(256, "GOGOLO", "07787312950", "2019-03-03", "Restaurant"),
(184, "PARMA", "07787312950", "2019-04-04", "Parlour"),
(553, "SAPSANI", "07787312871", "2019-07-07", "Restaurant"),
(457,"GOLONI", "07787312084", "2019-08-08", "Parlour"),
(305,"PAPADOPOULOS", "07787312000", "2019-09-09", "Parlour"),
(113,"KARAS", "07787312433", "2019-10-10", "Parlour");