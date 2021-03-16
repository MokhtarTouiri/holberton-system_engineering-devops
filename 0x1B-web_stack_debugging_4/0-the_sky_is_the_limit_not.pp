# the sky is the limit not
exec { 'fix nginx':
  path    => '/bin/',
  command => 'sed -i \'s/^ULIMIT=.*/ULIMIT="-n 4096"/g\' /etc/default/nginx',
}
exec { 'nginx restart':
  path    => '/etc/init.d/',
  command => 'sudo service nginx restart',
}
