DROP TABLE IF EXISTS sched;
DROP TABLE IF EXISTS port;
DROP TABLE IF EXISTS controller;
DROP TABLE IF EXISTS day;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE day(
    day_id INTEGER NOT NULL PRIMARY KEY,
    day_name VARCHAR(15) NOT NULL
);

CREATE INDEX ix_day_001 ON day(day_name);

CREATE TABLE controller (
    controller_id INTEGER PRIMARY KEY AUTOINCREMENT,
    controller_name VARCHAR(256) NOT NULL,
    enabled INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX ix_controller_001 ON controller(controller_name);

CREATE TABLE port(
    port_id INTEGER PRIMARY KEY AUTOINCREMENT,
    controller_id INTEGER NOT NULL,
    port_number INTEGER NOT NULL DEFAULT 0,
    port_name VARCHAR(256) NOT NULL,
    enabled INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(controller_id) REFERENCES controller(controller_id)
);

CREATE INDEX ix_port_001 ON port(port_name);
CREATE INDEX ix_port_002 ON port(controller_id, port_number);

CREATE TABLE sched(
    sched_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    day INTEGER NOT NULL,
    hour INTEGER NOT NULL,
    minute INTEGER NOT NULL,
    controller_id INTEGER NOT NULL,
    port_id INTEGER NOT NULL,
    enabled INTEGER NOT NULL,
    state INTEGER NOT NULL,
    FOREIGN KEY (day) REFERENCES day(day_id),
    FOREIGN KEY (controller_id) REFERENCES controller(controller_id),
    FOREIGN KEY (port_id) REFERENCES port(port_id)
);