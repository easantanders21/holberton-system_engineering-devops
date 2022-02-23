#!/usr/bin/env ruby
str = ARGV[0]
puts str.scan(/hbt{2,5}n/).join
