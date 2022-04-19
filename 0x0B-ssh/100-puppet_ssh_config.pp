# create a simple hostname and ip host entry
include stdlib
file_line{'disable password login':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
  ensure => 'absent',
}
file_line { 'Identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  ensure => 'absent',
}
