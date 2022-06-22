# Программа-уведомитель процентного изменения цены акций :chart:
___
:round_pushpin: _Процентное изменение цены: Цена продажи минус первоначальная цена покупки. Результатом является прибыль или убыток. Прибыль или убыток делим на первоначальную цену покупки. Умножаем результат на 100, чтобы получить процентное изменение цены акции._
___

:alarm_clock: При запуске, программа мониторит процент изменения фондового индекса __CROBEX__[^1], уведомляя пользователя об изменении цены каждый установленный интервал времени.

>print(f"Price in defined range {text}%.. no need to sent alert.")


:e-mail: Программа отправляет емэйл на указанный почтовый адрес, когда цена акций становится ниже установленного порога.

```
    threshold = -0.10
    if float(text) < threshold:
      send_email(str(text))
      print("Email Alert Sent!")
```

* :croatia: Сайт _Загребской фондовой биржи_. Процент изменения индекса _CROBEX_ показан зеленым цветом.
<img width="1425" alt="screen1" src="https://user-images.githubusercontent.com/97599612/174771317-d1078f8e-6ea2-47d2-8c03-1f6d2e0ec717.png">


* :inbox_tray: Письмо, информирующее пользователя о том, что цена акций, входящих в индекс, ниже установленного порога. 
<img width="526" alt="mail" src="https://user-images.githubusercontent.com/97599612/174771297-ce463899-51ea-4022-b363-ecd9717d98b6.png">


[^1]: CROBEX — ключевой хорватский фондовый индекс, рассчитывающийся на Загребской фондовой бирже. По состоянию на 2022 год в индекс входит 21 компания.