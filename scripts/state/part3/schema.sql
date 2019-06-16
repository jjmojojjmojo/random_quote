CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY, 
	quote TEXT NOT NULL,
	author TEXT NOT NULL,
	created TEXT DEFAULT (datetime('now')),
	rand INTEGER DEFAULT (random())
);

CREATE INDEX IF NOT EXISTS quotes_rand ON quotes (rand);

CREATE TABLE IF NOT EXISTS quote_of_the_day (
    quote_id INTEGER NOT NULL,
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    FOREIGN KEY(quote_id) REFERENCES quotes(id)
    UNIQUE(day, month, year)
);