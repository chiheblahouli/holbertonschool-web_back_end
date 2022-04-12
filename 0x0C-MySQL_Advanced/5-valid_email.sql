-- tasks mysql advanced
-- email validation
DELIMITER !F>

DROP TRIGGER IF EXISTS `validationemail` ;  
CREATE TRIGGER  `validationemail`
BEFORE UPDATE ON `users`

FOR EACH ROW
    BEGIN
        IF OLD.email != NEW.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END; !F>

DELIMITER ;
