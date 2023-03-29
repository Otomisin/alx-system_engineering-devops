# creates a file in /tmp
file { '/alx-system_engineering-devops/0x0A-configuration_management/hello.txt':
  ensure => file,
  content => 'Hello, world!',
}


