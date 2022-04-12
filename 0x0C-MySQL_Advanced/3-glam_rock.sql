-- tasks mysql advanced
-- 3 Task
select band_name, (IF(split is  NULL, 2020, split) - formed) AS lifespan from metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
