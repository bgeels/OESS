NAME= oess-frontend
VERSION = 1.1.5

rpm:	dist
	rpmbuild -ta dist/$(NAME)-$(VERSION).tar.gz

clean:	
	rm -rf dist/$(NAME)-$(VERSION)
	rm -rf dist

dist:
	rm -rf dist/$(NAME)-$($VERSION)
	mkdir -p dist/$(NAME)-$(VERSION)
	mkdir -p dist/$(NAME)-$(VERSION)/www
	mkdir -p dist/$(NAME)-$(VERSION)/www/openlayers
	cp www/openlayers/OpenLayers.js dist/$(NAME)-$(VERSION)/www/openlayers/
	cp -r www/admin  www/css  www/html_templates  www/index.cgi  www/js_templates  www/js_utilities  www/media dist/$(NAME)-$(VERSION)/www/
	cp -r Makefile webservice/ conf/ docs/ $(NAME).spec dist/$(NAME)-$(VERSION)/
	cd dist; tar -czvf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)/ --exclude .svn --exclude tiles --exclude yui
