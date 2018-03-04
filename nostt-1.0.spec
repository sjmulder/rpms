%define debug_package	%{nil}

Name:		nostt
Version:	1.0
Release:	1%{?dist}
Summary:	NOS Teletekst reader
Group:		Application/Multimedia
License:	BSD
URL:		https://github.com/sjmulder/nostt
Source0:	https://github.com/sjmulder/nostt/releases/download/1.0/nostt-1.0.tar.gz

%description
Command line NOS Teletekst reader, the Dutch teletext service.

%prep
%autosetup

%build
make

%install
install -d %{buildroot}/%{_bindir} \
           %{buildroot}/%{_mandir}/man1 \
	   %{buildroot}/%{_docdir}/nostt
install -s nostt %{buildroot}/%{_bindir}/
install nostt.1 %{buildroot}/%{_mandir}/man1/
install README.md LICENSE.md %{buildroot}/%{_docdir}/nostt/

%files
/%{_bindir}/nostt
/%{_mandir}/man1/nostt.1.gz
/%{_docdir}/nostt/README.md
/%{_docdir}/nostt/LICENSE.md
