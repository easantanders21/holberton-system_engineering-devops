# create a simple hostname and ip host entry
include stdlib
file_line{'disable password login':
  ensure => 'absent',
  path => '/etc/ssh/sshd_config',
  line => '    PasswordAuthentication no',
  replace => true,
}
file_line { 'Identity file':
  ensure => 'absent',
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
  replace => true,
}
