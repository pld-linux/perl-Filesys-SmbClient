# TODO:
# - make cgi scripts from doc as separate packages
%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	SmbClient
Summary:	Filesys::SmbClient perl module
Summary(pl):	Modu³ perla Filesys::SmbClient
Name:		perl-Filesys-SmbClient
Version:	1.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-notest.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	libsmbclient-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys::SmbClient.

%description -l pl
Filesys::SmbClient.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
autoconf
%configure
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes smb2www-2.cgi smb2www.css
%{perl_sitearch}/Filesys/*.pm
%dir %{perl_sitearch}/auto/Filesys/SmbClient
# this is NOT duplicate:
%dir %{perl_sitearch}/auto/Filesys/Smbclient
%dir %{perl_sitearch}/auto/Filesys/Smbclient/libauthSamba
%attr(755,root,root) %{perl_sitearch}/auto/Filesys/SmbClient/SmbClient.so
%attr(644,root,root) %{perl_sitearch}/auto/Filesys/SmbClient/SmbClient.bs
%attr(644,root,root) %{perl_sitearch}/auto/Filesys/Smbclient/libauthSamba/libauthSamba.a
%{_mandir}/man3/*
