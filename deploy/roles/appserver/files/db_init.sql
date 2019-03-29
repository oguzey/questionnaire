BEGIN;
CREATE TABLE IF NOT EXISTS "user_data" (
    "name" TEXT NOT NULL UNIQUE,
    "color" TEXT NOT NULL,
    "animals" TEXT NOT NULL
);

COMMIT;