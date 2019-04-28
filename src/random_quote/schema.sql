CREATE TABLE IF NOT EXISTS quotes (
	quote TEXT NOT NULL,
	created TEXT DEFAULT (datetime('now'))
);