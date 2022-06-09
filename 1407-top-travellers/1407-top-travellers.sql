SELECT name, IFNULL(SUM(distance),0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = user_id
GROUP BY user_id
ORDER BY travelled_distance DESC, name
