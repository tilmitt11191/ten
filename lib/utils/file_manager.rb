#ruby
STDOUT.sync = true

class File_manager

	def self.renew_file filename, array
		file = File.open(filename, "a+", encoding: "Shift_JIS")
		line_count = 0
		while file.gets
			line_count +=1
		end
		puts "line_count[#{line_count}], array.size[#{array.size}]"
		if line_count < array.size then
			puts "renew"
			for i in line_count..array.size-1
				file.puts array[i]
			end
		end
		
		file.close
	end

end