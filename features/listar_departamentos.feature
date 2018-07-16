Feature: Listar Departamentos
  Listar los departamentos del Perú

  Scenario: Pedir lista de departamentos incluyendo headers
    Given Generar petición HTTP "ubicaciones/departamento/listar" con headers
    When Ejecutar petición HTTP
    Then Se debe obtener un status code success 200
    Then Se debe obtener los departamentos mayor o igual a 25

  Scenario: Pedir lista de departamentos per sin headers
    Given Generar petición HTTP "ubicaciones/departamento/listar" sin headers
    When Ejecutar petición HTTP
    Then Se debe obtener un status code error 500
    Then Se debe obtener mensaje de error CSRF token
