-- Command to prints the following description of the table
-- first_table from the database hbtn_0c_0 in MySQL server.

SELECT
    CONCAT(
        TABLE_NAME, 
        '     CREATE TABLE `', 
        TABLE_NAME, 
        '` (\n  ', 
        GROUP_CONCAT(
            CONCAT(
                '`', COLUMN_NAME, '` ', 
                COLUMN_TYPE, 
                IF(IS_NULLABLE = 'NO', ' NOT NULL', ''), 
                IFNULL(CONCAT(' DEFAULT ', IF(COLUMN_DEFAULT IS NULL, 'NULL', QUOTE(COLUMN_DEFAULT))), ''),
                '\n'
            )
            SEPARATOR ''
        ),
        ') ENGINE=', ENGINE, ' DEFAULT CHARSET=', CHARACTER_SET_NAME, ' COLLATE=', COLLATION_NAME
    ) AS table_description
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table'
GROUP BY
    TABLE_NAME;
