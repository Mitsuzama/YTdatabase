@ delete.sql

host echo Se construiesc tabelele. Va rugam asteptati

-----------------------------------------------TABELE-------------------------------------

CREATE TABLE role(
    role_id NUMBER(1) NOT NULL,
    role_type VARCHAR(10) NOT NULL,
    CONSTRAINT role_id_pk PRIMARY KEY(role_id)
);

CREATE TABLE users(
    user_id NUMBER(3) NOT NULL,
    first_name VARCHAR2(20) NOT NULL UNIQUE,
    last_name VARCHAR2(20) NOT NULL,
    age NUMBER(2) NOT NULL,
    city VARCHAR(15) NOT NULL,
    email VARCHAR2(30) NOT NULL UNIQUE,
    role_type VARCHAR(10) NOT NULL,
    CONSTRAINT user_id_pk PRIMARY KEY(user_id),
    CONSTRAINT email_ch CHECK (email = '%_@__%.__%'),
    CONSTRAINT role_type_fk FOREIGN KEY (role_id) REFERENCES role
);

CREATE TABLE videos(
    video_id NUMBER(3) NOT NULL,
    title VARCHAR2(50) NOT NULL UNIQUE,
    user_id VARCHAR2(20) NOT NULL,
    no_of_likes NUMBER(10) NOT NULL,
    CONSTRAINT video_id_pk PRIMARY KEY(video_id),
    CONSTRAINT email_ch CHECK (email = '%_@__%.__%'),
    CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES users
);

CREATE TABLE video_comment(
    comment_id NUMBER(3) NOT NULL,
    user_id NUMBER(3) NOT NULL,
    video_id NUMBER(3) NOT NULL,
    comment VARCHAR(250) NOT NULL,
    CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES users,
    CONSTRAINT video_id_fk FOREIGN KEY (video_id) REFERENCES videos
);

CREATE TABLE login_account(
    user_id NUMBER(3) NOT NULL,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(16),
    CONSTRAINT password_check CHECK (length(password) >= 8 AND length(password)<=16)
);

------------------------------------------POPULAREA TABELELOR----------------------------

INSERT INTO role VALUES (1, 'user');
INSERT INTO role VALUES (2, 'admin');


