# TODO:
# - make cgi scripts from doc as separate packages
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filesys
%define		pnam	SmbClient
Summary:	Filesys::SmbClient - interface for access Samba filesystem
Summary(pl):	Filesys::SmbClient - interfejs dostêpu do systemu plików Samby
Name:		perl-Filesys-SmbClient
Version:	1.5
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d5fdb54c7a36053bbf0e4f77c17fc885
Patch0:		%{name}-notest.patch
BuildRequires:	autoconf
BuildRequires:	libsmbclient-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _noautocompressdoc *.cgi

%description
Filesys::SmbClient Perl module provides interface to access routine
defined in libsmbclient.so and, using this routine, Samba filesystem.

%description -l pl
Modu³ Perla Filesys::SmbClient stanowi interfejs dostêpu do procedury
zdefiniowanej w libsmbclient.so i, za po¶rednictwem tej procedury, do
systemu plików Samby.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__autoconf}
%configure
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes smb2www-2.cgi smb2www.css
%dir %{perl_vendorarch}/Filesys
%{perl_vendorarch}/Filesys/*.pm
%dir %{perl_vendorarch}/auto/Filesys
%dir %{perl_vendorarch}/auto/Filesys/SmbClient
# empty autosplit.ix
#%%{perl_vendorarch}/auto/Filesys/SmbClient/autosplit.ix
%{perl_vendorarch}/auto/Filesys/SmbClient/SmbClient.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Filesys/SmbClient/SmbClient.so
# this is NOT duplicate:
#%dir %{perl_vendorarch}/auto/Filesys/Smbclient
#%dir %{perl_vendorarch}/auto/Filesys/Smbclient/libauthSamba
#%%{perl_vendorarch}/auto/Filesys/Smbclient/libauthSamba/libauthSamba.a
%{_mandir}/man3/*
