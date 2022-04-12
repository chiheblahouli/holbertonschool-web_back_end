-- tasks mysql advanced
-- 4 updateQntite
DROP TRIGGER IF EXISTS `updateQntite` ;  
CREATE TRIGGER  `updateQntite`
AFTER INSERT ON `orders`
FOR EACH ROW
   UPDATE items
   SET quantity = quantity - NEW.number 
   WHERE name = NEW.item_name;
