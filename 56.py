num=0 #присваиваем значение для num
with open("text.txt", "r",encoding= "utf-8") as read_file, open("output.txt", "w", encoding= "utf-8") as write_file: #открывааем файлы на чтение и запись 
   for line in read_file: # пока line в файле открытом на чтение 
       num+=1 #каждый раз num увеличивается на 1
       write_file.write(str(num) + '.')# записываем num с точкой после неё в другой файл 
       write_file.write(line) #запись line в другой файл 