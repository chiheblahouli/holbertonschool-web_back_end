const calculateNumber = require("./0-calcul");
const assert = require('assert');

describe("calculate number testing", () => {
    it('test0', function() {
        assert.strictEqual(calculateNumber(1.9, 2.9), 5);
    });
    it('test1', function() {
        assert.strictEqual(calculateNumber(1, 2.9), 4);
    });
    it('test2', function() {
        assert.ok(!(calculateNumber(0, 0)));
    });
    it('test3', function() {
        assert.ok(!(calculateNumber("f", 1009, 2.9)));
    });
    it('test4', function() {
        assert.ok(!(calculateNumber({}, "f")));
    });
    it('tes5', function() {
        assert.strictEqual(calculateNumber(-1, 9), 8);
        assert.strictEqual(calculateNumber(-2, -1), -3);
    })
    it('tes6', function() {
        assert.strictEqual(calculateNumber(5.9, 2.1), 8);

    })
    it('check7', function() {
        assert.ok(!(calculateNumber()));
        assert.strictEqual(calculateNumber(0.2, 0.7), 1);
        assert.strictEqual(calculateNumber(1.5, 4.9), 7);
        assert.strictEqual(calculateNumber(3.6, 2), 6);
        assert.strictEqual(calculateNumber(10.9, 10.1), 21);
    });

});