const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const assert = require('assert');

describe('my test', function() {
    let log;
    beforeEach(function() {
        log = sinon.spy(console, 'log');
    });
    afterEach(function() {
        log.restore();
    });
    it('check0', function() {
        sendPaymentRequestToApi(100, 20);
        assert.ok(log.calledOnce, true);
        assert.ok(log.calledWith('The total is: 120'), true);
    });
    it('check1', function() {
        sendPaymentRequestToApi(10, 10);
        assert.ok(log.calledOnce, true);
    });
});