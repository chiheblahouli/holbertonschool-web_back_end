const calculateNumber = require('./1-calcul.js');
const assert = require('assert');

describe('mytest', () => {
    it('SUBTRACT', function() {
        assert.strictEqual(calculateNumber('SUBTRACT', 0.4, 4.2), -4);
        assert.strictEqual(calculateNumber('SUBTRACT', 2, 1.2), 1);
        assert.strictEqual(calculateNumber('SUBTRACT', 7.3, 5), 2);
    });
    it('SUM', function() {
        assert.strictEqual(calculateNumber('SUM', 4.3, 4.5), 9);
        assert.strictEqual(calculateNumber('SUM', 2, 5.1), 7);
    });
    it('DIVIDE', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 3.4, 0), 'Error');
        assert.strictEqual(calculateNumber('DIVIDE', 2.5, 1.1), 3);
        assert.strictEqual(calculateNumber('DIVIDE', -9, 2), -4.5);
    });
});