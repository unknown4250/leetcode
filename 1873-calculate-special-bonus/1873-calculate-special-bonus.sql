# Write your MySQL query statement below
SELECT employee_id, IF (MOD(employee_id,2) = 0 OR name LIKE 'M%', 0, salary) AS bonus
FROM Employees
ORDER BY employee_id