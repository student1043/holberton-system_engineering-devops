# Puppet Project Task 0
file { '/tmp/holberton':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}

