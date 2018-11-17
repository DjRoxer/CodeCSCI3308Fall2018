
CREATE TABLE drinks (
    did SERIAL PRIMARY KEY,
    name varchar(40),
    ingredients text[][],
    instructions text[],
    link text[]
);

CREATE TABLE users (
    uid SERIAL PRIMARY KEY,
    name varchar(40),
    password varchar(40),
    favorites INTEGER[]
);
