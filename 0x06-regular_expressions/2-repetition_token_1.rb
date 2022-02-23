#!/usr/bin/env ruby
str = ARGV[0]
puts str.scan(/hb{0,1}tn/).join
