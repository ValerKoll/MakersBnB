-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.


-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS availabilities;
DROP SEQUENCE IF EXISTS availabilities_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(255),
  email_address VARCHAR(255),
  passcode VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  descr VARCHAR(255),
  price float4,
  user_id INTEGER
);

CREATE SEQUENCE IF NOT EXISTS availabilities_id_seq;
CREATE TABLE availabilities (
  id SERIAL PRIMARY KEY,
  date_from DATE,
  date_to DATE,
  space_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (fullname, email_address, passcode) VALUES ('Peter Pan', 'peterpan', 'peter&1234');
INSERT INTO users (fullname, email_address, passcode) VALUES ('Jenny Mill', 'notsoFar', 'docker&1234');
INSERT INTO users (fullname, email_address, passcode) VALUES ('kevin Tosh', 'kevin-90', 'linux456789!');

INSERT INTO spaces (name, descr, price, user_id) VALUES ('Villa Kitty', 'A light, warm, and modern space for a gathering.  Wonderful outdoor living.  Beautiful gardens in Area of Outstanding Natural Beauty in the High Weald . Lovely walks', 70.00, 1);
INSERT INTO spaces (name, descr, price, user_id) VALUES ('Perro House', 'A light, warm, and modern space for a gathering.  Wonderful outdoor living.  Beautiful gardens in Area of Outstanding Natural Beauty in the High Weald . Lovely walks', 35.00, 3);
INSERT INTO spaces (name, descr, price, user_id) VALUES ('Parrot Delight', 'A light, warm, and modern space for a gathering.  Wonderful outdoor living.  Beautiful gardens in Area of Outstanding Natural Beauty in the High Weald . Lovely ', 80.00, 2);
INSERT INTO spaces (name, descr, price, user_id) VALUES ('Casa Burro', 'A light, warm, and modern space for a gathering.  Wonderful outdoor living.  Beautiful gardens in Area of Outstanding Natural Beauty in the High Weald . Love', 45.00, 1);

INSERT INTO availabilities (date_from, date_to, space_id) VALUES ('2024-01-01', '2024-01-14', 1);
INSERT INTO availabilities (date_from, date_to, space_id) VALUES ('2024-02-01', '2024-02-14', 1);
INSERT INTO availabilities (date_from, date_to, space_id) VALUES ('2024-03-01', '2024-03-14', 1);