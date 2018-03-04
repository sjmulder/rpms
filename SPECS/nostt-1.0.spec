%define name		nostt
%define version		1.0
%define release		1
%define buildroot	%{name}-%{version}
%define bindir		usr/bin
%define man1dir		usr/share/man/man1
%define docdir		usr/share/doc/%{name}
%define debug_package	%{nil}

BuildRoot:	%{buildroot}
Summary:	nostt
License:	BSD2CLAUSE
Name:		nostt
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}.tar.gz
Prefix:		/usr
Group:		Application/Multimedia

%description
Command line NOS Teletekst reader, the Dutch teletext service.

%prep
%setup -q

%build
make

%install
install -d %{buildroot}/%{bindir} \
           %{buildroot}/%{man1dir} \
	   %{buildroot}/%{docdir}
install -s nostt %{buildroot}/%{bindir}/
install nostt.1 %{buildroot}/%{man1dir}/
install README.md LICENSE.md %{buildroot}/%{docdir}/

%files
/%{bindir}/nostt

%doc
/%{man1dir}/nostt.1.gz
/%{docdir}/README.md
/%{docdir}/LICENSE.md
