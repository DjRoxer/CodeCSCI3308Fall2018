
CREATE TABLE drinks (
    did SERIAL PRIMARY KEY,
    name varchar(40),
    ingredients text[][],
    instructions text[],
    link text[]
);
