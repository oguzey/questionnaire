BEGIN;
CREATE TABLE "user_data" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
);

COMMIT;
