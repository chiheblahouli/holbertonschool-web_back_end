
-- tasks mysql advanced
-- ComputeAverageWeightedScoreForUser adv
DELIMITER !F>
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser ;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        FROM corrections
        INNER JOIN projects
        ON corrections.project_id = projects.id and corrections.user_id = user_id)
    WHERE id = user_id;
END !F>
DELIMITER ;
