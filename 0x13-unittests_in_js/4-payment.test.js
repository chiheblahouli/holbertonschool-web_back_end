const sendPaymentRequestToApi = require('./3-payment');
const Util = require('./utils');
const assert = require('assert');
const sinon = require('sinon');

describe('test with spy', function() {
    it('check0', function() {
        const c = sinon.stub(console, 'log');
        const a = sinon.stub(Util, 'calculateNumber').returns(10);
        sendPaymentRequestToApi(100, 20);
        assert.ok(a.calledWithExactly('SUM', 100, 20), true);
        assert.ok(c.calledWithExactly("The total is: 10"), true);
        a.restore();
        c.restore();
    });
});