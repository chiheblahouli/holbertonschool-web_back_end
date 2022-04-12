
-- tasks mysql advanced
-- ComputeAverageWeightedScoreForUser adv
DELIMITER !F>
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser ;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS fde,
        (SELECT fde.id, SUM(score * weight) / SUM(weight) AS tun
        FROM users AS fde
        JOIN corrections as coor ON fde.id=coor.user_id
        JOIN projects AS proj ON coor.project_id=proj.id
        GROUP BY fde.id)
    AS f
    SET fde.average_score = f.tun
    WHERE fde.id=f.id;
END!F>
DELIMITER ;
