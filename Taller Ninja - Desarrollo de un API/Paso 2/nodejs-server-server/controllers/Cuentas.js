'use strict';

var utils = require('../utils/writer.js');
var Cuentas = require('../service/CuentasService');

module.exports.crearCuenta = function crearCuenta (req, res, next) {
  var body = req.swagger.params['body'].value;
  Cuentas.crearCuenta(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.eliminarCuenta = function eliminarCuenta (req, res, next) {
  var cuentaId = req.swagger.params['cuentaId'].value;
  var api_key = req.swagger.params['api_key'].value;
  Cuentas.eliminarCuenta(cuentaId,api_key)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.infoCuenta = function infoCuenta (req, res, next) {
  var cuentaId = req.swagger.params['cuentaId'].value;
  Cuentas.infoCuenta(cuentaId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.modificaCuenta = function modificaCuenta (req, res, next) {
  var body = req.swagger.params['body'].value;
  Cuentas.modificaCuenta(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
