
const coap  = require('coap') // or coap
, req   = coap.request('coap://localhost/Matteo')

req.on('response', function(res) {
    res.pipe(process.stdout)
})

req.end()