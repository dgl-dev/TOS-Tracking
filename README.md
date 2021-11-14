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
  - Load recommendations recs into Reccs.db
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
