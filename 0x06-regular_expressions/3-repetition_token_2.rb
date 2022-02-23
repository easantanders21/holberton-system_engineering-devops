#!/usr/bin/env ruby
str = ARGV[0]
puts str.scan(/hbt{1,}n/).join
