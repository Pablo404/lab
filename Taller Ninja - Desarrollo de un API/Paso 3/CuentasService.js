'use strict';

// La variable examples simula la BD
var  examples = [ {
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
}, {
  "cliente" : 6,
  "cuentaId" : 1,
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
} ];

/**
 * Crear una cuenta nueva
 * 
 *
 * body Cuenta Objeto con toda la información necesaria para la creación de una cuenta.
 * no response value expected for this operation
 **/
exports.crearCuenta = function(body) {
  return new Promise(function(resolve, reject) {
    //Se añade la cuenta a la colección
    examples.push(body);
    resolve("OK");
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
    console.log("cuentas antes de eliminar:" + examples);
    // Buscamos la cuenta con el "cuentaId" pasado como parámetro
    var cuenta = examples.find(function(elemento){
      return elemento.cuentaId == cuentaId;
    });
    console.log("cuenta obtenida: " + cuenta);
    // Una vez encontrada la cuenta, se elimina del array
    var index = examples.indexOf(cuenta);
    console.log("índice de la cuenta:" + index);
    examples.splice(index,1);
    console.log("cuentas después de eliminar: " + examples);
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

    if (Object.keys(examples).length > 0) {
      var cuenta = examples.find(function(elemento){
        return elemento.cuentaId == cuentaId;
      });
      resolve(cuenta);
    } else {
      resolve();
    }
  });
}


/**
 * Devolver las cuentas de un cliente
 * Dado el identificador de un cliente, devuelve todas sus cuentas.
 *
 * clienteId Long Id del cliente de la cuenta a consultar
 * returns List
 **/
exports.listaCuentas = function(clienteId) {
  return new Promise(function(resolve, reject) {
    console.log("devolviendo lista de cuentas")
    if (Object.keys(examples).length > 0) {
      resolve(examples);
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

