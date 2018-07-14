
class BeforeAll():
  def __init__(self, get_response=None):
    self.get_response = get_response

  def process_request(self, request):
    None

  def process_response(self, request, response):
    response['Server'] = 'Ubuntu; Python; '
    return response
