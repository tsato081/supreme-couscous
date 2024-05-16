#Exercise 0
def github() -> str:
    """
    takes no arguments and returns a link to my solutions on GitHub.
    """
    
    return "https://github.com/tsato081/supreme-couscous/blob/main/Problem_Set_6.py"

#Exercise 1
def std() -> str:
    """
    Takes no arguments and returns a string containing a SQL query 
    that can be run against the auctions.db database.
    """

    print(' """ '
"SELECT \n" +
" itemid\n" +
" , bidamount\n" +
" , SQRT(SUM((bidamount - avg_bid) * (bidamount - avg_bid)) / (n_bids - 1)) AS std\n" +
" FROM (\n" +
"     SELECT \n" +
"          itemid\n" +
"        , bidamount\n" +
"        , AVG(bidamount) OVER (PARTITION BY itemid) as avg_bid\n" +
"        , COUNT(*) OVER (PARTITION BY itemid) as n_bids\n" +
"    FROM bids\n" +
" ) SUB\n" +
" GROUP BY itemid\n" +
" HAVING COUNT(*) > 1\n" +
' """ '
)
    return None

#Exercise 2
def bidder_spend_frac() -> str:
    """
    takes no arguments and returns a string containing a SQL query that can be run against the auctions.db
    database that outputs a table that has four columns:
    
    bidderName: the name of the bidder
    total_spend: the amount the bidder spent (that is, the sum of their winning bids)
    total_bids: the amount the bidder bid, regardless of the outcome. NB: bidders may submit multiple bids for an item
    spend_frac: total_spend/total_bids
    """
    print(' """ '
        "SELECT\n" +
        "  bidderName\n" +
        " ,total_spend\n" +
        " ,total_bids\n" +
        " ,(total_spend / total_bids) AS spend_frac\n" +
        " FROM (\n" +
        "   SELECT\n" +
        "     bidderName\n" +
        "    ,SUM(CASE WHEN bidderName = highBidderName THEN bidAmount ELSE 0 END) AS total_spend\n" +
        "    ,MAX(bidamount) AS total_bids\n" +
        "    FROM bids\n" +
        "    GROUP BY bidderName\n" +
        " )\n" +
        ' """ ') 

    return None

#Exercise 3
def min_increment_freq() -> str:
    """
    takes no arguments and returns a string containing 
    a SQL query that can be run against the auctions.db database that 
    outputs a table that has one column (freq) 
    which represents the fraction of bids in the database 
    that are exactly the minimum bid increment above the previous high bid.
    """

    return """
SELECT 
    COUNT (*) * 1.0 /(SELECT COUNT(*) FROM bids JOIN items ON bids.itemId = items.itemId WHERE items.isBuyNowUsed = 0) AS freq
    FROM(
      SELECT
         bids.itemId
        ,bidAmount
        ,LAG(bidAmount) OVER (PARTITION BY bids.itemId ORDER BY bidTime) as prevBidAmount
        ,items.bidIncrement
      FROM bids
      JOIN items ON bids.itemId = items.itemId
      WHERE items.isBuyNowUsed = 0
      ) AS subquery
WHERE (bidAmount - prevBidAmount) = bidIncrement;
"""


#Exercise 4
def win_perc_by_timestamp() -> str:
    """
    that takes no arguments and returns a string containing a SQL query that
    outputs a table that has two columns:
        timestamp_bin: normalize the bid timestamp and classify it as one of ten bins: 
            1 corresponds to 0-.1, 2 corresponds to .1-.2, etc.
        win_perc: the frequency with which a bid placed with this timestamp bin won the auction.
    """

    return """
WITH TimeNorm AS (
    SELECT
        b.itemid
       ,b.bidamount
       ,(JULIANDAY(endtime) - JULIANDAY(b.bidtime)) / (JULIANDAY(i.endtime) - JULIANDAY(i.starttime)) AS time_norm
       ,b.bidAmount = MAX(b.bidAmount) OVER (PARTITION BY b.itemid) AS isWinning
    FROM
        bids AS b
    JOIN 
        items AS i ON b.itemid = i.itemid
),
Bins AS (
    SELECT
         itemid
        ,CASE
            WHEN time_norm <= 0.1 THEN 1
            WHEN time_norm <= 0.2 THEN 2
            WHEN time_norm <= 0.3 THEN 3
            WHEN time_norm <= 0.4 THEN 4
            WHEN time_norm <= 0.5 THEN 5
            WHEN time_norm <= 0.6 THEN 6
            WHEN time_norm <= 0.7 THEN 7
            WHEN time_norm <= 0.8 THEN 8
            WHEN time_norm <= 0.9 THEN 9
            ELSE 10
        END AS timestamp_bin,
        isWinning
    FROM TimeNorm
)

SELECT
     timestamp_bin
    ,(SUM(isWinning) * 100.0 / COUNT(*)) AS win_perc
FROM Bins
GROUP BY timestamp_bin;
"""