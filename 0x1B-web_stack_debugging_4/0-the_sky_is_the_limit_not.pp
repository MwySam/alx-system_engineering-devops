# Increase limit of requests to nginx server

exec { 'fix--for-nginx':
  command => "sed -i 's/15/4096/' /etc/default/nginx; sudo service nginx restart",
  path    => ['/usr/local/bin/:/bin/', '/usr/sbin']
}
