SELECT employee_id, IF (name LIKE 'M%' OR MOD(employee_id,2) = 0, 0, salary) AS bonus
FROM Employees
ORDER BY employee_id