INSERT INTO users VALUES (1,  'Paraschiva', 'Pristanda',    18, 'Iasi',         'paraschiva@yahoo.com' , 'admin);
INSERT INTO users VALUES (2,  'Paula',      'Horea',        34, 'Galati',       'daniel@yahoo.com');
INSERT INTO users VALUES (3,  'Demetra',    'Daniel',       21, 'Bacau',        'paraschiva@yahoo.com');
INSERT INTO users VALUES (4,  'Stefania',   'Petru',        9,  'Arad',         'petru@yahoo.com');
INSERT INTO users VALUES (5,  'Rares',      'Veronica',     37, 'Olt',          'veronica@yahoo.com');
INSERT INTO users VALUES (6,  'Sorin',      'Antalupei',    14, 'Cluj',         'antalupei@yahoo.com');
INSERT INTO users VALUES (7,  'Ava',        'Bishop',       18, 'Philadelphia', 'bishop@yahoo.com');
INSERT INTO users VALUES (8,  'River',      'Austin',       34, 'Chongqing',    'austin@yahoo.com');
INSERT INTO users VALUES (9,  'Alex',       'Bailey',       21, 'Miami',        'bailey@yahoo.com');
INSERT INTO users VALUES (10, 'Arianne',    'Coombes',      9,  'Tokyo',        'coombes@yahoo.com');
INSERT INTO users VALUES (11, 'Maximus',    'Bean',         37, 'Gaborone',     'bean@yahoo.com');
INSERT INTO users VALUES (12, 'Anish',      'Farrington',   14, 'Nashville',    'farrington@yahoo.com');
INSERT INTO users VALUES (13, 'Rico',       'Beech',        18, 'Vienna',       'beech@yahoo.com');
INSERT INTO users VALUES (14, 'Aysha',      'Orr',          34, 'Bratislava',   'orr@yahoo.com');
INSERT INTO users VALUES (15, 'Tammy',      'Gunn',         21, 'Manila',       'gunn@yahoo.com');
INSERT INTO users VALUES (16, 'Abu',        'Vaughan',      9,  'Dubai',        'vaughan@yahoo.com');
INSERT INTO users VALUES (17, 'Dorian',     'Holland',      37, 'Brussels',     'holland@yahoo.com');
INSERT INTO users VALUES (18, 'Hudson',     'Dixon',        14, 'Bern',         'dixon@yahoo.com');
INSERT INTO users VALUES (19, 'Fionn',      'Hall',         18, 'Ottawa',       'hall@yahoo.com');
INSERT INTO users VALUES (20, 'Jaeden',     'Bowden',       34, 'Split',        'bowden@yahoo.com');
INSERT INTO users VALUES (21, 'Hania',      'Faulkner',     21, 'Frankfurt',    'faulkner@yahoo.com');
INSERT INTO users VALUES (22, 'Rudi',       'Singh',        9,  'Riyadh',       'singh@yahoo.com');
INSERT INTO users VALUES (23, 'Caden',      'Mckee',        37, 'Monaco',       'mckee@yahoo.com');
INSERT INTO users VALUES (24, 'Sahib',      'Coombes',      14, 'Nairobi',      'coombes@yahoo.com');
INSERT INTO users VALUES (25, 'Lee',        'Mcbride',      18, 'Sydney',       'mcbride@yahoo.com');
INSERT INTO users VALUES (26, 'Macey',      'Mullen',       34, 'Quito',        'mullen@yahoo.com');
INSERT INTO users VALUES (27, 'Deniz',      'Franco',       21, 'Bishkek',      'franco@yahoo.com');
INSERT INTO users VALUES (28, 'Blythe',     'Joseph',       9,  'Belgrade',     'joseph@yahoo.com');
INSERT INTO users VALUES (29, 'Tyrell',     'Tucker',       37, 'Shanghai',     'tucker@yahoo.com');
INSERT INTO users VALUES (30, 'Koby',       'Oliver',       14, 'Mexico',       'oliver@yahoo.com');
INSERT INTO users VALUES (31, 'Willa',      'Cash',         18, 'Freetown',     'cash@yahoo.com');
INSERT INTO users VALUES (32, 'Rylee',      'Rosas',        34, 'Kathmandu',    'rosas@yahoo.com');
INSERT INTO users VALUES (33, 'Courtney',   'Pierce',       21, 'Bologna',      'pierce@yahoo.com');
INSERT INTO users VALUES (34, 'Wade',       'Villanueva',   9,  'New York',     'villanueva@yahoo.com');
INSERT INTO users VALUES (35, 'Riley',      'Greenaway',    37, 'Dushanbe',     'greenaway@yahoo.com');
INSERT INTO users VALUES (36, 'Mica',       'Cosmin',       14, 'Warsaw',       'cosmin@yahoo.com');


INSERT INTO videos VALUES ( 1,  '10 MIN FULL BODY STRETCHING',                  36, 1913627);
INSERT INTO videos VALUES ( 2,  'Next Gen Graphics Is Kinda Nuts..',            1,  1913627);
INSERT INTO videos VALUES ( 3,  'Kygo - Love Me Now',                           26, 1913627);
INSERT INTO videos VALUES ( 4,  'How Science Got Us to 2020 ',                  1,  1913627);
INSERT INTO videos VALUES ( 5,  'Amazing Science Experiments to Try at Home',   27, 1913627);
INSERT INTO videos VALUES ( 6,  'Agent Crime Action Movie Full Length',         26, 1913627);
INSERT INTO videos VALUES ( 7,  'The Bad Seed Kids Book Read Aloud',            24, 1913627);
INSERT INTO videos VALUES ( 8,  'THE COUCH POTATO',                             1,  1913627);
INSERT INTO videos VALUES ( 9,  'Baby Shark',                                   34, 1913627);
INSERT INTO videos VALUES (10,  'Noone is reading my names in this database',   36, 1913627);
INSERT INTO videos VALUES (11,  'Cancel or pause your YouTube TV membership',   7,  1913627);
INSERT INTO videos VALUES (12,  'Router basics for absolute begginers',         4,  1913627);
INSERT INTO videos VALUES (13,  'How To Use A Router',                          34, 1913627);
INSERT INTO videos VALUES (14,  'Razer Kraken Kitty Edition ',                  1,  1913627);
INSERT INTO videos VALUES (15,  'The Monitor Buying Guide',                     36, 1913627);
INSERT INTO videos VALUES (16,  'Top Pens Of All Time',                         25, 1913627);
INSERT INTO videos VALUES (17,  'Really, noone read them',                      22, 1913627);
INSERT INTO videos VALUES (18,  'IS THIS the BEST PEN? - Ink Pen Battle!',      23, 1913627);
INSERT INTO videos VALUES (19,  'I Could Watch Flowers',                        1,  1913627);
INSERT INTO videos VALUES (20,  'Beautiful flowers',                            17, 1913627);
INSERT INTO videos VALUES (21,  'FLOWERS CAN DANCE!!! ',                        3,  1913627);
INSERT INTO videos VALUES (22,  'Pls read my video names',                      1,  1913627);















