'use strict';


/**
 * Crear una cuenta nueva
 * 
 *
 * body Cuenta Objeto con toda la información necesaria para la creación de una cuenta.
 * no response value expected for this operation
 **/
exports.crearCuenta = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Eliminar una cuenta
 * 
 *
 * cuentaId Long Id de la cuenta a eliminar
 * api_key String  (optional)
 * no response value expected for this operation
 **/
exports.eliminarCuenta = function(cuentaId,api_key) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Devolver los datos de una cuenta
 * Dado el identificador de una cuenta de vuelve todos sus datos.
 *
 * cuentaId Long Id de la cuenta a consultar
 * returns Cuenta
 **/
exports.infoCuenta = function(cuentaId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "cliente" : 6,
  "cuentaId" : 0,
  "saldo" : "saldo",
  "movimientos" : [ {
    "fecha" : "2000-01-23",
    "id" : 1,
    "saldo" : 5.962133916683182
  }, {
    "fecha" : "2000-01-23",
    "id" : 1,
    "saldo" : 5.962133916683182
  } ]
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Modificar una cuenta existente.
 * 
 *
 * body Cuenta Objeto con los datos de la cuenta a modificar.
 * no response value expected for this operation
 **/
exports.modificaCuenta = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

