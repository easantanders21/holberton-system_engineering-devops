# task 0 Web stack debugging #4

exec { 'change ulimit':
    path    => '/bin',
    command => "sed -i 's/15/2000/g' /etc/default/nginx"
}

exec { 'nging restart':
    path    => '/etc/init.d',
    command => 'nginx restart'
}