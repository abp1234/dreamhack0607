<?php
    $directory = './uploads/';
    $scanned_directory = array_diff(scandir($directory), array('..', '.', 'index.html'));
    foreach ($scanned_directory as $key => $value) {
        echo "<li><a href='{$directory}{$value}'>".$value."</a></li><br/>";
    }
?> 