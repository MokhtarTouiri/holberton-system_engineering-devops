#executing my manifest
exec { 'pkill killmenow':
command  => 'pkill killmenow',
path     => '/usr/bin/env',
provider => 'shell',
}
