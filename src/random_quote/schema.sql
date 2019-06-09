CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY, 
	quote TEXT NOT NULL,
	author TEXT NOT NULL,
	created TEXT DEFAULT (datetime('now')),
	rand INTEGER DEFAULT (random())
);

CREATE INDEX quotes_rand ON quotes (rand);