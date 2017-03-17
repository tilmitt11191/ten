
#ruby
STDOUT.sync = true
Dir.chdir(File.dirname(File.expand_path(__FILE__))+"/../test_cases/workspace/")
require "../../lib/haihu/get_tsumo_from.rb"

#input_file = "sample.txt"
input_file = "../../etc/hounan2015/hounan2015.txt"
#output_file = "../../test_cases/workspace/output/output.txt"
output_file = "../../test_cases/workspace/output/hounan2015.csv"
File.open(output_file,'w'){|file| file = nil}

Get_tsumo_from::get_tsumo_from input_file, output_file

