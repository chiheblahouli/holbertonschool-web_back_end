const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    let f = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${f}`);
    return f
}
module.exports = sendPaymentRequestToApi;