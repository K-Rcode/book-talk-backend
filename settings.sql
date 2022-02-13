DROP DATABASE book_talk;
DROP USER book_talkusers;

CREATE DATABASE book_talk;
CREATE USER book_talkusers WITH PASSWORD 'book_talk';
GRANT ALL PRIVILEGES ON DATABASE book_talk TO book_talkusers;