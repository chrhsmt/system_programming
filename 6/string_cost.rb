#!/usr/bin/ruby 

if (ARGV.length < 2)
  puts("usage : ruby string_cost.rb [type: plus or buffer] [count]")
  exit(1)
end

count = ARGV[1].to_i

before = Time.now
String buffer = ""
if ("plus" == ARGV[0]) 

  (0..count).each do | i |
    buffer += "abc"
  end

elsif ("buffer" == ARGV[0])

  (0..count).each do | i |
    buffer << "abc"
  end
end

puts "#{(Time.now - before) * 1000} ms"
exit(0)