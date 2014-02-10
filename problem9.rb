class Problem9Solution
  def find
    squared = 1.upto(1000).map { |x| x * x }
    squared.each_with_index do |x, i|
      j = 0
      k = i - 1
      while j < i or k > 0
        if squared[j] + squared[k] < x
          j += 1
        elsif squared[j] + squared[k] > x
          k -= 1
        elsif squared[j] + squared[k] == x
          if (j + 1) + (k + 1) + (i + 1) == 1000
            return j + 1, k + 1, i + 1
          end
          j += 1
          k -= 1
        end
      end
    end
  end
end
