@ delete.sql

-----------------------------------------------TABELE
CREATE TABLE users(
    user_id NUMBER(3) NOT NULL,
    first_name VARCHAR2(20) NOT NULL UNIQUE,
    last_name VARCHAR2(20) NOT NULL,
    age NUMBER(2) NOT NULL,
    city VARCHAR(15) NOT NULL,
    email VARCHAR2(30) NOT NULL UNIQUE,
    CONSTRAINT user_id_pk PRIMARY KEY(user_id),
    CONSTRAINT email_ch CHECK (email = '%_@__%.__%')
);

INSERT INTO users VALUES (1, 'Paraschiva', 'Pristanda', 18, 'Iasi', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (2, 'Paula', 'Horea', 34, 'Galati', 'daniel@yahoo.com');
INSERT INTO users VALUES (3, 'Demetra', 'Daniel', 21, 'Bacau', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (4, 'Stefania', 'Petru', 9, 'Arad', 'petru@yahoo.com');
INSERT INTO users VALUES (5, 'Rares', 'Veronica', 37, 'Olt', 'veronica@yahoo.com');
INSERT INTO users VALUES (6, 'Sorin', 'Antalupei', 14, 'Cluj', 'antalupei@yahoo.com');


INSERT INTO users VALUES (7, 'Ava', 'Bishop', 18, 'Iasi', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (8, 'River', 'Austin', 34, 'Galati', 'daniel@yahoo.com');
INSERT INTO users VALUES (9, 'Alex', 'Bailey', 21, 'Bacau', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (10, 'Arianne', 'Coombes', 9, 'Arad', 'petru@yahoo.com');
INSERT INTO users VALUES (11, 'Maximus', 'Bean', 37, 'Olt', 'veronica@yahoo.com');
INSERT INTO users VALUES (12, 'Anish', 'Farrington', 14, 'Cluj', 'antalupei@yahoo.com');
INSERT INTO users VALUES (13, 'Rico', 'Beech', 18, 'Iasi', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (14, 'Aysha', 'Orr', 34, 'Galati', 'daniel@yahoo.com');
INSERT INTO users VALUES (15, 'Tammy', 'Gunn', 21, 'Bacau', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (16, 'Abu', 'Vaughan', 9, 'Arad', 'petru@yahoo.com');
INSERT INTO users VALUES (17, 'Rares', 'Veronica', 37, 'Olt', 'veronica@yahoo.com');
INSERT INTO users VALUES (18, 'Sorin', 'Antalupei', 14, 'Cluj', 'antalupei@yahoo.com');
INSERT INTO users VALUES (19, 'Paraschiva', 'Pristanda', 18, 'Iasi', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (20, 'Paula', 'Horea', 34, 'Galati', 'daniel@yahoo.com');
INSERT INTO users VALUES (21, 'Demetra', 'Daniel', 21, 'Bacau', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (22, 'Stefania', 'Petru', 9, 'Arad', 'petru@yahoo.com');
INSERT INTO users VALUES (23, 'Rares', 'Veronica', 37, 'Olt', 'veronica@yahoo.com');
INSERT INTO users VALUES (24, 'Sorin', 'Antalupei', 14, 'Cluj', 'antalupei@yahoo.com');
INSERT INTO users VALUES (25, 'Paraschiva', 'Pristanda', 18, 'Iasi', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (26, 'Paula', 'Horea', 34, 'Galati', 'daniel@yahoo.com');
INSERT INTO users VALUES (27, 'Demetra', 'Daniel', 21, 'Bacau', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (28, 'Stefania', 'Petru', 9, 'Arad', 'petru@yahoo.com');
INSERT INTO users VALUES (29, 'Rares', 'Veronica', 37, 'Olt', 'veronica@yahoo.com');
INSERT INTO users VALUES (30, 'Sorin', 'Antalupei', 14, 'Cluj', 'antalupei@yahoo.com');
INSERT INTO users VALUES (31, 'Paraschiva', 'Pristanda', 18, 'Iasi', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (32, 'Paula', 'Horea', 34, 'Galati', 'daniel@yahoo.com');
INSERT INTO users VALUES (33, 'Demetra', 'Daniel', 21, 'Bacau', 'paraschiva@yahoo.com');
INSERT INTO users VALUES (34, 'Stefania', 'Petru', 9, 'Arad', 'petru@yahoo.com');
INSERT INTO users VALUES (35, 'Rares', 'Veronica', 37, 'Olt', 'veronica@yahoo.com');
INSERT INTO users VALUES (36, 'Sorin', 'Antalupei', 14, 'Cluj', 'antalupei@yahoo.com');



CREATE TABLE video(
    video_id NUMBER(3) NOT NULL,
    title VARCHAR2(50) NOT NULL UNIQUE,
    user_id VARCHAR2(20) NOT NULL,
    no_of_likes NUMBER(6) NOT NULL,
    CONSTRAINT video_id_pk PRIMARY KEY(video_id),
    CONSTRAINT email_ch CHECK (email = '%_@__%.__%')
);