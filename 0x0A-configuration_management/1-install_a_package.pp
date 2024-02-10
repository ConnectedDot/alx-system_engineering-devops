# install flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}


class main {
  package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }
}

include main