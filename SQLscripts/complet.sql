create database ytdatabase;
use ytdatabase;
show tables;
select * from users;

DROP TABLE login_account;
DROP TABLE video_comment;
DROP TABLE videos;
DROP TABLE users;
DROP TABLE roles;

CREATE TABLE roles(
                role_id INTEGER PRIMARY KEY NOT NULL,
                role_type VARCHAR(255) UNIQUE NOT NULL
            );

CREATE TABLE users(
                user_id INTEGER PRIMARY KEY NOT NULL,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                age INTEGER,
                city TEXT,
                email TEXT,
                role_type VARCHAR(255) NOT NULL,
                FOREIGN KEY (role_type) REFERENCES roles(role_type) ON DELETE CASCADE
            );

CREATE TABLE videos(
                video_id INTEGER PRIMARY KEY NOT NULL,
                title VARCHAR(255) NOT NULL UNIQUE,
                user_id INTEGER NOT NULL,
                no_of_likes INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            );

CREATE TABLE video_comment(
                comment_id INTEGER PRIMARY KEY NOT NULL,
                user_id INTEGER NOT NULL,
                video_id INTEGER NOT NULL,
                comments TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (video_id) REFERENCES videos(video_id) ON DELETE CASCADE
            );

CREATE TABLE login_account(
                user_id INTEGER PRIMARY KEY NOT NULL,
                username VARCHAR(255) NOT NULL,
                user_password VARCHAR(20),
                CONSTRAINT password_check CHECK (length(user_password) >= 1 AND length(user_password)<=16),
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            );            

INSERT INTO roles VALUES (1, 'user');
INSERT INTO roles VALUES (2, 'admin');

INSERT INTO users VALUES (1,  'Paraschiva', 'Pristanda',    18, 'Iasi',         'paraschiva@yahoo.com'  , 'admin');
INSERT INTO users VALUES (2,  'Paula',      'Horea',        34, 'Galati',       'daniel@yahoo.com'      , 'user');
INSERT INTO users VALUES (3,  'Demetra',    'Daniel',       21, 'Bacau',        'paraschiva@yahoo.com'  , 'user');
INSERT INTO users VALUES (4,  'Stefania',   'Petru',        9,  'Arad',         'petru@yahoo.com'       , 'user');
INSERT INTO users VALUES (5,  'Rares',      'Veronica',     37, 'Olt',          'veronica@yahoo.com'    , 'user');
INSERT INTO users VALUES (6,  'Sorin',      'Antalupei',    14, 'Cluj',         'antalupei@yahoo.com'   , 'user');
INSERT INTO users VALUES (7,  'Ava',        'Bishop',       18, 'Philadelphia', 'bishop@yahoo.com'      , 'user');
INSERT INTO users VALUES (8,  'River',      'Austin',       34, 'Chongqing',    'austin@yahoo.com'      , 'user');
INSERT INTO users VALUES (9,  'Alex',       'Bailey',       21, 'Miami',        'bailey@yahoo.com'      , 'user');
INSERT INTO users VALUES (10, 'Arianne',    'Coombes',      9,  'Tokyo',        'coombes@yahoo.com'     , 'user');
INSERT INTO users VALUES (11, 'Maximus',    'Bean',         37, 'Gaborone',     'bean@yahoo.com'        , 'user');
INSERT INTO users VALUES (12, 'Anish',      'Farrington',   14, 'Nashville',    'farrington@yahoo.com'  , 'user');
INSERT INTO users VALUES (13, 'Rico',       'Beech',        18, 'Vienna',       'beech@yahoo.com'       , 'user');
INSERT INTO users VALUES (14, 'Aysha',      'Orr',          34, 'Bratislava',   'orr@yahoo.com'         , 'user');
INSERT INTO users VALUES (15, 'Tammy',      'Gunn',         21, 'Manila',       'gunn@yahoo.com'        , 'user');
INSERT INTO users VALUES (16, 'Abu',        'Vaughan',      9,  'Dubai',        'vaughan@yahoo.com'     , 'user');
INSERT INTO users VALUES (17, 'Dorian',     'Holland',      37, 'Brussels',     'holland@yahoo.com'     , 'user');
INSERT INTO users VALUES (18, 'Hudson',     'Dixon',        14, 'Bern',         'dixon@yahoo.com'       , 'user');
INSERT INTO users VALUES (19, 'Fionn',      'Hall',         18, 'Ottawa',       'hall@yahoo.com'        , 'user');
INSERT INTO users VALUES (20, 'Jaeden',     'Bowden',       34, 'Split',        'bowden@yahoo.com'      , 'user');
INSERT INTO users VALUES (21, 'Hania',      'Faulkner',     21, 'Frankfurt',    'faulkner@yahoo.com'    , 'user');
INSERT INTO users VALUES (22, 'Rudi',       'Singh',        9,  'Riyadh',       'singh@yahoo.com'       , 'user');
INSERT INTO users VALUES (23, 'Caden',      'Mckee',        37, 'Monaco',       'mckee@yahoo.com'       , 'user');
INSERT INTO users VALUES (24, 'Sahib',      'Coombes',      14, 'Nairobi',      'coombes@yahoo.com'     , 'user');
INSERT INTO users VALUES (25, 'Lee',        'Mcbride',      18, 'Sydney',       'mcbride@yahoo.com'     , 'user');
INSERT INTO users VALUES (26, 'Macey',      'Mullen',       34, 'Quito',        'mullen@yahoo.com'      , 'user');
INSERT INTO users VALUES (27, 'Deniz',      'Franco',       21, 'Bishkek',      'franco@yahoo.com'      , 'user');
INSERT INTO users VALUES (28, 'Blythe',     'Joseph',       9,  'Belgrade',     'joseph@yahoo.com'      , 'user');
INSERT INTO users VALUES (29, 'Tyrell',     'Tucker',       37, 'Shanghai',     'tucker@yahoo.com'      , 'user');
INSERT INTO users VALUES (30, 'Koby',       'Oliver',       14, 'Mexico',       'oliver@yahoo.com'      , 'user');
INSERT INTO users VALUES (31, 'Willa',      'Cash',         18, 'Freetown',     'cash@yahoo.com'        , 'user');
INSERT INTO users VALUES (32, 'Rylee',      'Rosas',        34, 'Kathmandu',    'rosas@yahoo.com'       , 'user');
INSERT INTO users VALUES (33, 'Courtney',   'Pierce',       21, 'Bologna',      'pierce@yahoo.com'      , 'user');
INSERT INTO users VALUES (34, 'Wade',       'Villanueva',   9,  'New York',     'villanueva@yahoo.com'  , 'user');
INSERT INTO users VALUES (35, 'Riley',      'Greenaway',    37, 'Dushanbe',     'greenaway@yahoo.com'   , 'user');
INSERT INTO users VALUES (36, 'Mica',       'Cosmin',       14, 'Warsaw',       'cosmin@yahoo.com'      , 'user');



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

