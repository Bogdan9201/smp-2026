# Результат роботи 8

## 1. Вивід perevir.py

```

== 1. Треки гурту Queen: трек, альбом
     Name | Title
     A Kind Of Magic | Greatest Hits II
     Under Pressure | Greatest Hits II
     Radio GA GA | Greatest Hits II
     … ще 42
  ✅ правильно (рядків: 45)

== 2. Треків у кожному жанрі: жанр, кількість; від найбільшого
     Name | kilkist
     Rock | 1297
     Latin | 579
     Metal | 374
     … ще 22
  ✅ правильно (рядків: 25)

== 3. Топ-10 клієнтів за сумою покупок: імʼя, прізвище, сума; від найбільшої
     FirstName | LastName | suma
     Helena | Holý | 49.62
     Richard | Cunningham | 47.62
     Luis | Rojas | 46.62
     … ще 7
  ✅ правильно (рядків: 10)

== 4. Виконавці з більш ніж 5 альбомами: виконавець, альбомів; від найбільшого
     Name | albomiv
     Iron Maiden | 21
     Led Zeppelin | 14
     Deep Purple | 11
     … ще 3
  ✅ правильно (рядків: 6)

== 5. Виконавці без жодного альбому
     Name
     Milton Nascimento & Bebeto
     Azymuth
     João Gilberto
     … ще 68
  ✅ правильно (рядків: 71)

== 6. Середня тривалість треку по жанрах, хв з одним знаком; від найдовшої
     Name | khvylyn
     Sci Fi & Fantasy | 48.5
     Science Fiction | 43.8
     Drama | 42.9
     … ще 22
  ✅ правильно (рядків: 25)

== 7. Виторг за країнами (за рахунками): країна, сума; від найбільшого
     BillingCountry | suma
     USA | 523.06
     Canada | 303.96
     France | 195.1
     … ще 21
  ✅ правильно (рядків: 24)

== 8. Співробітники підтримки й кількість їхніх клієнтів; від найбільшого
     FirstName | LastName | klientiv
     Jane | Peacock | 21
     Margaret | Park | 20
     Steve | Johnson | 18
  ✅ правильно (рядків: 3)

Разом: 8 з 8 пунктів ✅   (мінімум для зарахування — пункти 1–5)
```

## 2. Моє питання

Які п'ять виконавців принесли магазину найбільше грошей?

## 3. Запит

```sql
SELECT ar.Name, ROUND(SUM(il.UnitPrice * il.Quantity), 2) AS vytorh
FROM InvoiceLine il
JOIN Track t   ON il.TrackId = t.TrackId
JOIN Album al  ON t.AlbumId = al.AlbumId
JOIN Artist ar ON al.ArtistId = ar.ArtistId
GROUP BY ar.ArtistId
ORDER BY vytorh DESC
LIMIT 5;
```

| Name | vytorh |
|---|---|
| Iron Maiden | 138.6 |
| U2 | 105.93 |
| Metallica | 90.09 |
| Led Zeppelin | 86.13 |
| Lost | 81.59 |

## 4. Відповідь

Найбільше грошей принесли Iron Maiden (138,60), далі U2 і Metallica, тож рок і метал варто тримати в асортименті першими.

## 5. Порядок виконання мого запиту

`FROM` + `JOIN` (з'єднуємо чотири таблиці: рядок продажу → трек → альбом → виконавець) → `GROUP BY` (по одній групі на виконавця) → `SELECT` (рахуємо суму `UnitPrice * Quantity` у групі) → `ORDER BY` (від найбільшої суми) → `LIMIT 5`. `WHERE` і `HAVING` тут не потрібні.
