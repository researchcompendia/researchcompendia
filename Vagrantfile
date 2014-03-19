# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "debian-70rc1-x64-vbox4210"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/debian-70rc1-x64-vbox4210.box"
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.ssh.forward_agent = true
  config.vm.provision :shell, :path => "bootstrap.sh"
end
