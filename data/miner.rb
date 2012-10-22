def download(source, target, varname)
  require 'open-uri'
  puts "Downloading #{source}..."
  begin
    source = open("http://www.fuvest.br/#{source}") { |f| f.read }
  rescue
    puts "Can't download #{source}!"
    return
  end
  content = source[source.index(varname)..-1]
  content = content[content.index("=")+1..-1]

  file = File.new target, "w"
  file.write content
  file.close
end

Dir::mkdir Dir::pwd+"/json" if !FileTest::directory?(Dir::pwd+"/json")

anos = (1995..2012)
fases = ["inscritos","2a_fase", "1a_chamada", "ultima_chamada"]
tipos = ["regiao", "carreira", "carreira_campus"]

anos.each do |ano|
  dir_name = Dir::pwd + "/json/" + "#{ano}"
  Dir::mkdir dir_name if !FileTest::directory?(dir_name)
  download "vest#{ano}/js/qase_quest_#{ano}.js", "#{dir_name}/questoes.json", "aQst"
  (1..4).each do |fase|
    (1..3).each do |tipo|
      download "vest#{ano}/js/qase_grupos_#{fase}_#{tipo}_#{ano}.js", "#{dir_name}/#{fases[fase-1]}-#{tipos[tipo-1]}.json", "aGrp"
    end
  end
end