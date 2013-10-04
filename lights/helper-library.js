var http = require('http');

lr_host = 'lightroom.vhata.net';

var lr_get = function(x, y, cb) {
    request = http.get({
        host: lr_host,
        path: '/get/'+x+'/'+y+'/'
    })
    .on('response', function(response) {
        response.on('data', cb);
    })
};

var lr_set = function(x, y, intensity) {
    request = http.get({
        host: lr_host,
        path: '/set/'+x+'/'+y+'/'+intensity+'/'
    });
};

var lr_toggle = function(x, y) {
    request = http.get({
        host: lr_host,
        path: '/toggle/'+x+'/'+y+'/'+intensity+'/'
    });
};

var lr_set_multi = function(data) {
    request = http.request({
        host: lr_host,
        path: '/set_multi/',
        method: 'POST'
    }).write(data).end();
};

