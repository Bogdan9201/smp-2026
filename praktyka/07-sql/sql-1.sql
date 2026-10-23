-- Робота 7. SQL: вибірка. База data/chinook.db
-- Під кожним рядком «-- N.» — ОДИН запит. Рядки з «--» — коментарі, їх можна дописувати.
-- Перевірка:  python praktyka/07-sql/perevir.py

-- 1. Треки, довші за 5 хвилин: назва, тривалість у секундах; від найдовшого
SELECT Name, Milliseconds / 1000.0 AS Seconds
FROM Track
WHERE Milliseconds > 300000
ORDER BY Milliseconds DESC;

-- 2. Виконавці, чиї назви починаються на A, за абеткою
SELECT Name
FROM Artist
WHERE Name LIKE 'A%'
ORDER BY Name;

-- 3. Сім найдорожчих рахунків: номер, дата, країна, сума; від найбільшої
SELECT InvoiceId, InvoiceDate, BillingCountry, Total
FROM Invoice
ORDER BY Total DESC
LIMIT 7;

-- 4. Клієнти з Польщі або Чехії: імʼя, прізвище, країна
SELECT FirstName, LastName, Country
FROM Customer
WHERE Country IN ('Poland', 'Czech Republic');

-- 5. Приватні клієнти з Канади (поле Company порожнє): імʼя, прізвище, місто
SELECT FirstName, LastName, City
FROM Customer
WHERE Country = 'Canada' AND Company IS NULL;

-- 6. Країни, де є клієнти, — без повторів, за абеткою
SELECT DISTINCT Country
FROM Customer
ORDER BY Country;

-- 7. Альбоми, у назві яких є слово Live
SELECT Title
FROM Album
WHERE Title LIKE '%Live%';

-- 8. Рахунки за березень 2025 року: номер, дата, країна, сума; за датою
SELECT InvoiceId, InvoiceDate, BillingCountry, Total
FROM Invoice
WHERE InvoiceDate >= '2025-03-01' AND InvoiceDate < '2025-04-01'
ORDER BY InvoiceDate;
