SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE (NAME LIKE '%EL%' OR '%el%') and ANIMAL_TYPE = 'Dog'
ORDER BY NAME