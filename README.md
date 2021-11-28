# ThinkOrSwim (TOS) Trading Log
 A Flask-based tool to load TOS TRD records into a SQLIte db as a trading log
  - yadda yadda

## Process
  - Regular download  (probably weekly) of TOS TRD records - TOS_TRDs.csv
  - Regular download of trading recommendations
      -  MoneyMap.csv
      -  ProfitsRun.csv
  - Load TRD recs into SQLite DB - Trades.db
    - Regularize the Description field into proper fields
      - Date
      - Time
      - BOT / SOLD
      - VERTICAL /  SINGLE
      - Symbol
      - CALL / PUT
      - Strike
      - Cost
  - Load recommendations recs into TrRecs.db
    - Regularize records from two (or more) sources
      - Date
      - Symbol
      - VERTICAL / SINGLE
      - Strike(s)
      - Limit
      - Expiration data
      - BUY / SELL
      -
## Flask app
The Flask app provides an interface to
  - run the processing steps
  - Display the results

## Modules
  - loadTOS
    - TRD.db
      - Return connection, create if doesn't exist, throw FileNotFound,
      - User specifies database file path in config.py at installation in DATABASE_FILE_PATH_
    - TrRec.db - likewise
    - Create db from schema or code?
    - Read uploaded .csv w/DictReader
    - Write with execute (not using linux csv to create since .csv struct is wrong)
