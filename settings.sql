DROP DATABASE book_talk;
DROP USER book_talkuser;

CREATE DATABASE book_talk;
CREATE USER book_talkuser WITH PASSWORD 'book_talk';
GRANT ALL PRIVILEGES ON DATABASE book_talk TO book_talkuser;