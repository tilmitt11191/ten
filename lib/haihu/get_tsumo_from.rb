
#ruby
STDOUT.sync = true
require "logger"
require "../../lib/utils/file_manager.rb"

class Get_tsumo_from

	def self.get_tsumo_from txt_file, output_file
		log = Logger.new("../../etc/log")
		log.info "Get_tsumo_from::get_tsumo_from"
		@status = ""#∈{start, drew, discarded}
		@ivent=""
		output = []
		File.open(txt_file, "r", encoding: "Shift_JIS:UTF-8").each do |line|
			line.lstrip!
			if line[0,1] == "東" || line[0,1] == "南" then
				log.debug "局の開始"
				@status = "start"
				output.push line.chomp
			elsif line.empty? then
				log.debug "局の終了"
				File_manager.renew_file output_file, output
			elsif line[0,1] == "*" then
				log.debug "牌譜の開始"
				line.gsub!("*", "")
				haihu = line.split(" ")
				haihu.each do |action|
						log.debug action
					if action.include?("G") then #"GET"
						if @status == "start" || @status == "discarded" then
							@status = "drew"
							player, tsumo = action.split("G")
							log.debug "player[#{player}], tsumo[#{tsumo}]"
							output.push("#{player},#{tsumo}")
						end
					elsif action.include?("R") then #"reach"
						log.debug "reach"
						@ivent += ",reach"
						#output[output.size-1] += ",reach"
					elsif action.include?("N") then #"naki"
						log.debug "naki"
						#@ivent += ",naki"
						#output[output.size-1] += ",naki"
					elsif action.include?("D") then #"Discard. tsumogiri"
						log.debug "tsumogiri"
						if @status == "drew" then
							@status = "discarded"
							output[output.size-1] += ",tsumogiri#{@ivent}"
							@ivent = ""
						end
					elsif action.include?("d") then #"discard. tedashi"
						log.debug "tedashi"
						if @status == "drew" then
							@status = "discarded"
							output[output.size-1] += ",tedashi#{@ivent}"
							@ivent = ""
						end
					end
				end
			end
		end
		
		return output
	end

end





