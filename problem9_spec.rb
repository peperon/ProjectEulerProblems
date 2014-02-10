require './problem9'

describe Problem9Solution do
  it "Finds the special pythagorean triplet" do
    solution = Problem9Solution.new
    a, b, c = solution.find
    expect(a * a + b * b).to eq(c * c)
    expect(a + b + c).to eq(1000)
  end
end
