// modules de express
const express = require('express');
const path = require('path');
const logger = require('morgan');
const bodyParser = require('body-parser');
const fileUpload = require('express-fileupload');
const async = require('async');
const unirest = require('unirest');
const base_url = 'http://localhost:9090/';
// servidor express
var app = express();
app.use(logger('dev'));
app.use(function (req, res, next) {
  res.set('Server', 'Ubuntu');
  res.set('Access-Control-Allow-Origin', '*');
  return next();
});
app.use(bodyParser.urlencoded({ extended: false }));
app.use(fileUpload());
app.use(express.static(path.join(__dirname, 'static')));
app.listen(9090);
console.log('Listening on port 9090');
// rutas rest
app.get('/', function (req, res) {
  var rpta = {
    'tipo_mensaje': 'error',
    'mensaje': [
      'No se puede acceder al recurso', // mensaje
    ]
  };
  res.send(JSON.stringify(rpta));
});
