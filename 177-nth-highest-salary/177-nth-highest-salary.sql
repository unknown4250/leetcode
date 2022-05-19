CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      /*  LIMIT is used for how many rows u want in the output, and OFFSET is used for like how many rows you wanna skip to get the desired row... */
      SELECT DISTINCT(salary) FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET N
  );
END