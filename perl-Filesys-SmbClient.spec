# TODO:
# - make cgi scripts from doc as separate packages
#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filesys
%define		pnam	SmbClient
Summary:	Filesys::SmbClient Perl module
Summary(cs):	Modul Filesys::SmbClient pro Perl
Summary(da):	Perlmodul Filesys::SmbClient
Summary(de):	Filesys::SmbClient Perl Modul
Summary(es):	Módulo de Perl Filesys::SmbClient
Summary(fr):	Module Perl Filesys::SmbClient
Summary(it):	Modulo di Perl Filesys::SmbClient
Summary(ja):	Filesys::SmbClient Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Filesys::SmbClient ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Filesys::SmbClient
Summary(pl):	Modu³ Perla Filesys::SmbClient
Summary(pt):	Módulo de Perl Filesys::SmbClient
Summary(pt_BR):	Módulo Perl Filesys::SmbClient
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Filesys::SmbClient
Summary(sv):	Filesys::SmbClient Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Filesys::SmbClient
Summary(zh_CN):	Filesys::SmbClient Perl Ä£¿é
Name:		perl-Filesys-SmbClient
Version:	1.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-notest.patch
BuildRequires:	autoconf
BuildRequires:	libsmbclient-devel
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _noautocompressdoc *.cgi

%description
Filesys::SmbClient Perl module.

%description -l cs
Modul Filesys::SmbClient pro Perl.

%description -l da
Perlmodul Filesys::SmbClient.

%description -l de
Filesys::SmbClient Perl Modul.

%description -l es
Módulo de Perl Filesys::SmbClient.

%description -l fr
Module Perl Filesys::SmbClient.

%description -l it
Modulo di Perl Filesys::SmbClient.

%description -l ja
Filesys::SmbClient Perl ¥â¥¸¥å¡¼¥ë.

%description -l ko
Filesys::SmbClient ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Filesys::SmbClient.

%description -l pl
Modu³ Perla Filesys::SmbClient.

%description -l pt
Módulo de Perl Filesys::SmbClient.

%description -l pt_BR
Módulo Perl Filesys::SmbClient.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Filesys::SmbClient.

%description -l sv
Filesys::SmbClient Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Filesys::SmbClient.

%description -l zh_CN
Filesys::SmbClient Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__autoconf}
%configure
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes smb2www-2.cgi smb2www.css
%dir %{perl_sitearch}/Filesys
%{perl_sitearch}/Filesys/*.pm
%dir %{perl_sitearch}/auto/Filesys
%dir %{perl_sitearch}/auto/Filesys/SmbClient
# empty autosplit.ix
#%{perl_sitearch}/auto/Filesys/SmbClient/autosplit.ix
%{perl_sitearch}/auto/Filesys/SmbClient/SmbClient.bs
%attr(755,root,root) %{perl_sitearch}/auto/Filesys/SmbClient/SmbClient.so
# this is NOT duplicate:
#%dir %{perl_sitearch}/auto/Filesys/Smbclient
#%dir %{perl_sitearch}/auto/Filesys/Smbclient/libauthSamba
#%{perl_sitearch}/auto/Filesys/Smbclient/libauthSamba/libauthSamba.a
%{_mandir}/man3/*
