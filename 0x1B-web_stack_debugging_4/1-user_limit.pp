# User limit
file { 'remove user limit':
  ensure  => file,
  path    => '/etc/security/limits.conf',
  content => '\n'
}
