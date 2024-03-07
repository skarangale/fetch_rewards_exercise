CREATE TABLE IF NOT EXISTS brand (
    id VARCHAR(24) PRIMARY KEY,
    barcode VARCHAR(12) UNIQUE NOT NULL,
    brand_code VARCHAR,
    category VARCHAR,
    category_code VARCHAR,
    cogs_id VARCHAR(24) FOREIGN KEY REFERENCES cogs(id),
    cpgs_id VARCHAR(24) FOREIGN KEY REFERENCES cpgs(id),
    name VARCHAR NOT NULL,
    top_brand BOOLEAN
);