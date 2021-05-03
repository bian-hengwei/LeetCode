# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
From Person LEFT OUTER JOIN Address ON Person.PersonId = Address.PersonId