# Fixing the login without errors
exec { 'errorfix':
command  => '/usr/bin/env sed -i "s/holberton/" /etc/security/limits.conf',
provider => shell,
}
