# Client configuration file (w/ Puppet)

file_line { 'Turn off passwd':
  ensure => 'absent',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}

file_line { 'Declare identity':
  ensure => 'absent',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}