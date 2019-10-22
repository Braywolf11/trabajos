var http = require('http');
var dt = require('./Modules/dateTime');

http.createServer(function(req, res){
    res.writeHead(200,{'Content-Type': 'text/html'});
    res.write('The current Date Time is : <br>'+ dt.currentDateTime());
    res.end('<center><h5>Hello World! Node.js Example<h5></center>');
    

}).listen(8080);
