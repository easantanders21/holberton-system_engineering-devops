# Client configuration file (w/ Puppet)

file_line { 'Turn off password':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}

file_line { 'Add identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}