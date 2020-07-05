# benchmarking Apache Server
exec {'benchmarking':
command => "sudo sed -i 's/15/3000/g' /etc/default/nginx; sudo service nginx restart",
path    => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
}
