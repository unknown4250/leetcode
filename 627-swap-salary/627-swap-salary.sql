# Write your MySQL query statement below
# UPDATE Salary SET sex = IF(sex='m','f','m')
UPDATE Salary
SET sex = case WHEN sex='f' THEN 'm' ELSE 'f' END