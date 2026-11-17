create table raw_times (
    item_id BIGINT primary key,
    fetched_at TIMESTAMP,
    payload JSON,
    unique(item_id)
);

create table stories (
    id BIGINT NOT null primary key,
    title  VARCHAR(100) NOT NULL,
    author  VARCHAR(50),
    score INT not NULL,
    created_at TIMESTAMP,
    url TEXT,
    unique(id)
);
