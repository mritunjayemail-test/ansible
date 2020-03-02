httpd:
	ansible-playbook httpd.yml

mysql:
	ansible-playbook mysql.yml

mysql-test:
	python3 python/mysql-test.py

gather-facts:
	ansible-playbook playbook/gather-facts.yml

lookup:
	ansible-playbook playbook/lookup.yml

packer:
	ansible-playbook packer.yml

terraform:
	ansible-playbook terraform.yml
