-- script that creates the table unique_id on MySQL server
-- unique_id description:
-- id INT with the unique value 1
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
)
