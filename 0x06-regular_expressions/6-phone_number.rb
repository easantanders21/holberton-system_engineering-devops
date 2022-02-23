#!/usr/bin/env ruby
number = ARGV[0]
puts number.scan(/^\d{10,10}$/).join
