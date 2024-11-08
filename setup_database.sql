-- 1. Create the database (run this if database does not exist)

-- Uncomment the following lines if you need to create the database
-- CREATE DATABASE sb_foodbank_intro_project_database;

-- 2. Connect to the database: \c sd_foodbank_database;
--                    

-- 3. Create Tables
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user' 
);

CREATE TABLE IF NOT EXISTS posts (
    post_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP 
);

CREATE TABLE IF NOT EXISTS comments (
    comment_id SERIAL PRIMARY KEY,
    post_id INT REFERENCES posts(post_id),
    user_id INT REFERENCES users(user_id),
    content TEXT NOT NULL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP 
);

-- If we want to insert some sample data for testing:
-- INSERT INTO "user" (name, phone_number, email) VALUES ('John Doe', 1234567890, 'johndoe@example.com');
-- INSERT INTO appointment (user_id, appointment_time) VALUES (1, '2024-11-10 10:00:00');

