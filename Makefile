all:
	spectool -g -R nostt-1.0.spec
	rpmbuild -v -ba --clean nostt-1.0.spec

.PHONY: all
