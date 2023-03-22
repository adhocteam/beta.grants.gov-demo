rebuild:
	go run grantsxmltosqlite.go < ~/Downloads/GrantsDBExtract20230307v2.xml > output.json
	sqlite3 db.sqlite3 'delete from search_opportunity'
	sqlite3 db.sqlite3 < insert.sql
	yes | python manage.py search_index --rebuild
