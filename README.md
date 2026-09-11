# parse_bm_tg
Выборка разговорных групп из BM для их автоматического обновления на сайте.

Переходим в /tmp и запускаем скрипт. Авторизация на BM не нужна. После окончания работы скрипта в этой папке видим tg.txt который копируем в /var/www/html/

В php страничке создаём форму для его отображения:

                 <?php
                 $filePath = __DIR__ . '/tg.txt';
                 if (file_exists($filePath) && is_readable($filePath)) {
                     $fileContent = file_get_contents($filePath);
                     echo "<pre>" . htmlspecialchars($fileContent) . "</pre>";
                 } else {
                     echo "<p>Файл <code>tg.txt</code> не найден или недоступен для чтения.</p>";
                 }
                 ?>

