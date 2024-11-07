-- 1. Create the database (run this if database does not exist)

-- Uncomment the following lines if you need to create the database
-- CREATE DATABASE project_database;

-- 2. Connect to the database: \c sd_foodbank_database;
--                    

-- 3. Create Tables
CREATE TABLE IF NOT EXISTS "user" (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number BIGINT,
    email VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS appointment (
    appointment_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "user" (user_id) ON DELETE CASCADE,
    appointment_time TIMESTAMP NOT NULL,
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS conversation_logs (
    log_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "user" (user_id) ON DELETE SET NULL,
    option_id INT REFERENCES bot_choices (option_id) ON DELETE SET NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    speech_to_text TEXT,
    decision VARCHAR(255),
    intent VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS bot_choices (
    option_id SERIAL PRIMARY KEY,
    option_text TEXT NOT NULL,
    intent VARCHAR(255),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS faq (
    faq_id SERIAL PRIMARY KEY,
    language VARCHAR(10),
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- If we want to insert some sample data for testing:
-- INSERT INTO "user" (name, phone_number, email) VALUES ('John Doe', 1234567890, 'johndoe@example.com');
-- INSERT INTO appointment (user_id, appointment_time) VALUES (1, '2024-11-10 10:00:00');

