***
# Содержание #
1.   [Введение](https://github.com/kulisworm/PCTelegramNotification#%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5 "Описание программы") 
2.   [Файл конфигурации](https://github.com/kulisworm/PCTelegramNotification#to-do "Настройка программы") 
3.   [Установка в kali/ubuntu/debian](https://github.com/kulisworm/PCTelegramNotification#kalidebianubuntu "Установка программы на linux") 
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
