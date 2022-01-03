@ delete.sql

host echo Se construiesc tabelele. Va rugam asteptati

-----------------------------------------------TABELE-------------------------------------

CREATE TABLE roles(
    role_id NUMBER(2) NOT NULL,
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
    CONSTRAINT role_type_fk FOREIGN KEY (role_id) REFERENCES roles
);

CREATE TABLE videos(
    video_id NUMBER(3) NOT NULL,
    title VARCHAR2(50) NOT NULL UNIQUE,
    user_id VARCHAR2(20) NOT NULL,
    no_of_likes NUMBER(10) NOT NULL,
    CONSTRAINT video_id_pk PRIMARY KEY(video_id),
    CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES users
);

CREATE TABLE video_comment(
    comment_id NUMBER(3) NOT NULL,
    user_id NUMBER(3) NOT NULL,
    video_id NUMBER(3) NOT NULL,
    comment VARCHAR(250) NOT NULL,
    CONSTRAINT comment_id_pk PRIMARY KEY (user_id),
    CONSTRAINT user_id_video_comment_fk FOREIGN KEY (user_id) REFERENCES users,
    CONSTRAINT video_id_video_comment_fk FOREIGN KEY (video_id) REFERENCES videos
);

CREATE TABLE login_account(
    user_id NUMBER(3) NOT NULL,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(16),
    CONSTRAINT user_id_log_pk PRIMARY KEY (user_id),
    CONSTRAINT password_check CHECK (length(password) >= 8 AND length(password)<=16),
    CONSTRAINT user_id_log_fk FOREIGN KEY (user_id) REFERENCES users
);















