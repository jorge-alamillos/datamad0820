
#CHALLENGE 1
SELECT au.au_id AS "AUTHOR ID", au.au_fname AS "FIRST NAME", au.au_lname AS "LAST NAME", t.title AS "TITLE", pu.pub_id AS "PUBLISHER"
FROM titles AS t
LEFT JOIN titleauthor AS ta ON t.title_id=ta.title_id
LEFT JOIN authors AS au ON ta.au_id=au.au_id
LEFT JOIN publishers AS pu ON t.pub_id=pu.pub_id;

#CHALLENGE 2
SELECT au.au_id AS "AUTHOR ID",au.au_lname AS "LAST NAME",au.au_fname AS "FIRST NAME", pu.pub_name AS "PUBLISHER", COUNT(t.title) AS "TITLE COUNT"
FROM titles AS t
LEFT JOIN titleauthor AS ta ON t.title_id=ta.title_id
LEFT JOIN authors AS au ON ta.au_id=au.au_id
LEFT JOIN publishers AS pu ON t.pub_id=pu.pub_id
GROUP BY au.au_id, au.au_fname, au.au_lname, pu.pub_name;


#CHALLENGE 3

SELECT au.au_id AS "AUTHOR ID",au.au_lname AS "LAST NAME",au.au_fname AS "FIRST NAME", sum(sa.qty) AS "TOTAL"
FROM authors AS au
LEFT JOIN titleauthor AS ta ON au.au_id=ta.au_id
LEFT JOIN sales AS sa ON ta.title_id=sa.title_id
group by au.au_id, au.au_lname, au.au_fname
ORDER BY TOTAL desc
LIMIT 3;

#CHALLENGE 4

SELECT au.au_id AS "AUTHOR ID",au.au_lname AS "LAST NAME",au.au_fname AS "FIRST NAME", ifnull(sum(sa.qty),0) AS "TOTAL"
FROM authors AS au
LEFT JOIN titleauthor AS ta ON au.au_id=ta.au_id
LEFT JOIN sales AS sa ON ta.title_id=sa.title_id
group by au.au_id, au.au_lname, au.au_fname
ORDER BY TOTAL desc

#BONUS
SELECT ta.title_id AS "BOOK", au.au_id AS "AUTHOR_ID",au.au_lname AS "LAST NAME",au.au_fname AS "FIRST NAME", ta.royaltyper AS "ROYATIES SPLIT", ti.price, ti.advance, ti.royalty, sum(sa.qty),(sum(sa.qty)*ti.price*(ti.royalty/100)*(ta.royaltyper/100)+ti.advance*(ta.royaltyper/100)) AS "PROFIT"
FROM authors AS au
LEFT JOIN titleauthor AS ta ON au.au_id=ta.au_id
LEFT JOIN sales AS sa ON ta.title_id=sa.title_id
LEFT JOIN titles AS ti ON ta.title_id=ti.title_id
GROUP BY ta.title_id, au.au_id, au.au_lname, au.au_fname, ta.royaltyper, ti.advance, ti.royalty
order by PROFIT desc 
LIMIT 3;
