httpd:
	ansible-playbook httpd.yml

mysql:
	ansible-playbook mysql.yml

mysql-test:
	python3 python/mysql-test.py
