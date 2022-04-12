const sendPaymentRequestToApi = require('./3-payment.js');
const Util = require('./utils');
const assert = require('assert');
const sinon = require('sinon');

describe('test with spy', function() {
    it('check0', function() {
        const a = sinon.spy(Util, 'calculateNumber');
        Util.calculateNumber('SUM', 2, 9);
        const callb = Util.calculateNumber.getCall(0);
        assert.equal(callb.returnValue, sendPaymentRequestToApi(2, 9));
        a.restore();
    });
});