INSERT INTO video_comment VALUES(1, 3, 14, 'Beautiful execution!');
INSERT INTO video_comment VALUES(2, 4, 16, 'Incredible!');
INSERT INTO video_comment VALUES(3, 7, 2, 'Cant wait for the next one');
INSERT INTO video_comment VALUES(4, 30, 1, 'I dont know the language');


            
INSERT INTO login_account VALUES (1,  'Paraschiva', 'Pristanda');
INSERT INTO login_account VALUES (2,  'Paula',      'Horea');
INSERT INTO login_account VALUES (3,  'Demetra',    'Daniel');
INSERT INTO login_account VALUES (4,  'Stefania',   'Petru');
INSERT INTO login_account VALUES (5,  'Rares',      'Veronica');
INSERT INTO login_account VALUES (6,  'Sorin',      'Antalupei');
INSERT INTO login_account VALUES (7,  'Ava',        'Bishop');
INSERT INTO login_account VALUES (8,  'River',      'Austin');
INSERT INTO login_account VALUES (9,  'Alex',       'Bailey');
INSERT INTO login_account VALUES (10, 'Arianne',    'Coombes');
INSERT INTO login_account VALUES (11, 'Maximus',    'Bean');
INSERT INTO login_account VALUES (12, 'Anish',      'Farrington');
INSERT INTO login_account VALUES (13, 'Rico',       'Beech');
INSERT INTO login_account VALUES (14, 'Aysha',      'Orr');
INSERT INTO login_account VALUES (15, 'Tammy',      'Gunn');
INSERT INTO login_account VALUES (16, 'Abu',        'Vaughan');
INSERT INTO login_account VALUES (17, 'Dorian',     'Holland');
INSERT INTO login_account VALUES (18, 'Hudson',     'Dixon');
INSERT INTO login_account VALUES (19, 'Fionn',      'Hall');
INSERT INTO login_account VALUES (20, 'Jaeden',     'Bowden');
INSERT INTO login_account VALUES (21, 'Hania',      'Faulkner');
INSERT INTO login_account VALUES (22, 'Rudi',       'Singh');
INSERT INTO login_account VALUES (23, 'Caden',      'Mckee');
INSERT INTO login_account VALUES (24, 'Sahib',      'Coombes');
INSERT INTO login_account VALUES (25, 'Lee',        'Mcbride');
INSERT INTO login_account VALUES (26, 'Macey',      'Mullen');
INSERT INTO login_account VALUES (27, 'Deniz',      'Franco');
INSERT INTO login_account VALUES (28, 'Blythe',     'Joseph');
INSERT INTO login_account VALUES (29, 'Tyrell',     'Tucker');
INSERT INTO login_account VALUES (30, 'Koby',       'Oliver');
INSERT INTO login_account VALUES (31, 'Willa',      'Cash');
INSERT INTO login_account VALUES (32, 'Rylee',      'Rosas');
INSERT INTO login_account VALUES (33, 'Courtney',   'Pierce');
INSERT INTO login_account VALUES (34, 'Wade',       'Villanueva');
INSERT INTO login_account VALUES (35, 'Riley',      'Greenaway');
INSERT INTO login_account VALUES (36, 'Mica',       'Cosmin');

