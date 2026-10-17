require "active_support/all"

module Jekyll
  # Formats a number with thousands separators, e.g. {{ 8679 | number_with_delimiter }} -> "8,679".
  module NumberDelimiterFilter
    def number_with_delimiter(input)
      ActiveSupport::NumberHelper.number_to_delimited(input)
    end
  end
end

Liquid::Template.register_filter(Jekyll::NumberDelimiterFilter)
