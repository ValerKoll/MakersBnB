DROP TABLE IF EXISTS "public"."spaces";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;

-- Table Definition
CREATE TABLE "public"."spaces" (
    "id" int4 NOT NULL DEFAULT nextval('spaces_id_seq'::regclass),
    "name" varchar,
    "description" varchar,
    "price" float4
);

INSERT INTO "public"."spaces" ("id", "name", "description", "price") VALUES
(1, 'Space 1', 'urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque sodales ut etiam sit amet nisl purus in mollis nunc sed id semper', 200);
INSERT INTO "public"."spaces" ("id", "name", "description", "price") VALUES
(2, 'Space 2', 'sed arcu non odio euismod lacinia at quis risus sed vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum non consectetur a erat', 400);
INSERT INTO "public"."spaces" ("id", "name", "description", "price") VALUES
(3, 'Space 3', 'tortor condimentum lacinia quis vel eros donec ac odio tempor orci dapibus ultrices in iaculis nunc sed augue lacus viverra vitae congue eu consequat ac felis donec et odio pellentesque', 300);