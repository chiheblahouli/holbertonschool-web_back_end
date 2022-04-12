const calculateNumber = require('./2-calcul_chai.js');
const chai = require('chai');

describe('mytest', () => {
    it('SUBTRACT', function() {
        chai.expect(calculateNumber('SUBTRACT', 0.4, 4.2)).to.equal(-4);
        chai.expect(calculateNumber('SUBTRACT', 2, 1.2)).to.equal(1);
        chai.expect(calculateNumber('SUBTRACT', 7.3, 5)).to.equal(2);
    });
    it('SUM', function() {
        chai.expect(calculateNumber('SUM', 4.3, 4.5)).to.equal(9);
        chai.expect(calculateNumber('SUM', 2, 5.1)).to.equal(7);
    });
    it('DIVIDE', function() {
        chai.expect(calculateNumber('DIVIDE', 3.4, 0)).to.equal('Error');
        chai.expect(calculateNumber('DIVIDE', 2.5, 1.1)).to.equal(3);;
        chai.expect(calculateNumber('DIVIDE', -9, 2)).to.equal(-4.5);
    });
});