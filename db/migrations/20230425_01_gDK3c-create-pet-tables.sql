-- Create tables for pet data
-- depends: 
CREATE TABLE IF NOT EXISTS pet_skills(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL,
    range REAL,
    time REAL,
    cooldown REAL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pets(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL,
    skill1 INTEGER NOT NULL REFERENCES pet_skills(id),
    skill2 INTEGER NOT NULL REFERENCES pet_skills(id),
    skill3 INTEGER NOT NULL REFERENCES pet_skills(id),
    skill4 INTEGER NOT NULL REFERENCES pet_skills(id),
    skill5 INTEGER NOT NULL REFERENCES pet_skills(id),
    hatch_exp INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS pet_catch_items(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    pet_id INTEGER UNIQUE NOT NULL REFERENCES pets(id),
    item_name TEXT NOT NULL,
    unit_price_shells INTEGER,
    quantity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS pet_hatch_stats(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    pet_id INTEGER NOT NULL REFERENCES pets(id),
    stat TEXT NOT NULL,
    amount INTEGER NOT NULL
);
