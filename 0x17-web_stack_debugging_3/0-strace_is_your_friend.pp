# strace is your friend
exec {'fix err':
  path    => '/bin',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
