***
# Содержание #
1.   [Введение](https://github.com/kulisworm/PCTelegramNotification#%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5 "Описание программы") 
2.   [Файл конфигурации](https://github.com/kulisworm/PCTelegramNotification#to-do "Настройка программы") 
3.   [Установка в kali/ubuntu/debian](https://github.com/kulisworm/PCTelegramNotification#kalidebianubuntu "Установка программы на linux") 
4.   [Установка в windows](https://github.com/kulisworm/PCTelegramNotification#windows-%D0%B0%D0%BB%D1%8C%D1%84%D0%B0 "Установка программы на windows")
***
# Введение #  
Программа выполняет роль уведомления в телеграм через бота о включении и выключении пк  
## Как это работает? ##  
Программа добавляется в автозагрузку системы и при её включение ,включается и программа , которая сразу отсылает уведомление об этом в телеграм , чекер запускается отдельно и позволяет отслеживать работу программы , в случае если она была нарушена , то уведомление также не заставит себя ждать  
***
## To-Do ##  
> Управление с бота телеграм (выключить , перезагрузить и тд)  
> Уведомление об открытии папок и приложений , указанных в файле конфигурации  
***
## Настройка ##
```token```  
токен вашего бота для уведомлений , можно получить у @BotFather  
```chat_id```  
можно получить у @getmyid_bot  
```enablechecker```  
Включение и выключение чекера работы программы , *true* - включить , *false* - выключить  
***Если вы на линуксе , поставьте значение false , в противном случае чекер не даст запустится скрипту (чекер на линуксе всегда считает что скрипт закрыт)***  
***
# Установка #  
##  Kali\debian\ubuntu ##  
```git clone https://github.com/kulisworm/PCTelegramNotification```  
Переходим в папку с программой:  
```cd PCTelegramNotification```  
```sudo apt install python```  
Выдача прав скрипту установки:  
```chmod +x linux-install.sh```  
Запускаем установщик и ждём:
```./linux-install.sh```  
или  
```bash linux-install.sh```  
***
## Windows (альфа) ##  
***Прошу заметить , что стабильной версии на windows еще нет , поэтому установка только через python***  
1.   Устанавливаем python3 c [оффициального сайта](https://www.python.org/ "python3") 
2.   Cкачиваем репозиторий с программой и распаковываем в удобное место 
3.   запускаем файл win-install.bat от имени администратора и ждём  
После этого выполняем настройку программы и запускаем файл ```main.pyw``` как python файл и добавляем в автозагрузку системы  
***Добавление файла в автозагрузку***  
1.   Жмём ```WIN + R``` 
2.   В открывшемся окне пишем ```shell:startup``` 
3.   В открывшуюся папку переносим все файлы программы 
*Всё*  
***
Способ установки на windows является очень нестабильным. Я в скором времени для windows выложу отдельный ***exe*** файл

