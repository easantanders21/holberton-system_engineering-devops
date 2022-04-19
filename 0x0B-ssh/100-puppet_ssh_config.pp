# create a simple hostname and ip host entry
file_line{ 'disable password login':
  ensure => 'present',
  path   => '/etc/ssh/sshd_config',
  line   => '    PasswordAuthentication no',
}
file_line { 'Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
