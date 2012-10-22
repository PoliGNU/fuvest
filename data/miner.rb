require 'open-uri'

anos = (1995..2012)
fases = ["inscritos","2a_fase", "1a_chamada", "ultima_chamada"]
tipos = ["regiao", "carreira", "carreira_campus"]

anos.each do |ano|
  dir_name = Dir::pwd + "/" + "#{ano}"
  Dir::mkdir dir_name if !FileTest::directory?(dir_name)
  (1..4).each do |fase|
    (1..3).each do |tipo|
      puts "Downloading qase_grupos_#{fase}_#{tipo}_#{ano}.js..."
      begin
        source = open("http://www.fuvest.br/vest#{ano}/js/qase_grupos_#{fase}_#{tipo}_#{ano}.js") { |f| f.read }
      rescue
        puts "Can't download qase_grupos_#{fase}_#{tipo}_#{ano}.js!"
        next
      end
      content = source[source.index("aGrp")..-1]
      content = content[content.index("=")+1..-1]

      file = File.new "#{dir_name}/#{fases[fase-1]}-#{tipos[tipo-1]}.json", "w"
      file.write content
      file.close
    end
  end
end