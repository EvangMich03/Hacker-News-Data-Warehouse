# Hacker News Data Warehouse

A Python-based ETL pipeline that fetches top stories from the [Hacker News API](https://github.com/HackerForge/HackerNewsAPI) and loads them into a PostgreSQL database.

## Features
- Fetches the top 100 stories from the Hacker News Firebase API.
- Stores core story metadata (ID, title, author, score, creation time, URL) in a `stories` table.
- Archives the full JSON response for each item in a `raw_times` table.
- Uses `psycopg2` for efficient database interactions.
- Handles conflicts via `ON CONFLICT` clauses to support idempotent updates.

## Prerequisites
- Python 3.12+
- A running PostgreSQL instance
- `.env` file containing the database password:
  ```env
  dbpassword=your_secure_password
  ```

## Setup
1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup
To initialize the database, execute the `schema.sql` file in your PostgreSQL instance:

```bash
psql -d <your_db_name> -f schema.sql
```

## Usage
Run the script to fetch and store the latest data:
```bash
python fetch.py
```

## Database Schema
The database requires the following tables, defined in `schema.sql`:

### `stories`
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | BIGINT | Primary key (HN ID) |
| `title` | VARCHAR(100) | Story title |
| `author` | VARCHAR(50) | Author username |
| `score` | INT | Current score |
| `created_at` | TIMESTAMP | Creation time |
| `url` | TEXT | Story URL |

### `raw_times`
| Column | Type | Description |
| :--- | :--- | :--- |
| `item_id` | BIGINT | Primary key (HN ID) |
| `fetched_at` | TIMESTAMP | Timestamp of fetch |
| `payload` | JSON | Full JSON payload |
