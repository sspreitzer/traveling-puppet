NAME	?= traveling-puppet
VERSION	?= 3.8.4
TRUBY   ?= traveling-ruby-20150715-2.1.6-linux-x86_64.tar.gz
GEMS	?= json_pure-1.8.3.gem deep_merge-1.0.1.gem hiera-1.3.4.gem facter-2.4.4.gem puppet-3.8.4.gem

all: $(NAME)-$(VERSION).tar.gz

$(TRUBY):
	wget http://d6r77u77i8pq3.cloudfront.net/releases/$(TRUBY)

$(GEMS):
	for i in $(GEMS); do \
		wget https://rubygems.org/downloads/$$i; \
	done

$(NAME)-$(VERSION).tar.gz: $(GEMS) $(TRUBY)
	mkdir -p $(NAME)-$(VERSION)
	cp -r scripts $(NAME)-$(VERSION)/
	cd $(NAME)-$(VERSION); tar xzf ../$(TRUBY)
	cd $(NAME)-$(VERSION); for i in $(GEMS); do \
		./bin/gem install --no-ri --no-rdoc -E -n ./bin --local ../$$i; \
	done
	tar czf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)

rpm: $(NAME)-$(VERSION).tar.gz
	cp -f $(NAME)-$(VERSION).tar.gz $(shell rpm --eval '%{_sourcedir}')/
	rpmbuild -ba $(NAME).spec

clean:
	rm -rf $(GEMS) $(TRUBY) $(NAME)-$(VERSION) $(NAME)-$(VERSION).tar.gz
