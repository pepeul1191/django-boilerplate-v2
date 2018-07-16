module FridayStepHelper
  def is_it_friday(day)
    if day == 'Friday'
      'TGIF'
    else
      'Nope'
    end
  end
end
World FridayStepHelper

Given("today is Sunday") do
  @today = 'Nope'
end

When("I ask whether it's Friday yet") do
  @actual_answer = is_it_friday(@today)
end

Then("I should be told {string}") do |expected_answer|
  puts expected_answer
  puts @actual_answer
  expect(@actual_answer).to eq(expected_answer)
end

Given("today is Friday") do
  @today = 'Friday'
end
