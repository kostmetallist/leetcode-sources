SELECT IFNULL(
    (
        SELECT DISTINCT Salary
        FROM `Employee`
        ORDER BY Salary DESC LIMIT 1, 1
    )
    , null
) as `SecondHighestSalary`
