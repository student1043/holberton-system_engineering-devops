# Task 2
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/',
}

