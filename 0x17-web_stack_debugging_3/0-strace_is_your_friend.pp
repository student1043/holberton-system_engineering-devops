# Fixing Wordpress Website Issues
exec {'Hot Fix':
path 	 => ['/usr/bin', '/bin'],
provider => 'shell',
command  => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}
