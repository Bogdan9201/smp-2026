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

---

# Додаткові завдання

## ⭐1. Хіти продажів: 5 жанрів за кількістю проданих штук

```sql
SELECT g.Name, SUM(il.Quantity) AS prodano
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
JOIN Genre g ON t.GenreId = g.GenreId
GROUP BY g.GenreId
ORDER BY prodano DESC
LIMIT 5;
```

| Name | prodano |
|---|---:|
| Rock | 835 |
| Latin | 386 |
| Metal | 264 |
| Alternative & Punk | 244 |
| Jazz | 80 |

## ⭐2. Мертвий каталог

```sql
SELECT COUNT(*) AS ne_kupleno,
       (SELECT COUNT(*) FROM Track) AS usogo,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM Track), 1) AS vidsotok
FROM Track t
LEFT JOIN InvoiceLine il ON il.TrackId = t.TrackId
WHERE il.InvoiceLineId IS NULL;
```

Результат: **1519** треків із **3503** жодного разу не купили, це **43,4%** каталогу.

Висновок для магазину: майже половина каталогу не продається, тож варто перевірити, чи її взагалі видно покупцям (пошук, добірки, рекомендації), і не купувати нові ліцензії на схожий матеріал, доки не зрозуміло чому.

## ⭐3. Звіт із Python

Файли `zvit.py` (виконує запит із пункту 7 через `sqlite3`) і `zvit.md` (таблиця «країна · виторг», від найбільшого) лежать поруч.

## ⭐4. Дерево підпорядкування

```sql
WITH RECURSIVE tree(id, name, lvl, path) AS (
  SELECT EmployeeId, FirstName || ' ' || LastName, 0, FirstName || ' ' || LastName
  FROM Employee
  WHERE ReportsTo IS NULL
  UNION ALL
  SELECT e.EmployeeId, e.FirstName || ' ' || e.LastName, tree.lvl + 1,
         tree.path || ' → ' || e.FirstName || ' ' || e.LastName
  FROM Employee e
  JOIN tree ON e.ReportsTo = tree.id
)
SELECT lvl, name, path FROM tree ORDER BY path;
```

| lvl | name | path |
|---:|---|---|
| 0 | Andrew Adams | Andrew Adams |
| 1 | Michael Mitchell | Andrew Adams → Michael Mitchell |
| 2 | Laura Callahan | Andrew Adams → Michael Mitchell → Laura Callahan |
| 2 | Robert King | Andrew Adams → Michael Mitchell → Robert King |
| 1 | Nancy Edwards | Andrew Adams → Nancy Edwards |
| 2 | Jane Peacock | Andrew Adams → Nancy Edwards → Jane Peacock |
| 2 | Margaret Park | Andrew Adams → Nancy Edwards → Margaret Park |
| 2 | Steve Johnson | Andrew Adams → Nancy Edwards → Steve Johnson |

Чому звичайним `JOIN` це не розв'язати: кожен `JOIN` піднімає ланцюжок рівно на один щабель (співробітник → начальник → начальник начальника). Щоб охопити три рівні, треба написати три `JOIN` самої таблиці, для чотирьох — чотири, і так далі, а кількість рівнів потрібно знати наперед. Якщо в компанії з'явиться ще один рівень, запит доведеться переписувати. `WITH RECURSIVE` розв'язує це: спочатку береться корінь (директор, у якого `ReportsTo IS NULL`), а потім крок «додай підлеглих тих, кого вже знайшли» повторюється, доки є нові рядки, тож глибина може бути довільною. У полі `path` на кожному кроці дописується ім'я підлеглого до ланцюжка начальника, звідси «Директор → Менеджер → Агент».
