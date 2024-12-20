#!/bin/bash
mysql -u root -ppassword user_info < "/docker-entrypoint-initdb.d/sql/users-scheme.sql"
mysql -u root -ppassword user_info < "/docker-entrypoint-initdb.d/sql/users-insert.sql"
