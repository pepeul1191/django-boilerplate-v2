from main.constants import constants

def access_css():
  switcher = {
    'desarrollo': [
      'bower_components/bootstrap/dist/css/bootstrap.min',
      'bower_components/font-awesome/css/font-awesome.min',
      'assets/css/constants',
      'assets/css/error',
    ],
    'produccion': ['dist/error.min'],
  }
  return switcher.get(constants['ambiente_static'])

def access_js():
  switcher = {
    'desarrollo': [],
    'produccion': [],
  }
  return switcher.get(constants['ambiente_static'])
