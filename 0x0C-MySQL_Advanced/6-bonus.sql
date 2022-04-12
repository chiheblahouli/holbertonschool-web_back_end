-- tasks mysql advanced
-- AddBonus Functuion

DROP PROCEDURE IF EXISTS `AddBonus` ;  
DELIMITER !F>
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
    THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SET @projid = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, @projid, score);
END !F>
DELIMITER ;
