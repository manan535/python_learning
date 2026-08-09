-- Insight: Lists customers from a selected country.

SELECT CustomerId,
       FirstName,
       LastName,
       Email,
       Country
FROM Customer
WHERE Country = 'India';
