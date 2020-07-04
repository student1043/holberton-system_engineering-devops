# Fixing Wordpress Website Issues
exec {'Hot Fix':
path     => ['/usr/bin', '/bin'],
provider => 'shell',
command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
}
