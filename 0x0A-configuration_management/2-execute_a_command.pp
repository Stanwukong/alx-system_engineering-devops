# This manifest kills a process called killmenow.
exec { 'kill_process':
  command => '/usr/bin/pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  onlyif  => '/bin/pgrep killmenow'
}
