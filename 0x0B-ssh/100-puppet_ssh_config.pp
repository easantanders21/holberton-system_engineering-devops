# create a simple hostname and ip host entry
file_line{ 'disable password login':
  ensure => 'absent',
  path => '/etc/ssh/sshd_config',
  line => '    PasswordAuthentication no',
}
file_line { 'Identity file':
  ensure => 'absent',
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}
