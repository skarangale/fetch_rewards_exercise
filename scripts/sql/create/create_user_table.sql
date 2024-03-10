CREATE TABLE IF NOT EXISTS "user" (
    id VARCHAR(24) PRIMARY KEY,
    active BOOLEAN NOT NULL,
    created_date DATE NOT NULL,
    last_login DATE,
    role VARCHAR NOT NULL,
    sign_up_source VARCHAR,
    state VARCHAR(2)
);