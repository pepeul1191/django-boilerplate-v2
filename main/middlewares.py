class BeforeAll():
  def __init__(self, get_response=None):
    self.get_response = get_response

  def process_request(self, request):
    None

  def process_response(self, request, response):
    response['x-powered-by'] = 'Ubuntu; Python; gunicorn/19.9.0;'
    return response
