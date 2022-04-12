-- tasks mysql advanced
-- ComputeAverageScoreForUser Proc
DROP PROCEDURE IF EXISTS `ComputeAverageScoreForUser`;
DELIMITER !F>
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections as COr WHERE COr.user_id=user_id) WHERE id = user_id;
END !F>
DELIMITER ;
