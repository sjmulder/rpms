RPMFLAGS=	-D"_topdir `pwd`" -v
TARBALLS=	SOURCES/nostt-1.0.tar.gz

all: $(TARBALLS)
	rpmbuild $(RPMFLAGS) -ba --clean SPECS/nostt-1.0.spec

SOURCES:
	mkdir -p SOURCES

SOURCES/nostt-1.0.tar.gz: | SOURCES
	curl -Lo $@ https://github.com/sjmulder/nostt/releases/download/1.0/nostt-1.0.zip

.PHONY: all
