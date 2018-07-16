require 'httparty'
require 'json'

Given("Generar petición HTTP {string} con headers") do |url|
  @url = CONSTANTS[:servicios][:ubicaciones][:url] + url
  @headers = {
    CONSTANTS[:servicios][:ubicaciones][:csrf_key] => CONSTANTS[:servicios][:ubicaciones][:csrf_value],
    'Content-Type' => 'application/x-www-form-urlencoded',
    'charset' => 'utf-8'
  }
  @query = {}
end

Given("Generar petición HTTP {string} sin headers") do |url|
  @url = CONSTANTS[:servicios][:ubicaciones][:url] + url
  @headers = {}
  @query = {}
end

When("Ejecutar petición HTTP") do
  @response = HTTParty.get(@url, headers: @headers, query: @query)
end

Then("Se debe obtener un status code success {int}") do |status_code|
  expect(@response.code).to be == status_code
end

Then("Se debe obtener un status code error {int}") do |status_code|
  expect(@response.code).to be == status_code
end

Then("Se debe obtener los departamentos mayor o igual a {int}") do |cantidad_minima|
  departamentos = JSON.parse(@response.body)
  expect(departamentos.length).to be >= cantidad_minima
end

Then("Se debe obtener mensaje de error CSRF token") do
  expect(@response.body).to include('error')
  expect(@response.body).to include('CSRF Token')
end
