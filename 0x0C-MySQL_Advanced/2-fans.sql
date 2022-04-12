-- tasks mysql advanced
-- third task
select DISTINCT  origin, SUM(fans) nb_fans from metal_bands GROUP BY origin ORDER BY nb_fans DESC;
