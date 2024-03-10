CREATE TABLE IF NOT EXISTS brand (
    id VARCHAR(24) PRIMARY KEY,
    barcode VARCHAR(12) NOT NULL,
    brand_code VARCHAR,
    category VARCHAR,
    category_code VARCHAR,
    cogs_id VARCHAR(24) REFERENCES cogs(id),
    cpgs_id VARCHAR(24) REFERENCES cpgs(id),
    name VARCHAR NOT NULL,
    top_brand BOOLEAN
);