SELECT 
    dep.name AS Department,
    emp.name AS Employee,
    emp.salary AS Salary
FROM Department dep, Employee emp 
where 
    emp.DepartmentId = dep.Id 
AND 
    emp.salary=
        (SELECT 
            MAX(Salary) 
         FROM
            Employee emp2 
         WHERE 
            emp2.DepartmentId=dep.Id)